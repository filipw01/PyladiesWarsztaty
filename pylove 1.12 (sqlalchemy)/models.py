from sqlalchemy import Column
from sqlalchemy.types import Integer
from sqlalchemy.types import String
from main import db


class BlogPosts(db.Model):
    """
    Blog post model
    """
    __tablename__ = 'blogpost'
    id = Column(Integer, autoincrement=True, primary_key=True)
    sub = Column(String(100), unique=True)
    content = Column(String(2000))
