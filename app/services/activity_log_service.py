from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc
from app.models.activity_log import ActivityLog
from app.models.user import User
from app.schemas.activity_log import ActivityLogListResponse, ActivityLogOut
from typing import Optional

async def get_activity_logs(
    db: AsyncSession,
    page: int = 1,
    size: int = 50,
    franchise_id: Optional[str] = None
) -> ActivityLogListResponse:
    query = select(ActivityLog)
    
    if franchise_id:
        from sqlalchemy import or_
        from app.models.franchise import Franchise
        
        # A user belongs to a franchise if they are an employee (User.franchise_id)
        # OR if they are the franchise owner (Franchise.user_id)
        owner_subquery = select(Franchise.user_id).where(Franchise.id == franchise_id).scalar_subquery()
        query = query.join(User).where(
            or_(
                User.franchise_id == franchise_id,
                User.id == owner_subquery
            )
        )
        
    # Count total
    count_query = select(func.count()).select_from(query.subquery())
    total_result = await db.execute(count_query)
    total = total_result.scalar_one_or_none() or 0

    # Get items
    query = query.order_by(desc(ActivityLog.created_at))
    query = query.offset((page - 1) * size).limit(size)
    
    result = await db.execute(query)
    logs = result.scalars().all()
    
    return ActivityLogListResponse(
        items=[ActivityLogOut.model_validate(log) for log in logs],
        total=total,
        page=page,
        size=size
    )
