python -m grpc_tools.protoc -I. --protobuf-to-pydantic_out=. reaction.proto
python -m grpc_tools.protoc -I. --protobuf-to-pydantic_out=. dataset.proto
# postprocess.py does not handle nested class definition, manually reorder `reaction.proto` instead