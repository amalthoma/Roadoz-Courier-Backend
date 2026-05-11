from sqlalchemy.ext.asyncio import AsyncSession

from app.models.notification import Notification

from app.websocket.manager import manager


async def create_notification(
    db: AsyncSession,
    title: str,
    message: str,
    type: str = "order",
    order_id: str | None = None,
):

    notification = Notification(
        title=title,
        message=message,
        type=type,
        order_id=order_id,
    )

    db.add(notification)
    await db.commit()
    await db.refresh(notification)
    await manager.broadcast({
        "id": notification.id,
        "title": notification.title,
        "message": notification.message,
        "type": notification.type,
        "is_read": notification.is_read,
        "created_at":
        str(notification.created_at),
    })

    return notification