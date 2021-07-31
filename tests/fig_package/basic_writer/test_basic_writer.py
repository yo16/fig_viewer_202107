"""
BasicWriterクラスのテスト
"""
import os
import sys
from unittest import TestCase

# srcの下をパスに追加
sys.path.append(os.path.join(os.getcwd(), 'src'))

from fig_package.basic_writer import BasicWriter
from fig_package.common import WriteFileAlreadyExists
class TestBasicWriter(TestCase):
    """
    BasicWriterクラスのテスト
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
        指定したファイルが存在していない場合
        正常に動くはず
        """
        w = BasicWriter('./not_exists_file')
        self.assertEqual(
            w.__class__.__name__, 'BasicWriter',
            'インスタンスが正常に作れてない。(Noneとか)'
        )
    

    def test_2_file_exists(self):
        """
        指定したパスにファイルが存在する場合
        WriteFileAlreadyExistsが起こる
        """
        try:
            # ダミーファイルを作っておく
            tmp_file_path = \
                os.path.join( \
                    os.path.dirname(__file__),  \
                    '../../tmp/any_file2.txt')
            with open(tmp_file_path, 'w') as f:
                f.write('abc')
            # 後で消す
            self.del_file_list.append(tmp_file_path)

            w = BasicWriter(tmp_file_path)

            self.assertTrue(False, 'エラーが起こるはず')
        except WriteFileAlreadyExists as e:
            # 正常
            pass
        except:
            # 他のexceptionが出たらエラー
            self.assertTrue(False, '予期せぬエラー')
    

    def test_3_file_exists(self):
        """
        指定したパスにファイルが存在する場合
        overwrite=Falseだとエラー
        """
        try:
            # ダミーファイルを作っておく
            tmp_file_path = \
                os.path.join( \
                    os.path.dirname(__file__),  \
                    '../../tmp/any_file3.txt')
            with open(tmp_file_path, 'w') as f:
                f.write('abc')
            # 後で消す
            self.del_file_list.append(tmp_file_path)

            w = BasicWriter(tmp_file_path, overwrite=False)

            self.assertTrue(False, 'エラーが起こるはず')
        except WriteFileAlreadyExists as e:
            # 正常
            pass
        except:
            # 他のexceptionが出たらエラー
            self.assertTrue(False, '予期せぬエラー')
    

    def test_4_file_exists(self):
        """
        指定したパスにファイルが存在する場合
        overwrite=Trueだと正常
        """
        try:
            # ダミーファイルを作っておく
            tmp_file_path = \
                os.path.join( \
                    os.path.dirname(__file__),  \
                    '../../tmp/any_file4.txt')
            with open(tmp_file_path, 'w') as f:
                f.write('abc')

            w = BasicWriter(tmp_file_path, overwrite=True)
            # 正常に通るはず

            # overwrite指定によって、削除されているはず
            self.assertFalse(
                os.path.exists(tmp_file_path),
                '削除されるはずのファイルが削除されてない')
        except:
            # 他のexceptionが出たらエラー
            self.assertTrue(False, '予期せぬエラー')


    def test_5_file_exists(self):
        """
        指定したパスにフォルダが存在する場合
        例外が出るはず
        """
        try:
            # ダミーファイルを作っておく
            tmp_dir_path = \
                os.path.join( \
                    os.path.dirname(__file__),  \
                    '../../tmp/any_dir5')
            os.makedirs(tmp_dir_path, exist_ok=True)
            self.del_dir_list.append(tmp_dir_path)

            w = BasicWriter(tmp_dir_path, overwrite=True)

            raise Exception('例外が起こらないとダメ')
        
        except WriteFileAlreadyExists as e:
            # 存在しているフォルダが指定された場合に出る例外でOK
            pass

        except:
            # 他のexceptionが出たらエラー
            self.assertTrue(False, '予期せぬエラー')


    def test_6_from_ynf_file(self):
        """
        Ynfファイルを使って読むテスト
        """
        ynf_file1 = \
            os.path.join( \
                os.path.dirname(__file__),  \
                '../../data/ynf/A3yoko.ynf')
        
        try:
            w = BasicWriter('./not_exists_file')
            w.write_from_ynf_file(ynf_file1)
            self.assertTrue(False, 'ここまで進まないはず')
        except NotImplementedError as e:
            # write()までは進んでるということだけ確認できればいいか
            pass
        except:
            self.assertTrue(False, '何かのエラー')
