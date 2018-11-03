from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (CheckConstraint, Column, ForeignKey,
                        Index, Integer, LargeBinary,
                        Numeric, SmallInteger, String, Table, Text, text)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import create_engine
import os

Base = declarative_base()
metadata = Base.metadata


class Clothes(Base):
    __tablename__ = "clothes"
    id = Column(Integer, primary_key=True)
    name = Column(ForeignKey('garment.name'), index=True)
    model = Column(String, nullable=False)
    info = Column(JSONB, nullable=False)

    def to_json(self):
        return {"id": self.id, "name": self.name,
                "model": self.model, "info": self.info}


class Garment(Base):
    __tablename__ = "garment"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    def to_json(self):
        return {"id": self.id, "name": self.name}




# creating tables
if __name__ == '__main__':
    engine = create_engine(os.environ['DATABASE_URL'])
    Base.metadata.create_all(engine)