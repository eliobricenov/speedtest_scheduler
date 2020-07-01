from crontab import CronTab

from src.logger import get_logger
from src.util import get_script_path

USER = 'elio'


def setup_jobs():
    logger = get_logger()

    with CronTab(user=USER) as cron:
        cron.remove_all()
        job_command = 'python3 {}/speedtest.py'.format(get_script_path())
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
