from job import setup_jobs, list_jobs, clean_jobs
from speedtest import run_test
from db import SpeedtestService


def main():
    # setup_jobs()
    # list_jobs()
    # clean_jobs()
    speedtest = SpeedtestService()
    speedtest.create(result=3)
    print(speedtest.all())


if __name__ == '__main__':
    main()
