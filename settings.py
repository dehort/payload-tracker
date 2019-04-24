import os

ENVIRONMENT = os.environ.get('TRACKER_ENV', 'dev')
DEBUG = ENVIRONMENT in ('dev', 'ci', 'qa')

# Logging settings
DEV_LOG_LEVEL = 'INFO'
DEV_LOG_MSG_FORMAT = "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] " \
            "[%(thread)d  %(threadName)s] [%(process)d] %(message)s"
DEV_LOG_DATE_FORMAT = "%H:%M:%S"
APP_NAME = "payload-tracker-service"
