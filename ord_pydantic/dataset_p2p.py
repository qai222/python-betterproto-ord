# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

import typing

from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic.fields import FieldInfo

from ..reaction_p2p import Reaction, RecordEvent


class Dataset(BaseModel):
    name: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    reactions: typing.List[Reaction] = FieldInfo(default_factory=list)
    reaction_ids: typing.List[str] = FieldInfo(default_factory=list)
    dataset_id: str = FieldInfo(default="")


class DatasetExample(BaseModel):
    dataset_id: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    url: str = FieldInfo(default="")
    created: RecordEvent = FieldInfo()
