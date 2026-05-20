# from sqlalchemy import Column, Integer, String, ForeignKey, DateTime,Text
# from sqlalchemy.orm import relationship
# from app.core.database import Base
# from datetime import datetime


# class BankDetails(Base):
#     __tablename__ = "bank_details"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     beneficiary_name = Column(String)
#     account_number = Column(String)
#     ifsc_code = Column(String)
#     account_type = Column(String)
#     cancelled_cheque = Column(String)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     user = relationship("User",back_populates="bank_details")




# class PersonalIdentification(Base):
#     __tablename__ = "personal_identification"
    
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     authorized_person_full_name = Column(String,nullable=False)
#     residential_address = Column(Text,nullable=False)
#     aadhaar_number = Column(String(12),nullable=False)
#     pan_number = Column(String(10),nullable=False)
#     aadhaar_front = Column(String,nullable=False)
#     aadhaar_back = Column(String,nullable=False)
#     pan_image = Column(String,nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     user = relationship("User",back_populates="personal_identification")




  
    
# class BusinessInfo(Base):
#     __tablename__ = "business_info"
    
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     registered_company_name = Column(String,nullable=False)
#     cin_registration_number = Column(String,nullable=False)
#     gst_number = Column(String,nullable=False)
#     city = Column(String,nullable=False)
#     state = Column(String,nullable=False)
#     pincode = Column(String,nullable=False)
#     gst_certificate = Column(String,nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     user = relationship("User",back_populates="business_info")
    
    
    
 