"""
cYnfクラスのテスト
"""
import os
import sys
from unittest import TestCase

# srcの下をパスに追加
sys.path.append(os.path.join(os.getcwd(), 'src'))

from fig_package.format.ynf import cYnf, cYnfLine
class TestCYnf(TestCase):
    """
    cYnfクラスのテスト
    """
    def setUp(self):
        """
        テスト前処理
        """
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
    
    
    def test_1_default_create(self):
        """
        空で作るだけ
        """
        ynf = cYnf({})

        # 一応インスタンス確認
        self.assertTrue(isinstance(ynf, cYnf))


    def test_2_append(self):
        """
        要素を追加する
        """
        y = cYnf({})

        # 要素
        ye = cYnfLine({'p1':[0,0], 'p2':(10,20)})

        # 追加
        y.append(ye)

        # 単体テストでは確認しようがない・・・


    def test_3_serialize(self):
        """
        シリアライズ
        """
        # 保存先
        out_file = 'test_sirialyze_test3.pkl'

        # cYnf
        y = cYnf({})

        # 要素
        ye = cYnfLine({'p1':[0,0], 'p2':(10,20)})

        # 追加
        y.append(ye)

        # シリアライズ
        y.serialize(out_file)


    def test_4_deserialize(self):
        """
        デシリアライズ
        """
        # 保存先
        out_file = 'test_sirialyze_test4.pkl'

        # cYnf
        y = cYnf({})

        # 要素
        ye = cYnfLine({'p1':[0,0], 'p2':(10,20)})

        # 追加
        y.append(ye)

        # シリアライズ
        y.serialize(out_file)

        # デシリアライズ
        y2 = cYnf.deserialize(out_file)
        #print(y2.to_str())

