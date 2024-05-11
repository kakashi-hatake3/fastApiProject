from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.booking.models import reservation
from src.booking.schemas import ReservationCreate
from src.database import get_async_session

router = APIRouter(
    prefix="/booking",
    tags=["Booking"]
)


@router.get("/")
async def get_reservations(hotel_name: str, session: AsyncSession = Depends(get_async_session)):
    query = select(reservation).where(reservation.c.hotel_name == hotel_name)
    print(query)
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def add_reservation(new_reservation: ReservationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(reservation).values(**new_reservation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": 200}
