""" 共通関数
"""
import datetime
from logging import Logger, getLogger, StreamHandler, handlers, Formatter, \
    INFO
import os

from .const import LOGGER_DIR, LOG_LEVEL

def get_default_logger(initial_talk:bool=False) -> Logger:
    """
    デフォルトロガーを返す

    Parameters
    ----------
    initial_talk: bool
        デフォルトロガーを使用したことをログ出力するか否か。
    """
    logger = getLogger(__name__)
    # RotatingFileHandler版ロガー
    __set_logger_RotatingFileHander(logger)

    if initial_talk:
        logger.debug('Using default logger.')
        logger.debug(f'Log level is {logger.level}.')
    
    return logger


def __set_logger_StreamHandler(logger: Logger) -> None:
    """
    StreamHandler版ロガー
    """
    logger = getLogger(__name__)
    handler = StreamHandler()
    handler.setLevel(LOG_LEVEL)
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(handler)
    logger.propagate = False
    

def __set_logger_RotatingFileHander(logger: Logger) -> None:
    """
    RotatingFileHandler版ロガー
    """
    dt_now = datetime.datetime.now()
    str_now = dt_now.strftime('%Y%m%d_%H%M%S')
    str_log_dir = dt_now.strftime(f'{LOGGER_DIR}/%Y/%Y%m')
    os.makedirs(str_log_dir, exist_ok=True)
    handler = handlers.RotatingFileHandler(
        f'{str_log_dir}/{str_now}.log', 'a+',
        maxBytes=10000, backupCount=5
    )
    handler.setLevel(LOG_LEVEL)
    handler.setFormatter(Formatter('[%(asctime)s] %(levelname)s: %(message)s'))
    logger.addHandler(handler)
    logger.setLevel(LOG_LEVEL)

