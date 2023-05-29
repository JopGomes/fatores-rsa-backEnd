from pydantic import BaseModel

class RSABase(BaseModel):
    RSAname: str | None = None


class RSACreate(RSABase):
    RSAname: str


class RSAUpdate(RSABase):
    pass;


class RSAOut(RSABase):
    id: int
    

    class Config:
        orm_mode = True
