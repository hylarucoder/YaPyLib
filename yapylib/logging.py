import logging
from logging.config import dictConfig
import os

from yapylib.settings import USE_COLORS, DEBUG, LOGS_DIR

LOGGING = {  # dictConfig for output stream and file logging
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'console': {
            'format': '[%(asctime)s] %(levelname)s::%(module)s - %(message)s',
        },
        'file': {
            'format': '[%(asctime)s] %(levelname)s::(P:%(process)d T:%(thread)d)::%(module)s - %(message)s',
        },
    },

    'handlers': {
        'console': {
            'class': 'yapylib.misc.color_stream_handler.ColorStreamHandler',
            'formatter': 'console',
            'level': 'DEBUG',
            'use_colors': USE_COLORS,
        },
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'file',
            'level': 'INFO',
            'when': 'midnight',
            'filename': str(LOGS_DIR) + '/yapylib.log',
            'interval': 1,
            'backupCount': 0,
            'encoding': 'utf-8',
            'delay': False,
            'utc': False,
        },
    },

    'loggers': {
        'default': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
        'project': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
        'common': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
        'http': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
        'proxy': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        }
    }
}

dictConfig(LOGGING)

import logging


def get_logger(name="common"):
    """
    :param name:
    :return:
    """
    logger = logging.getLogger(name)
    return logger
