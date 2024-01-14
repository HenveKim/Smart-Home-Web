from django.apps import AppConfig
from tasks.tasks import start_scheduler

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    def ready(self):
        # 在应用启动时启动任务调度器
        start_scheduler()