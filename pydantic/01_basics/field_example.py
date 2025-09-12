from pydantic import BaseModel
from typing import Optional,List,Dict
class Cart(BaseModel):
    id:int
    items:List[str]
    quantities:Dict[str,int]
class Blog(BaseModel):
    title:str
    content:str
    image_url:Optional[str]=None
    