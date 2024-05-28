from sqlalchemy import TIMESTAMP, Column, DateTime, Integer, MetaData, String, Table
from datetime import datetime
from src.database import metadata


operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("currency", String),
    Column("quantity", String),
    Column("instrument_type", String, nullable=True),
    Column("date", TIMESTAMP(timezone=True), default=datetime.utcnow),
    Column("type", String),
)
