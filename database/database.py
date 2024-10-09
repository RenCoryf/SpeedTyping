from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine=create_async_engine(
    "sqlite+aiosqlite:///task.db"
)

new_session=async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class TaskOrm(Model):
    table_name="tasks"

    id: Mapped[int]=mapped_column()
    email: Mapped[str]
    password: Mapped[str]
    