from apscheduler.schedulers.background import BackgroundScheduler

# Define a function to perform the scheduled task
def my_task():
    print("Task executed at the scheduled time")

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.start()

    # Example: Schedule a task to run at a specific time (e.g., 2:30 PM every day)
    scheduler.add_job(my_task, 'cron', hour=14, minute=48, id='specific_time_task')

    # Example: Schedule a task to run at regular intervals (e.g., every 30 seconds)
    scheduler.add_job(my_task, 'interval', seconds=30, id='interval_task')

    try:
        input()
    except (KeyboardInterrupt, SystemExit):
        pass

    scheduler.shutdown()
