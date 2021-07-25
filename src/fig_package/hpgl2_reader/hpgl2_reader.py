
from logging import Logger

from ..basic_reader import BasicReader

class Hpgl2Reader(BasicReader):
    """
    HPGL2Reader クラス
    HPGL2を読む。
    """
    def __init__(self, file_path:str, logger:Logger=None):
        """
        コンストラクタ

        Parameters
        ----------
        file_path: str
            読み込むファイルのパス。
        logger: Logger
            ロガー。指定されない場合は別途定義してあるデフォルトロガー。
        """
        super().__init__(file_path=file_path, logger=logger)


    def __to_ynf(self, file_path:str) -> None:
        """
        YNF形式へ変換する。
        Private method.
        変換した結果を、self.ynf へ格納する。
        BasicReaderクラスを継承したクラスは、主にこの関数を実装する。

        Parameters
        ----------
        file_path: str
            読み込むファイルのパス。
            存在しない場合は FileNotFoundError をraiseする。
        """

        return None