from apscheduler.schedulers.background import BackgroundScheduler

def my_task():
    #定时任务逻辑
    print('定时任务执行成功！')


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(my_task, 'interval', seconds=10)  # 每 60 秒执行一次
    scheduler.start()