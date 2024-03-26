import socket

import uvicorn
from ec2_metadata import ec2_metadata
from fastapi import FastAPI

# from sqlalchemy.orm import Session

# from week6 import models, schemas, crud
# from week6.database import engine, SessionLocal
#
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    try:
        return {
            "message": f"Hello update from gitHub actions, {ip_address} {hostname}",
            "metadata": {
                "public_ipv4": ec2_metadata.public_ipv4,
                "public_hostname": ec2_metadata.public_hostname,
                "region": ec2_metadata.region,
                "instance_id": ec2_metadata.instance_id,
                "domain": ec2_metadata.domain
            }
        }
    except:
        return {"message": f"Hello, not on ec2; {ip_address} {hostname}"}


#
# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
#
#
# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
#
#
# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
