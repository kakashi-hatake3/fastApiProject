from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

metadata = MetaData()

reservation = Table(
    "reservation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("hotel_name", String, nullable=False),
    Column("count_of_people", Integer, nullable=False),
    Column("reservation_date", TIMESTAMP, default=datetime.utcnow()),
)
