""" BasicReader class
"""
import datetime
from logging import Logger
import os
import shutil

from ..common import get_default_logger, PROCESSED_FILE

class BasicReader(object):
    """
    BasicReaderクラス。
    ファイルを読み込むクラスはこのクラスを継承し、
    コンストラクタで super().__init__(logger) を呼ぶこと。
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
        # ロガーを設定
        self.logger = logger or get_default_logger()

        # ファイルパスを覚えておく
        self.file_path = file_path

        # Ynf形式へ変換
        self.__to_ynf(file_path)
    

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
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'入力ファイル "{file_path}" がありません！')
        
        return


    def save_original_data(self) -> str:
        """
        入力ファイルをそのままの形式で保存する。
        自身で持つ、file_path(存在してるはず)をそのまま使う。
        保存先は、PROCESSED_FILE の下に日付を切って入れる。

        Parameters
        ----------
        None

        Returns
        -------
        str
            保存したファイルパス
        """
        # ベースのフォルダ
        # カレントディレクトリの下にPROCESSED_FILEフォルダを作る
        base_dir_path = os.path.join(os.getcwd(), PROCESSED_FILE)

        # 年/月/日のフォルダを作る
        dt_now = datetime.datetime.now()
        today_dir_path = \
            os.path.join(
                base_dir_path, 
                f'{dt_now.year}/{dt_now.month:02}/{dt_now.day:02}')
        os.makedirs(today_dir_path, exist_ok=True)

        # ファイル名を決める
        copied_file_name = \
              f'{dt_now.year}{dt_now.month:02}{dt_now.day:02}_' \
            + f'{dt_now.hour:02}{dt_now.minute:02}{dt_now.second:02}_' \
            + f'{os.path.basename(self.file_path)}'
        copied_file_path = os.path.join(today_dir_path, copied_file_name)

        # ファイルコピー
        shutil.copy(self.file_path, copied_file_path)

        return copied_file_path
