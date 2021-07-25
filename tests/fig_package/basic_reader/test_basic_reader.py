"""
BasicReaderモジュールのテスト
"""
import os
import sys
from unittest import TestCase

# srcの下をパスに追加
sys.path.append(os.path.join(os.getcwd(), 'src'))

from fig_package.basic_reader import BasicReader
class TestBasicReader(TestCase):
    def setUp(self):
        """
        テスト前処理
        """
        self.del_file_list = []
    
    def tearDown(self):
        """
        テスト後処理
        """
        # ファイル削除
        for f in self.del_file_list:
            os.remove(f)
        return
    

    """
    BasicReaderクラスのテスト
    """
    def test_1_not_found(self):
        """
        ファイル存在チェック。
        存在していなかったらFileExistsErrorが出る。
        """
        try:
            file_path_not_exist = './not_exist.txt'
            r = BasicReader(file_path_not_exist)

            # Exceptionが出なかったら失敗
            assert False

        except FileNotFoundError:
            # Exceptionが出たらOK
            assert True


    def test_2_file_copy(self):
        """
        ファイルのコピーをすることのテスト。
        """
        file_path = \
            os.path.join( \
                os.path.dirname(__file__),  \
                '../../data/hpgl2/A3yoko.dat')
        r = BasicReader(file_path)
        copied_path = r.save_original_data()

        assert os.path.exists(copied_path), \
            f'コピーされたファイル"{copied_path}"がない'
        
        # 消すファイルに登録しておく
        self.del_file_list.append(copied_path)
    



