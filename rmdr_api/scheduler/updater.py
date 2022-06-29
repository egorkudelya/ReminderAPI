from apscheduler.schedulers.background import BackgroundScheduler
from ..views import NotificationViewset


def start():
    scheduler = BackgroundScheduler()
    notification = NotificationViewset()
    scheduler.add_job(notification.save_user_log, 'interval', minutes=5, id='rmd1', replace_existing=True)
    scheduler.start()
