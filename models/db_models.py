import datetime
from sqlalchemy import (
    JSON,
    MetaData,
    Integer,
    String,
    Float,
    TIMESTAMP,
    ForeignKey,
    Table,
    Column,
)


metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("email", String),
    Column("password", String, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.UTC),
    Column("role_id", Integer, ForeignKey("roles.id")),
)
