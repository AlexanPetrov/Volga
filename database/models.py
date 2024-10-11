from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    temperature = Column(Float)
    wind_speed = Column(Float)
    wind_direction = Column(String)
    pressure = Column(Float)
    precipitation = Column(Float)
    timestamp = Column(DateTime)
