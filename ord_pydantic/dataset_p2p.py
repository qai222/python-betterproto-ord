# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.1.7.4](https://github.com/so1n/protobuf_to_pydantic)
import typing

from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel, Field

from .reaction_p2p import Reaction, RecordEvent


class Dataset(BaseModel):

    name: str = Field(default="") 
    description: str = Field(default="") 
    reactions: typing.List[Reaction] = Field(default_factory=list) 
    reaction_ids: typing.List[str] = Field(default_factory=list) 
    dataset_id: str = Field(default="") 



class DatasetExample(BaseModel):

    dataset_id: str = Field(default="") 
    description: str = Field(default="") 
    url: str = Field(default="") 
    created: RecordEvent = Field() 

