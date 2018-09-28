启动命令：celery -A celery_task.celery -l info -B
其中： celery_task.celery为celery实例的路径，依实际项目而定

文件结构：
        ├── celerybeat-schedule
        ├── celery_task
        │   ├── celeryconfig.py
        │   ├── celeryconfig.pyc
        │   ├── celery.py
        │   ├── celery.pyc
        │   ├── __init__.py
        │   ├── __init__.pyc
        │   └── tasks
        │       ├── __init__.py
        │       ├── __init__.pyc
        │       ├── task1.py
        │       ├── task1.pyc
        │       ├── task2.py
        │       └── task2.pyc
        └── readme.txt

定时任务中对于时间的控制，crontab只能精确到分钟，不能精确到秒