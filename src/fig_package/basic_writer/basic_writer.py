"""
BasicWriter Class
"""
from logging import Logger
import os

from ..common import get_default_logger, WriteFileAlreadyExists
from ..format.ynf import cYnf

class BasicWriter(object):
    """
    BasicWriterクラス。
    Ynf形式から何かのフォーマットへ変換する処理の基底クラス。
    """
    def __init__(self, file_path:str, overwrite:bool=False, logger:Logger=None):
        """
        コンストラクタ

        Parameters
        ----------
        file_path: str
            出力するファイルパス
        overwrite: bool
            既に存在する場合は上書きするオプション
        logger: Logger
            ロガー。指定されない場合は別途定義してあるデフォルトロガー。
        """
        # ロガーを設定
        self.logger = logger or get_default_logger()
        
        # 開始ログ
        msg = f'Start writing. ({self.__class__.__name__})'
        self.logger.info(msg)
        self.logger.info(f'file:{file_path}')

        # ファイルが既に存在している場合は、Overwriteオプションがついていないとダメ
        if os.path.exists(file_path):
            if not overwrite:
                raise WriteFileAlreadyExists(
                    'Write file is already exists. ' + \
                    'Consider using a option `overwrite=True`.'
                )
            
            # フォルダが存在している場合は、エラー
            if os.path.isdir(file_path):
                raise WriteFileAlreadyExists(
                    f'Directory is exists. ({file_path})'
                )

            # overwrite指定されている場合はここで消す
            os.remove(file_path)


    def write(self, ynf: cYnf):
        """
        コンストラクタで指定したファイルを出力する
        派生クラスでオーバーライドすること。

        Parameters
        ----------
        ynf: cYnf
            出力するcYnfファイル
        """
        raise NotImplementedError
    
