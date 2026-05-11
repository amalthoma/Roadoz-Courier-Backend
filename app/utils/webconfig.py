from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.models.webconfiguration import WebConfiguration


async def check_maintenance_mode(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WebConfiguration))
    config = result.scalars().first()
    print("ORDERS API CALLED")
    if config and config.maintenance_mode:
        raise HTTPException(status_code=503,detail="System under maintenance")
    return config