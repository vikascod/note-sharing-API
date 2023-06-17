from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    
    notes = relationship("Note", back_populates="user")


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="notes")

