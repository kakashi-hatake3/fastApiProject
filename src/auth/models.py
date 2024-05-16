from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

from src.database import Base

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON)
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow()),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow())
    role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
