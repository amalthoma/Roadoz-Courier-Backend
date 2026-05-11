from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from datetime import datetime

from app.core.database import get_db

from app.models.notification import Notification

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.get("")
async def get_notifications(

    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(

        select(Notification)

        .where(
            Notification.expires_at >
            datetime.utcnow()
        )

        .order_by(
            Notification.created_at.desc()
        )
    )

    notifications = result.scalars().all()

    return notifications


@router.put("/{notification_id}/read")
async def mark_notification_read(

    notification_id: str,

    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(

        select(Notification)

        .where(Notification.id == notification_id)
    )

    notification = result.scalars().first()

    if not notification:

        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    notification.is_read = True

    await db.commit()

    return {
        "message":
        "Notification marked as read"
    }