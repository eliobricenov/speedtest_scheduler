import fastdotcom
import traceback
import os

from .logger import get_logger
from .speedtest_service import SpeedtestService

EXPECTED_SPEED_MB = 2
MAX_TRIES_NUMBER = 3


def main():
    logger = get_logger()
    result_service = SpeedtestService()
    result = {}
    logger.info('STARTING SPEED TEST IN PID: {}'.format(os.getpid()))

    try:
        result = run_test()
    except SystemError:
        error = traceback.print_exc()
        print('ERROR: {}', error)
        logger.error(error)
    finally:
        result_service.create(result)

    logger.info('TEST RESULT: {}'.format(result))


def run_test():
    print('Running test ...')
    num_tries = 0
    test_result = fastdotcom.fast_com()

    while test_result == 0 and num_tries < MAX_TRIES_NUMBER:
        num_tries += 1
        test_result = fastdotcom.fast_com()

    print('Test result: {} MB'.format(test_result))
    return test_result


if __name__ == '__main__':
    main()
