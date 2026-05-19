# import os
# import shutil
# from app.models.user import User
# from fastapi import (APIRouter,Depends,UploadFile,File,Form,HTTPException)
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from app.core.database import get_db
# from app.models.kyc import (BankDetails,PersonalIdentification,BusinessInfo)


# from app.dependencies.role_checker import get_current_user

# router = APIRouter(prefix="/kyc",tags=["KYC"])
# os.makedirs("uploads/aadhaar", exist_ok=True)
# os.makedirs("uploads/pan", exist_ok=True)
# os.makedirs("uploads/cheque", exist_ok=True)
# os.makedirs("uploads/gst", exist_ok=True)


# @router.post("/create")
# async def create_full_kyc(
#     beneficiary_name: str = Form(...),
#     account_number: str = Form(...),
#     ifsc_code: str = Form(...),
#     account_type: str = Form(...),
#     aadhaar_number: str = Form(...),
    
    
#     authorized_person_full_name: str = Form(...),
#     residential_address: str = Form(...),
#     aadhaar_number:str = Form(...),
#     pan_number: str = Form(...),
    
    
#     company_name: str = Form(...),
#     gst_number: str = Form(...),
#     cin_number: str = Form(...),
#     business_type: str = Form(...),
#     address: str = Form(...),
#     city: str = Form(...),
#     state: str = Form(...),
#     pincode: str = Form(...),
    
#     aadhaar_front: UploadFile = File(...),
#     aadhaar_back: UploadFile = File(...),
#     pan_image: UploadFile = File(...),
#     cancelled_cheque: UploadFile = File(...),
#     gst_certificate: UploadFile = File(...),
    

#     db: AsyncSession = Depends(get_db),
#     current_user: User = Depends(get_current_user)):
#     bank_check = await db.execute(select(BankDetails).where(BankDetails.user_id == current_user.id))
#     existing_bank = bank_check.scalar_one_or_none()
#     if existing_bank:
#         raise HTTPException(status_code=400,detail="KYC Already Submitted")
#     aadhaar_front_path = (f"uploads/aadhaar/{aadhaar_front.filename}")
#     with open(aadhaar_front_path, "wb") as buffer:
#         shutil.copyfileobj(aadhaar_front.file,buffer)
#     aadhaar_back_path = (f"uploads/aadhaar/{aadhaar_back.filename}")
#     with open(aadhaar_back_path, "wb") as buffer:
#         shutil.copyfileobj(aadhaar_back.file,buffer)
#     pan_image_path = (f"uploads/pan/{pan_image.filename}")
#     with open(pan_image_path, "wb") as buffer:
#         shutil.copyfileobj(pan_image.file,buffer)
#     cheque_path = (f"uploads/cheque/{cancelled_cheque.filename}")
#     with open(cheque_path, "wb") as buffer:
#         shutil.copyfileobj(cancelled_cheque.file,buffer)
#     gst_path = (f"uploads/gst/{gst_certificate.filename}")
#     with open(gst_path, "wb") as buffer:
#         shutil.copyfileobj(gst_certificate.file,buffer)
#     bank_data = BankDetails(
#         user_id=current_user.id,
#         beneficiary_name=beneficiary_name,
#         account_number=account_number,
#         ifsc_code=ifsc_code,
#         account_type=account_type,
#         cancelled_cheque=cheque_path)
#     db.add(bank_data)
#     personal_data = PersonalIdentification(
#         user_id=current_user.id,
#         aadhaar_number=aadhaar_number,
#         pan_number=pan_number,
#         aadhaar_front=aadhaar_front_path,
#         aadhaar_back=aadhaar_back_path,
#         pan_image=pan_image_path)
#     db.add(personal_data)
#     business_data = BusinessInfo(
#         user_id=current_user.id,
#         company_name=company_name,
#         gst_number=gst_number,
#         cin_number=cin_number,
#         business_type=business_type,
#         address=address,
#         city=city,
#         state=state,pincode=pincode
#         ,gst_certificate=gst_path)
#     db.add(business_data)
#     await db.commit()
#     return {"message": "KYC Created Successfully"}







# @router.get("/kycdetailsbyauth")
# async def get_my_kyc(
#     db: AsyncSession = Depends(get_db),
#     current_user: User = Depends(get_current_user)):
#     bank_result = await db.execute(
#         select(BankDetails).where(BankDetails.user_id == current_user.id))
#     bank_data = bank_result.scalar_one_or_none()
#     personal_result = await db.execute(
#         select(PersonalIdentification).where(PersonalIdentification.user_id == current_user.id))
#     personal_data = personal_result.scalar_one_or_none()
#     business_result = await db.execute(
#         select(BusinessInfo).where(BusinessInfo.user_id == current_user.id))
#     business_data = business_result.scalar_one_or_none()
#     return {"bank_details": bank_data,"personal_identification": personal_data,"business_information": business_data}