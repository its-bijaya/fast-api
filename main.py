from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize the FastAPI app
app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./requests_count.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class RequestCount(Base):
    __tablename__ = "request_count"
    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer, default=0)

SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

# Increment count in the database
def increment_count():
    db = SessionLocal()
    count_row = db.query(RequestCount).first()
    if not count_row:
        count_row = RequestCount(count=1)
        db.add(count_row)
    else:
        count_row.count += 1
    db.commit()
    db.refresh(count_row)
    db.close()
    return count_row.count

@app.get("/count")
async def get_count():
    current_count = increment_count()
    return {"count": current_count}