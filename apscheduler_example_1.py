from apscheduler.schedulers.blocking import BlockingScheduler

def some_job():
    print "Hello World"

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', seconds=1)
scheduler.start()
