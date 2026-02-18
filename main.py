from fastapi import FastAPI

from db import get_db,DATABASE_URL
from sqlalchemy import create_engine
import os
from models import Base
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
#cros 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



from fastapi.staticfiles import StaticFiles



# Mount uploads directory to serve files
if not os.path.exists("uploads"):
    os.makedirs("uploads")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


#to create database

engine = create_engine(DATABASE_URL)
# Base.metadata.create_all(engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000,reload=True)