import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from database.models import Base

load_dotenv()

database_url = os.getenv('DATABASE_URL')

engine = create_engine(database_url)

Base.metadata.create_all(engine)

print("Database tables created successfully.")
