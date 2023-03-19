import ast
from typing import List


def flatten_classes(code: str) -> str:
    tree = ast.parse(code)

    # Get all classes defined in the module
    classes = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            classes.append(node)
            classes.extend(get_nested_classes(node))

    # Create a new module with the flattened classes
    new_code = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            continue
        new_code.append(ast.unparse(node))  # imports

    for cls in classes:
        remove_child_class(cls)
        new_code.append(ast.unparse(cls))

    return "\n\n".join(new_code)


def remove_child_class(node: ast.ClassDef) -> None:
    new_body = []
    for child_node in node.body:
        if not isinstance(child_node, ast.ClassDef):
            new_body.append(child_node)
    if len(new_body) == 0:
        new_body.append(ast.Pass())
    node.body = new_body


def get_nested_classes(node: ast.ClassDef) -> List[ast.ClassDef]:
    nested_classes = []
    for child_node in ast.iter_child_nodes(node):
        if isinstance(child_node, ast.ClassDef):
            nested_classes.append(child_node)
            nested_classes.extend(get_nested_classes(child_node))
    return nested_classes


def reorder_classes(source):
    tree = ast.parse(source)

    # Extract the classes from the AST and sort them topologically
    class_nodes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
    class_dependencies = {}
    for class_node in class_nodes:
        class_dependencies[class_node] = {
            dep.id for dep in ast.walk(class_node) if
            isinstance(dep, ast.Name) and dep.id in [cls.name for cls in class_nodes]
        }
    sorted_classes = []
    while class_dependencies:
        acyclic_nodes = [node for node, deps in class_dependencies.items() if not deps]
        if not acyclic_nodes:
            raise ValueError('Circular dependency found')
        for node in acyclic_nodes:
            del class_dependencies[node]
            sorted_classes.append(node)
            for deps in class_dependencies.values():
                deps.discard(node.name)

    # Rewrite the source code with the sorted classes
    sorted_source = '\n\n'.join([ast.unparse(node) for node in sorted_classes])
    return sorted_source


if __name__ == '__main__':
    with open("reaction_p2p.py", "r") as f:
        src = f.read()
        new_src = flatten_classes(src)
        new_src = reorder_classes(new_src)

    with open("dataset_p2p.py", "r") as f:
        src = f.read()
        new_src1 = flatten_classes(src)
        new_src1 = reorder_classes(new_src1)

    with open("__init__.py", "w") as f:
        f.write(new_src + "\n\n" + new_src1)
