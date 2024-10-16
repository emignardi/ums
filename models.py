from sqlalchemy import Column, Integer, String
from database import Base

# Data Model & Object Relational Mapping
class User(Base):
    __tablename__ = 'users'
    id = Column("id", Integer, primary_key=True, index=True)
    first_name = Column("first_name", String(25), nullable=False)
    last_name = Column("last_name", String(25), nullable=False)
    email = Column("email", String(25), nullable=False)
    phone = Column("phone", String(25), nullable=False)
    address = Column("address", String(25), nullable=False)