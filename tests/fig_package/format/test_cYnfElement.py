"""
cYnfElementのテスト
"""
import os
import sys
from unittest import TestCase

# srcの下をパスに追加
sys.path.append(os.path.join(os.getcwd(), 'src'))

from fig_package.format.ynf import cYnfElement
class TestCYnfElement(TestCase):
    """
    cYnfElementクラスのテスト
    """
    def test_1_create(self):
        """
        とりあえず作る
        """
        e = cYnfElement({})
        self.assertEqual(e.prop['display'], True, '属性の初期値チェック')
        self.assertEqual(e.prop['fill-color'], None, '属性の初期値チェック')
        self.assertEqual(e.prop['border-color'], None, '属性の初期値チェック')
        self.assertEqual(e.prop['border-width'], 1.0, '属性の初期値チェック')


    def test_2_any_params(self):
        """
        引数の属性
        """
        e = cYnfElement( \
            {'test1':'xyz', 'test2':False, \
             'test3':3.14, 'test4':40000})
        
        self.assertEqual(e.prop['test4'], 40000, '引数属性のチェック')
        self.assertEqual(e.prop['test3'], 3.14, '引数属性のチェック')
        self.assertEqual(e.prop['test2'], False, '引数属性のチェック')
        self.assertEqual(e.prop['test1'], 'xyz', '引数属性のチェック')


    def test_3_move(self):
        """
        move()。特に何もしない。エラーがない確認だけ。
        """
        e = cYnfElement({})
        e.move(100,200)


    def test_4_minmax(self):
        """
        get_min_max()のテスト
        """
        e = cYnfElement({})
        mm = e.get_minmax()
        self.assertEqual(len(mm), 2, "minmaxのサイズ")
        self.assertEqual(len(mm[0]), 2, "minmaxのサイズ")
        self.assertEqual(len(mm[1]), 2, "minmaxのサイズ")
        self.assertEqual(mm[0][0], 0, "mmの要素")
        self.assertEqual(mm[0][1], 0, "mmの要素")
        self.assertEqual(mm[1][0], 0, "mmの要素")
        self.assertEqual(mm[1][1], 0, "mmの要素")


    def test_5_isdisplay(self):
        """
        is_display()のテスト
        """
        e = cYnfElement({})
        
        self.assertEqual(e.is_display(), True, "is_display")



