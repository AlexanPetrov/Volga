import asyncio
import schedule
import time
import threading
from services.weather_fetcher import fetch_weather_data
from services.excel_exporter import export_to_excel

async def scheduled_job():
    fetch_weather_data()

def run_scheduled_tasks():
    schedule.every(3).minutes.do(asyncio.run, scheduled_job)

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
