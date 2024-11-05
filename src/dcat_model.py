from pydantic import BaseModel
from typing import List, Union
from datetime import date

class Resource(BaseModel):
    description: str = None
    uri: str = None
    title: str = None
    license : str = None
    identifier: str
    publisher: str = None
    contactPoint: str = None
    hasCurrentVersion: str = None
    theme: List[str] = None
    status: str = None
    conformsTo: List[any] = None
    modified: date = None

    
class Distribution(Resource):
    accessURL: str = None
    format: any = None

class Dataset(Resource, BaseModel):
    distribution: List[Distribution]=None
    spatial: any = None
    temporal: any = None
    wasDerivedFrom: List[Union[str, Resource]] = None
    


