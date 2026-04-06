from pydantic import BaseModel, EmailStr

class Cliente(BaseModel):
    id: int
    nombre: str
    email: EmailStr