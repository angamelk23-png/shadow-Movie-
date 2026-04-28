from apscheduler.schedulers.asyncio import AsyncIOScheduler
scheduler=AsyncIOScheduler()

def start_jobs():
 scheduler.start()
