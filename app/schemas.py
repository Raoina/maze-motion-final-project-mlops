from pydantic import BaseModel
from typing import List

class GestureRequest(BaseModel):
    features: List[float]  

class GestureResponse(BaseModel):
    gesture: str        
