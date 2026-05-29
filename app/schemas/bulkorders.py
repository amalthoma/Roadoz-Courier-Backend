from datetime import datetime, date
from typing import Optional, List, Dict, Any
from pydantic import BaseModel



# ============= Pydantic Models for Responses =============

class OrderItemResponse(BaseModel):
    product_name: str
    sku: Optional[str]
    unit_price: float
    qty: int
    total: float

class OrderPackageResponse(BaseModel):
    count: int
    length_cm: float
    breadth_cm: float
    height_cm: float
    vol_weight_kg: float
    physical_weight_kg: float

class OrderTrackingResponse(BaseModel):
    stage: str
    status: str
    pincode: str
    timestamp: Optional[str]

class OrderDetailResponse(BaseModel):
    id: str
    order_number: str
    order_type: str
    status: str
    previous_status: Optional[str]
    payment_method: str
    cod_amount: Optional[float]
    to_pay_amount: Optional[float]
    order_value: float
    total_weight_kg: float
    total_vol_weight_kg: float
    applicable_weight_kg: float
    total_boxes: int
    shipping_charge: float
    gst_number: Optional[str]
    eway_bill_number: Optional[str]
    created_at: str
    updated_at: str
    
    # Addresses
    pickup_address: Optional[Dict]
    delivery_address: Optional[Dict]
    warehouse_addresses: List[Dict]
    franchise_addresses: List[Dict]
    
    # Items and Packages
    items: List[OrderItemResponse]
    packages: List[OrderPackageResponse]
    
    # Tracking History
    tracking_history: List[OrderTrackingResponse]

class BulkOrderDetailResponse(BaseModel):
    id: str
    file_name: str
    order_type: str
    status: str
    total_orders: int
    successful_orders: int
    failed_orders: int
    created_by: str
    franchise_id: Optional[str]
    created_at: str
    updated_at: str
    orders: List[OrderDetailResponse]
    
    
    
    
class DateRangeFilter(BaseModel):
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: Optional[str] = None
    pincode: Optional[str] = None
    page: int = 1
    limit: int = 10    