from pydantic import BaseModel, conlist

class GestureRequest(BaseModel):
    features: conlist(float, min_items=63, max_items=63) 

class GestureResponse(BaseModel):
    gesture: str
