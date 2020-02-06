import asyncio
import logging

logging.basicConfig(
    format='%(levelname)s | %(asctime)s | %(message)s',
    level=logging.DEBUG,
)
log = logging.getLogger()


def main():
    log.info('Application started')

if __name__ == '__main__':
    main()

