Betterproto for ORD data model
===

This guide describes steps to generate python classes for ORD messages. Here is an example:
```python

from dataclasses import dataclass
from typing import Optional

import betterproto

@dataclass(eq=False, repr=False)
class Percentage(betterproto.Message):
    """Used for things like conversion and yield."""

    value: Optional[float] = betterproto.float_field(1, optional=True, group="_value")
    precision: Optional[float] = betterproto.float_field(
        2, optional=True, group="_precision"
    )
    """Precision of the measurement (with the same units as `value`)."""
```
The tree structures in `ord_tree` rely on these python classes. Type hinting is also included.

1. install protoc compiler, on debian do `sudo apt install protobuf-compiler`
2. install `poetry`: `curl -sSL https://install.python-poetry.org | python3 -`, 
    make sure the executable is in your `PATH`
3. install environment: 
    ```shell
    poetry install -E compiler
    poetry shell
    ```
   there should be an executable `protoc-gen-python_betterproto` in (the venv's) `PATH`
4. download `*.proto` files from [ORD](https://github.com/open-reaction-database/ord-schema/tree/main/proto) to this folder:
   ```bash
    for protoname in reaction dataset
    do
      wget https://raw.githubusercontent.com/open-reaction-database/ord-schema/main/proto/$protoname.proto
      if [[ $protoname == dataset ]]
      then
        sed -i 's/ord-schema\/proto\/reaction.proto/reaction.proto/' $protoname.proto
      fi
    done
   ```
   the `sed` operation is to make the `import` statement in `dataset.proto` matches current structure
5. generate classes
   ```shell
   protoc -I .  --python_betterproto_out=. dataset.proto --experimental_allow_proto3_optional
   ```
   results can be found in [ord/__init__.py](ord/__init__.py)