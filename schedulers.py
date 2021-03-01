from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from config import settings
import pytz

jobstores = {'default': SQLAlchemyJobStore(url=settings.SQLALCHEMY_DATABASE_URL)}
executors = {'default': ThreadPoolExecutor(20), 'processpool': ProcessPoolExecutor(5)}
job_defaults = {'coalesce': False, 'max_instances': 3}

scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=pytz.utc, misfire_grace_time=settings.MISFIRE_GRACE_TIME)