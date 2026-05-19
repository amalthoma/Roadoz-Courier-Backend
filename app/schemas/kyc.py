# from pydantic import BaseModel
# from typing import Optional


# # =====================================================
# # CREATE KYC SCHEMA
# # =====================================================

# class CreateKYCSchema(BaseModel):

#     # ==========================================
#     # BANK DETAILS
#     # ==========================================

#     beneficiary_name: str

#     account_number: str

#     ifsc_code: str

#     account_type: str

#     aadhaar_number: str

#     pan_number: str

#     # ==========================================
#     # BUSINESS INFORMATION
#     # ==========================================

#     company_name: str

#     gst_number: str

#     cin_number: str

#     business_type: str

#     address: str

#     city: str

#     state: str

#     pincode: str



# class KYCResponseSchema(BaseModel):

#     message: str

#     class Config:
#         from_attributes = True