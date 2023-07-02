from typing import Type

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, \
    func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(EmailType, nullable=False, unique=True)
    password = Column(String, nullable=False)

    ads = relationship("Advertisement", back_populates="user")

    def __str__(self):
        f'Id: {self.id},\nEmail: {self.email}'


class Advertisement(Base):
    __tablename__ = 'advertisement'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(256), nullable=False)
    description = Column(Text, nullable=False)
    creation_time = Column(DateTime, server_default=func.now(),
                           nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship(User, back_populates="ads")

    def __str__(self):
        f"Owner's id: {self.owner_id},\nTitle: {self.title},\nDescription:" \
        f" {self.description},\nCreation time: {self.creation_time}"


ORM_MODEL = Advertisement | User
ORM_MODEL_CLS = Type[Advertisement] | Type[User]
