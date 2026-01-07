from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import Column, Integer, Float, String, create_engine, select
from sqlalchemy.orm import declarative_base, sessionmaker, Session

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

# Transaction model
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    status = Column(String, default="pending")

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ramp Backend")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schemas
from pydantic import BaseModel

class TransactionCreate(BaseModel):
    amount: float

# Routes
@app.post("/transactions")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    if transaction.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")
    tx = Transaction(amount=transaction.amount)
    db.add(tx)
    db.commit()
    db.refresh(tx)
    return tx

@app.post("/transactions/{transaction_id}/approve")
def approve_transaction(transaction_id: int, db: Session = Depends(get_db)):
    tx = db.get(Transaction, transaction_id)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    if tx.status != "pending":
        raise HTTPException(status_code=400, detail="Transaction already processed")
    tx.status = "approved"
    db.commit()
    db.refresh(tx)
    return tx

@app.post("/transactions/{transaction_id}/reject")
def reject_transaction(transaction_id: int, db: Session = Depends(get_db)):
    tx = db.get(Transaction, transaction_id)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    if tx.status != "pending":
        raise HTTPException(status_code=400, detail="Transaction already processed")
    tx.status = "rejected"
    db.commit()
    db.refresh(tx)
    return tx
