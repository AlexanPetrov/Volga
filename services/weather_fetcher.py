import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime, timezone
from dotenv import load_dotenv
import os
import yaml
from database.models import WeatherData

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

API_URL = config['api_url']
LOCATION = config['location']

def fetch_weather_data():
    session = Session()
    try:
        response = requests.get(f"{API_URL}?latitude=55.7558&longitude=37.6176&hourly=temperature_2m,wind_speed_10m,wind_direction_10m,pressure_msl,precipitation")
        response.raise_for_status()

        data = response.json()
        print("API Response Data:", data)

        temperature = data['hourly']['temperature_2m'][0]
        wind_speed = data['hourly']['wind_speed_10m'][0]
        wind_direction = data['hourly']['wind_direction_10m'][0]
        pressure = data['hourly']['pressure_msl'][0]
        precipitation = data['hourly']['precipitation'][0]

        weather_record = WeatherData(
            temperature=temperature,
            wind_speed=wind_speed,
            wind_direction=wind_direction,
            pressure=pressure,
            precipitation=precipitation,
            timestamp=datetime.now(timezone.utc)
        )

        session.add(weather_record)
        session.commit()

        print("Weather data fetched and stored successfully.")

    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except Exception as e:
        print(f"Error saving weather data to the database: {e}")
        session.rollback()
    finally:
        session.close()

fetch_weather_data()
