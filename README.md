Volga Weather Data Fetcher:

This project is a Python-based weather data fetching application that periodically retrieves weather information for a specified location and stores it in a PostgreSQL database. It also allows exporting the data to an Excel file.

Project Stack:

Programming Language: Python 3
Frameworks/Libraries:
FastAPI: Backend framework for handling data fetching logic.
SQLAlchemy: ORM for interacting with PostgreSQL.
Requests: For making HTTP requests to the weather API.
Openpyxl: For generating and handling Excel files.
YAML: For configuration management.
dotenv: For environment variable management.
asyncio and schedule: For asynchronous task scheduling.
Database: PostgreSQL
Configuration Management: .env file and config.yaml
Environment: .venv (Python Virtual Environment)
How to Set Up and Run the Application

Prerequisites:

Python 3: Make sure you have Python 3 installed on your system.
PostgreSQL: Ensure that PostgreSQL is installed and running.
Git: For version control and cloning the repository.

1. Clone the Repository

git clone <your-github-repo-url>
cd Volga

2. Create and Activate a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate  # For Unix/macOS
.venv\Scripts\activate     # For Windows

3. Install Dependencies

pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the project root with the following content:

DATABASE_URL=postgresql://<username>:<password>@localhost:5432/volga_db

5. Set Up PostgreSQL Database
Make sure your PostgreSQL database is running and create a database named volga_db. Run the table setup script:

python database/setup_db.py

6. Edit the Configuration File
Edit the config/config.yaml file with your desired settings:

fetch_interval_minutes: 3
api_url: "https://api.open-meteo.com/v1/forecast"
location: "Skolkovo"

7. Run the Main Application
Start the main application which will handle automatic data fetching and exporting:

python main.py
Type <export> to manually export data to an Excel file.
Type <quit> to stop the scheduler.

8. Manually Running Weather Data Fetching or Excel Export (if needed)
To manually fetch weather data or export to Excel:

python -m services.weather_fetcher    # Fetch weather data
python -m services.excel_exporter     # Export data to Excel

Project Structure:

main.py: Main entry point for running the scheduler and interacting with the app.
services/weather_fetcher.py: Handles fetching weather data from the API.
services/excel_exporter.py: Handles exporting data to an Excel file.
database/: Contains database setup and models.
config/config.yaml: Stores configuration settings like fetch interval and API URL.
.env: Stores sensitive environment variables (e.g., database credentials).

Technology Stack Summary:

Backend: FastAPI, SQLAlchemy, Requests
Database: PostgreSQL
Excel Handling: Openpyxl
Configuration: YAML, dotenv
Scheduling: asyncio, schedule
Environment: Virtual environment (.venv)

Additional Notes:

Ensure your PostgreSQL server is running before starting the application.
You can modify the fetch interval or API URL in config/config.yaml without changing the code.
