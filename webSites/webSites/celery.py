from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
from django.conf import settings  # noqa

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webSites.settings')

# app = Celery('tasks', broker='amqp://localhost//',
#              backend='db+postgresql://postgres:fectper8819@localhost/websites')

app = Celery('webSites',
             broker='amqp://localhost//',
             backend='db+postgresql://postgres:fectper8819@localhost/websites',
             include=['webSites.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
