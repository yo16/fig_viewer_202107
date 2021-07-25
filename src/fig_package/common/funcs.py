""" 共通関数
"""

from logging import getLogger, StreamHandler, DEBUG
def get_default_logger(initial_talk:bool=False):
    """
    デフォルトロガーを返す

    Parameters
    ----------
    initial_talk: bool
        デフォルトロガーを使用したことをログ出力するか否か。
    """
    logger = getLogger(__name__)
    handler = StreamHandler()
    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    logger.propagate = False

    if initial_talk:
        logger.debug('Using default logger.')

    return logger

