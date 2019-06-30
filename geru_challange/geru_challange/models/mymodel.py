from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class GeruChallange(Base):
    __tablename__ = 'Session'
    id = Column(Integer, primary_key=True)
    identifier = Column(Text)
    date = Column(Text)
    url = Column(Text)
    
    def save(cls):
        print('ENTREI')
        pass

Index('identifier', GeruChallange.identifier, unique=True, mysql_length=255)