""" BasicReader class
"""
import datetime
from logging import Logger
import os
import shutil

from ..common import get_default_logger, PROCESSED_FILE
from ..format.ynf import cYnf

class BasicReader(object):
    """
    BasicReaderクラス。
    何かのフォーマットからYnf形式へ変換する処理の基底クラス。
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

        # 開始ログ
        msg = f'Start reading. ({self.__class__.__name__})'
        self.logger.info(msg)
        self.logger.info(f'file:{file_path}')

        # ファイルの存在チェック
        if not os.path.exists(file_path):
            msg = f'File not found. ({file_path}) '
            self.logger.error(msg)
            raise FileNotFoundError(msg)

        # ファイルパスを覚えておく
        self.file_path = file_path

        # readerが格納する要素
        self.ynf = None


    def to_ynf(self) -> cYnf:
        """
        読み込んだファイルからYnfオブジェクトを生成して返す

        コンストラクタとして連動してやってもよいが、
        バラせるものはバラすという理由で関数化。
        (つまりこだわりはないので、コンストラクタでやりたくなったら
         変更しても問題なし。)
        """
        # 初期のYnf要素を生成
        basename = os.path.basename(self.file_path)
        basename_no_ext = os.path.splitext(basename)[0]
        self.ynf = cYnf(
            canvas_info={'title': basename_no_ext}, logger=self.logger)

        # Ynf形式へ変換(self.ynf)
        self.__to_ynf(self.file_path)

        return self.ynf
    

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
