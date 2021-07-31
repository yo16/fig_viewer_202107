"""
cYnfTextのテスト
"""
import os
import sys
from unittest import TestCase

# srcの下をパスに追加
sys.path.append(os.path.join(os.getcwd(), 'src'))

from fig_package.format.ynf import cYnfText
from fig_package.common import IlligalParameterError
class TestCYnfText(TestCase):
    """
    cYnfTextのテスト
    """
    def test_1_create(self):
        """
        作成
        """
        t = cYnfText({
            'text': 'test_message',
            'pos': [10,20]
        })
    
    def test_2_create(self):
        """
        パラメータ詰め込んで作成
        """
        t = cYnfText({
            'text': 'test_message',
            'pos': [10,20],
            'text-align': 'left',
            'text-valign': 'top',
            'text-color': '#fff',
            'font-size': 10
        })

    def test_3_error(self):
        """
        必須パラメータ
        """
        try:
            t = cYnfText({
                'pos': [10,20]
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_4_error(self):
        """
        必須パラメータ
        """
        try:
            t = cYnfText({
                'text': 'test_message',
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_5_error(self):
        """
        必須パラメータ
        """
        try:
            t = cYnfText({
                'text': 'test_message',
                'pos': [10,20,30]
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_6_error(self):
        """
        必須パラメータ
        """
        try:
            t = cYnfText({
                'text': 'test_message',
                'pos': [10,]
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_7_error(self):
        """
        必須パラメータ
        """
        try:
            t = cYnfText({
                'text': 'test_message',
                'pos': [10]
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')
    
    def test_8_error(self):
        """
        必須パラメータ
        """
        try:
            t = cYnfText({
                'text': None,
                'pos': [10,20]
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_9_error(self):
        """
        任意パラメータ
        """
        try:
            t = cYnfText({
                'text': 'test message',
                'pos': [10,20],
                'text-align': 'middle', # 正しくは'center'
                'text-valign': 'top',
                'text-color': '#fff',
                'font-size': 10
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_10_error(self):
        """
        任意パラメータ
        """
        try:
            t = cYnfText({
                'text': 'test message',
                'pos': [10,20],
                'text-align': 'center',
                'text-valign': 'center', # 正しくはmiddle
                'text-color': '#fff',
                'font-size': 10
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_11_error(self):
        """
        任意パラメータ
        """
        try:
            t = cYnfText({
                'text': 'test message',
                'pos': [10,20],
                'text-align': 'center',
                'text-valign': 'middle',
                'text-color': '#fff',
                'font-size': '10'   # int or floatが必要
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')
