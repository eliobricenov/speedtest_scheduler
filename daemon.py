import os


def main():
    print('Daemon started with PID: {}'.format(os.getpid()))


if __name__ == '__main__':
    main()