import os
from crontab import CronTab
from dotenv import load_dotenv
from .logger import get_logger
from .util import get_script_path

load_dotenv()
USER = os.getenv('JOB_USER')


def setup_jobs():
    logger = get_logger()

    with CronTab(user=USER) as cron:
        cron.remove_all()
        job_command = 'cd {}/../ && $(which python3) -m src.speedtest'.format(get_script_path(__file__))
        print('The job command will be \'{}\''.format(job_command))
        job = cron.new(command=job_command)
        job.minutes.every(1)
        cron.write()
    logger.info('CRON JOBS CREATED')
    print('CRON JOBS CREATED')


def list_jobs():
    cron = CronTab(user=USER)
    for job in cron:
        print(job)


def clean_jobs():
    cron = CronTab(user=USER)
    cron.remove_all()
