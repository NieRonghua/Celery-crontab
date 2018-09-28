# -*- coding: UTF-8 -*-
from celery_task.celery import app


def test33():
    print('test33-------------------')


def test44():
    print('test44-------------------')
    test33()


@app.task
def celery_run():
    test33()
    test44()


if __name__ == '__main__':
    celery_run()