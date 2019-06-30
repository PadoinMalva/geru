# pyramidapp/models.py
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)
from .meta import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension
import datetime

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class GeruChallange(Base):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    identifier = Column(Text)
    url = Column(Text)
    datahora = Column(DateTime, default=datetime.datetime.utcnow)
    
    def __init__(self, idsession, endpoint):
        self.identifier = identifier
        self.url = url

Index('identifier', GeruChallange.identifier, unique=True, mysql_length=255)