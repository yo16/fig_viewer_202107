"""
TextWriter Class
"""

from logging import Logger

from ..basic_writer import BasicWriter

class TextWriter(BasicWriter):
    """
    TextWriterクラス
    Ynf形式を文字列にする。
    主にデバッグ用。
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
        super(__class__,self).__init__(file_path, overwrite, logger)


    def write(self, ynf):
        """
        ファイル出力
        """
        with open(self.file_path, mode="w", encoding="utf-8") as f:
            self.__write_top_properties(ynf, f)
            
            if 'elements' in ynf.__dict__.keys():
                for i, e in enumerate(ynf.elements):
                    self.__write_element_properties(i, e, f)
    

    def __write_top_properties(self, ynf, hndl):
        """
        Ynf全体のプロパティを出力する
        """
        hndl.write('--- top properties ---\n')
        for k, v in ynf.__dict__.items():
            hndl.write(f'[{k}]={v}\n')

        return


    def __write_element_troperits(self, index, elm, hndl):
        """
        elements属性のプロパティを出力する
        """
        hndl.write(f'--- element ({index}) ---\n')
        for k, v in elm.__dict__.items():
            hndl.write(f'[{k}]={v}\n')

        return

