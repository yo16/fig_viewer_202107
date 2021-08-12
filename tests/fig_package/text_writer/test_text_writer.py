"""
TextWriterクラスのテスト
"""
import os
import sys
from unittest import TestCase
import pickle

# srcの下をパスに追加
sys.path.append(os.path.join(os.getcwd(), 'src'))

from fig_package.text_writer import TextWriter
class TestTextWriter(TestCase):
    """
    TextWriterクラスのテスト
    """
    def setUp(self):
        """
        テスト前処理
        """
        self.del_file_list = []
        self.del_dir_list = []

        return
    
    
    def tearDown(self):
        """
        テスト後処理
        """
        # ファイル削除
        for f in self.del_file_list:
            os.remove(f)
        # フォルダ削除
        for d in self.del_dir_list:
            os.rmdir(d)
        
        return


    def test_1_no_file(self):
        """
        正常に出力
        """
        # 読むファイル
        ynf_file1 = \
            os.path.join( \
                os.path.dirname(__file__),  \
                '../../data/ynf/A3yoko.ynf')
        os.makedirs(
            os.path.abspath(os.path.join(ynf_file1, os.pardir)),
            exist_ok=True)
        # 書くファイル
        text_file1 = \
            os.path.join( \
                os.path.dirname(__file__),  \
                '../../data/tmp/test1.txt')
        os.makedirs(
            os.path.abspath(os.path.join(text_file1, os.pardir)),
            exist_ok=True)
        
        # 読んでデシリアライズ
        ynf = None
        with open(ynf_file1, 'rb') as f:
            ynf = pickle.load(f)

        w = TextWriter(file_path=text_file1, overwrite=True)
        w.write(ynf)
    

