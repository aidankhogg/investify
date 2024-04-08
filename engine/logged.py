"""
This module handles all logging functionality.
"""
from loguru import logger as log

import os.path
from loguru import logger
from sys import stderr, stdout

from engine.configured import local_paths


logger.remove()

# Define panic levels
TRACE = 5
DEBUG = 10
INFO = 20
NOTICE = 25
WARNING = 30
ERROR = 40
CRITICAL = 50
PANIC = 80


# settings = engine_settings.logging
# global_lvl = settings.level


def load_config_file(path_to_config):
    # Function to load the YAML config file and return a dictionary
    pass


def setup_logging(config):
    # Initialize the Loguru logging system with config settings
    pass


def configure_handlers(handlers_config):
    # Configure log handlers based on the settings
    pass


def configure_formatters(formatters_config):
    # Configure log formatters based on the settings
    pass


def set_logger_levels(logger_level):
    # Set logger levels (e.g., TRACE, DEBUG, INFO, etc.)
    pass


def handle_file_rotation(file_handler_config):
    # Implement file rotation and retention settings
    pass


def customize_log_settings():
    # Add custom log settings as per the formatter configurations
    pass


"""
Initial stuff
"""


def load_all_from_settings():
    # Create handlers
    for handler in settings.handlers:
        if handler['sink'].startswith('ext://'):
            pass
        else:
            # print(f"Adding sink: {handler['sink']}")
            logger.add(
                str(os.path.join(log_dir, handler['sink'])),
                format=getattr(handler, 'format', settings.formatters.complete),
                level=getattr(handler, 'level', settings.level),
                rotation=getattr(handler, 'rotation', '90 days'),
                retention=getattr(handler, 'retention', '6 months'),
                buffering=getattr(handler, 'buffering', 1)
            )


def setup_console_logging(start_fresh=True):
    if start_fresh:
        logger.remove()

    def stdout_filter(record):
        return record["level"].no <= INFO

    def stderr_filter(record):
        return record["level"].no > INFO

    # Informational log messages
    logger.add(
        stdout,
        format=settings.formatters.cleaner,
        colorize=True,
        backtrace=True,
        diagnose=True,
        level=global_lvl,
        filter=stdout_filter
    )

    # Exception log messages
    logger.add(
        stderr,
        format=settings.formatters.cleaner,
        colorize=True,
        backtrace=True,
        diagnose=True,
        level=global_lvl,
        filter=stderr_filter
    )

    logger.trace("Console logging enabled")


def setup_debug_logging():
    pass


def get_logger(name='system'):
    try:
        if name == 'system':
            return 'system'
        elif not isinstance(name, str):
            raise TypeError(f"Logger name is '{type(name).__class__.__name__}' is not a 'str'.")
        else:
            raise ValueError(f"Logger name is '{name}' is not in pre-configured loggers.")
    except (TypeError, ValueError) as e:
        raise NotImplementedError(f"Could not start logger.")


if __name__ == '__main__':
    logger.remove()
    setup_console_logging()
    load_all_from_settings()
    logger.trace("Starting logger tests")
    logger.trace("This is an example trace message")
    logger.debug("This is an example debug message")
    logger.info("This is an example info message")
    logger.warning("This is an example warning message")
    logger.error("This is an example error message")
    logger.critical("This is an example critical message")
    # get_logger('boo')
