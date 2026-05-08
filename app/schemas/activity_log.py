from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime
from app.schemas.auth import FranchiseInfo

class UserBasicInfo(BaseModel):
    id: str
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)

class ActivityLogOut(BaseModel):
    id: str
    user_id: Optional[str]
    method: str
    path: str
    description: Optional[str] = None
    ip_address: Optional[str]
    created_at: datetime
    user: Optional[UserBasicInfo] = None

    model_config = ConfigDict(from_attributes=True)

class ActivityLogListResponse(BaseModel):
    items: List[ActivityLogOut]
    total: int
    page: int
    size: int
