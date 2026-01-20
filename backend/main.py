from fastapi import FastAPI
from database import Base, engine, SessionLocal
from models import Wish
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/wishes")
def create_wish(nickname: str, content: str):
    db = SessionLocal()
    wish = Wish(nickname=nickname, content=content)
    db.add(wish)
    db.commit()
    db.refresh(wish)
    db.close()
    return wish

@app.get("/wishes")
def list_wishes():
    db = SessionLocal()
    wishes = db.query(Wish).order_by(Wish.created_at.desc()).all()
    db.close()
    return wishes