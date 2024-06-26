from app.banco_dados.database import SessionLocal


async def get_bd():
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()