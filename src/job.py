import getpass
from crontab import CronTab
from .logger import get_logger
from .util import get_script_path

USER = getpass.getuser()


def setup_jobs():
    logger = get_logger()
    with CronTab(user=USER) as cron:
        cron.remove_all()
        job_command = 'cd {}/../ && python -m src.speedtest'.format(get_script_path(__file__))
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
