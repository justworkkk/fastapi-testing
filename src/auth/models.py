import time
from datetime import datetime
from sqlalchemy import (
    JSON,
    Boolean,
    MetaData,
    Integer,
    String,
    Float,
    TIMESTAMP,
    ForeignKey,
    Table,
    Column,
    func,
    DateTime,
)


metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("email", String(length=320), unique=True, nullable=False),
    Column("hashed_password", String(length=1024), nullable=False),
    Column("registered_at", TIMESTAMP(timezone=True), default=datetime.utcnow),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)
