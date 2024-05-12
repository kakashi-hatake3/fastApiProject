from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update
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
    query = select(reservation).filter_by(hotel_name=hotel_name)
    print(query)
    result = await session.execute(query)
    return result.mappings().all()


@router.post("/")
async def add_reservation(new_reservation: ReservationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(reservation).values(**new_reservation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": 200}


@router.post("/update")
async def update_count_of_people_reservation(first_name: str,
                                             second_name: str,
                                             new_count: int,
                                             session: AsyncSession = Depends(get_async_session)):
    stmt = update(reservation).filter_by(first_name=first_name,
                                         second_name=second_name).values(count_of_people=new_count)
    await session.execute(stmt)
    await session.commit()
    return {"status": "updated"}
