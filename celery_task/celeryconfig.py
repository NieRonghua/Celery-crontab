# -*- coding: UTF-8 -*-

from __future__ import absolute_import  # 拒绝隐式导入，避免同名包冲突
from celery.schedules import crontab

broker_url = 'redis://localhost:6379/1'
result_backend = 'redis://localhost:6379/2'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = "Asia/Shanghai"  # 时区设置
worker_hijack_root_logger = True  # 关闭日志
# result_expires = 60 * 60 * 24  # 存储结果过期时间（默认1天）

# 导入任务所在文件
imports = [
    'celery_task.tasks.task1',
    'celery_task.tasks.task2'
]

# 需要执行任务的配置
beat_schedule = {
    'task1': {
        'task': 'celery_task.tasks.task1.celery_run',  # 要执行的函数
        'schedule': 10.0,  # 每10秒
        # 'schedule': crontab(minute='*/5'),  # 每5分钟执行，crontab只能精确到分钟
        'args': ''  # 任务函数所需参数
    },
    'task2': {
        'task': 'celery_task.tasks.task2.celery_run',  # 要执行的函数
        'schedule': 5.0,  # 每5秒
        # 'schedule': crontab(minute='*/3'),  # 每3分钟执行
        'args': ''  # 任务函数所需参数
    },
}
