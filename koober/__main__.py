import logging

from koober.logging import configure_logging

log = logging.getLogger(__name__)


def main():
    configure_logging()
    log.info('Application started')


if __name__ == '__main__':
    main()

