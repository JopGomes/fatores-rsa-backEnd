from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from app.database.config import Base


class Primo(Base):
    __tablename__ = 'primo'

    id = Column(BigInteger, primary_key=True, index=True)
    