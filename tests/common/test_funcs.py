"""
fig_package/common/funcs.pyのテスト
"""
import os
import sys
from logging import Logger

# srcの下をパスに追加
sys.path.append(os.path.join(os.getcwd(), 'src'))

from fig_package.common import get_default_logger
def test_get_default_logger1():
    """
    ロガーが返ってくるか（デフォルト引数）
    """
    lgr = get_default_logger()

    # Loggerの継承インスタンスが返ってくればいいか
    assert isinstance(lgr, Logger), 'Loggerでないものが返ってきてます'


def test_get_default_logger2():
    """
    ロガーが返ってくるか（True）
    """
    lgr = get_default_logger(True)

    # Loggerの継承インスタンスが返ってくればいいか
    assert isinstance(lgr, Logger), 'Loggerでないものが返ってきてます'


def test_get_default_logger3():
    """
    ロガーが返ってくるか（False）
    """
    lgr = get_default_logger(False)

    # Loggerの継承インスタンスが返ってくればいいか
    assert isinstance(lgr, Logger), 'Loggerでないものが返ってきてます'
