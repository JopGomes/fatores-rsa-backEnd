from pydantic import BaseModel

class RSABase(BaseModel):
    fator1: int | None
    fator2: int | None
    produto: int | None

class RSACreate(RSABase):
    fator1: int 
    fator2: int 
    produto: int

class RSAOut(RSABase):
    fator1: int | None
    fator2: int | None
    produto: int | None
    

    class Config:
        orm_mode = True
