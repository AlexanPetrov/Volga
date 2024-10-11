import asyncio
import schedule
import time
import threading
import yaml
from services.weather_fetcher import fetch_weather_data
from services.excel_exporter import export_to_excel

with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

fetch_interval_minutes = config['fetch_interval_minutes']

async def scheduled_job():
    fetch_weather_data()

def run_scheduled_tasks():
    schedule.every(fetch_interval_minutes).minutes.do(asyncio.run, scheduled_job)

    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler():
    scheduler_thread = threading.Thread(target=run_scheduled_tasks)
    scheduler_thread.daemon = True
    scheduler_thread.start()

def main():
    start_scheduler()

    while True:
        user_input = input("Type 'export' to export data to Excel or 'quit' to stop the scheduler: ").strip().lower()
        if user_input == 'export':
            export_to_excel()
        elif user_input == 'quit':
            print("Stopping the scheduler.")
            break

if __name__ == "__main__":
    main()
