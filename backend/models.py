
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class Wish(Base):
    __tablename__ = "wishes"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(50))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
