# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from celery import Celery
from celery_task import celeryconfig

app = Celery('celery_demo')

app.config_from_object(celeryconfig)