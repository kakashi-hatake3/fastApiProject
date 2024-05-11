from datetime import datetime
from pydantic import BaseModel


class ReservationCreate(BaseModel):
    id: int
    hotel_name: str
    count_of_people: int
    reservation_date: datetime
