from sqlalchemy import Column, DateTime, String, Integer, Enum
from db.common import Base
import enum

class MessageType(enum.Enum):
    TEXT=1
    PHOTO=2

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    username = Column(String(10), nullable=False)
    type = Column(Enum(MessageType), nullable=False)
    photo = Column(String(100), nullable=True)
    emoji = Column(String(100), nullable=True)
    text = Column(String(1000), nullable=True)
    date = Column(DateTime, nullable=False, index=True)

    def __init__(self, username, type, date, photo=None, emoji=None, text=None):
        self.username = username
        self.type = type
        self.photo = photo
        self.emoji = emoji
        self.text = text
        self.date = date

    def __repr__(self):
        return '<Message {}'.format(
            self.as_dict()
        )

    def as_dict(self):
        return {
            'username': self.username,
            'type': 'photo' if self.type == MessageType.PHOTO else 'text',
            'photo': self.photo,
            'emoji': self.emoji,
            'text': self.text,
            'date': self.date
        }
