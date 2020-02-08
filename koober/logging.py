import logging

__all__ = ('configure_logging',)


def configure_logging():
    logging.basicConfig(
        format='%(levelname)s | %(asctime)s | %(message)s',
        level=logging.DEBUG,
    )

    log = logging.getLogger()
    log.info('Logging is configured')
