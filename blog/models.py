from sqlalchemy import Column, Integer, String, ForeignKey
from blog.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String)
    password = Column(String)
    
    blogs = relationship('Blog', back_populates="creator")

class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User")  # Assuming you have a User model defined
    # Define the relationship inside the Blog class
    creator = relationship("User", back_populates="blogs")

