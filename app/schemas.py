from pydantic import BaseModel
from typing import List, Optional

class GestureRequest(BaseModel):
    features: List[float]

class GestureResponse(BaseModel):
    gesture: str
    missing_values: Optional[int] = None  
