from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from app.utils.config_loader import config

Base = declarative_base()
engine = create_engine(config['database']['url'])

class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    ip = Column(String(15), unique=True)
    model = Column(String(50))
    last_seen = Column(DateTime)
    config_version = Column(String(20))

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    hashed_password = Column(String(100))
    role = Column(String(20))
    # File: app/database/models.py
class Tenant(Base):
    __tablename__ = 'tenants'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    subdomain = Column(String(50), unique=True)
