from pydantic import BaseModel

class ClientIn(BaseModel):
    id: int
    client_isActive: bool
    client_name: str

class ClientOut(BaseModel):
    id: int
    name: str
    client_isActive: bool