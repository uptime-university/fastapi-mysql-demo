from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from schema import UserCreate


async def create_user(db: AsyncSession, user: UserCreate):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def get_user(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()
