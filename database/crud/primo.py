from datetime import datetime
from typing import Any

from sqlalchemy.orm import Session

from app.core.models import RSA, Trade
from app.core.schemas.RSA import RSACreate, RSAUpdate
from app.database.crud.base import BaseCRUD


class PrimoCRUD(BaseCRUD[RSA, RSACreate, RSAUpdate]):

    def __init__(self, db: Session):
        super().__init__(RSA, db)

    def create():
        pass
    def update():
        pass
    def delete():
        pass
