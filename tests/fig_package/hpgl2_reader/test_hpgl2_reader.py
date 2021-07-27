"""
Hpgl2Readerクラスのテスト
"""
import os
import sys
from unittest import TestCase

# srcの下をパスに追加
sys.path.append(os.path.join(os.getcwd(), 'src'))

from fig_package.hpgl2_reader import Hpgl2Reader
class TestHpgl2Reader(TestCase):
    """
    Hpgl2Readerクラスのテスト
    """
    def setUp(self):
        """
        テスト前処理
        """
        # 存在する正しいHPGL2ファイル
        self.exist_file1 = \
            os.path.join( \
                os.path.dirname(__file__),  \
                '../../data/hpgl2/A3yoko.dat')
        
        self.del_file_list = []

        return


    def tearDown(self):
        """
        テスト後処理
        """
        # ファイル削除
        for f in self.del_file_list:
            os.remove(f)
        
        return
    

    def test_1_file_exists(self):
        """
        とりあえず読むだけ
        """
        _ = Hpgl2Reader(self.exist_file1)
    

    def test_2_to_ynf(self):
        """
        Ynf化
        """
        rdr = Hpgl2Reader(self.exist_file1)
        _ = rdr.to_ynf()
        

