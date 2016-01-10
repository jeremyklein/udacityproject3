import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500))
    minutes = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    @property
    def serialize(self):

        return {
        'name' : self.name,
        'description': self.description,
        'minutes': self.minutes
        }

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    picture = Column(String(500))
    email = Column(Integer)
    todo = relationship("Todo")

    @property
    def serialize(self):

        return {
        'name' : self.name,
        'picture': self.picture,
        'email': self.email
        }


engine = create_engine('sqlite:///TodoWithUsers.db')


Base.metadata.create_all(engine)
