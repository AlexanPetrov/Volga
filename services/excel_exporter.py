from openpyxl import Workbook
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from database.models import WeatherData


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def export_to_excel():
    try:
        wb = Workbook()
        ws = wb.active
        ws.title = "Weather Data"

        ws.append(["ID", "Temperature (°C)", "Wind Speed (m/s)", "Wind Direction", "Pressure (mm Hg)", "Precipitation (mm)", "Timestamp"])

        weather_records = session.query(WeatherData).order_by(WeatherData.timestamp.desc()).limit(10).all()
        print(f"Fetched {len(weather_records)} records from the database.")

        for record in weather_records:
            ws.append([record.id, record.temperature, record.wind_speed, record.wind_direction, record.pressure, record.precipitation, record.timestamp])

        file_path = "data/weather_data.xlsx"
        wb.save(file_path)
        print(f"Data successfully exported to {file_path}.")

    except Exception as e:
        print(f"Error exporting data to Excel: {e}")

    finally:
        session.close()

export_to_excel()
