from fastapi import FastAPI, Depends
from schema import UserCreate, UserOut
from database import engine, Base, get_db
from crud import create_user, get_user

app = FastAPI(title="Fastapi + mysql")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.post("/add_user", response_model=UserOut)
async def add_user(user: UserCreate, db=Depends(get_db)):
    return await create_user(db, user)


@app.get("/get_user", response_model=UserOut)
async def list_user(db=Depends(get_db)):
    return await get_user(db)
