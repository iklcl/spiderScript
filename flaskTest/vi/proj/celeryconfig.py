#BROKER_URL = 'redis://192.168.201.91/0'
BROKER_URL = 'amqp://careland:careland@192.168.201.91/'
CELERY_RESULT_BACKEND = 'redis://192.168.201.91/1'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_ACCEPT_CONTENT = ['json']


