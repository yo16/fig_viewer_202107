"""
cYnfLine, cYnfPolyline, cYnfBoxのテスト
"""
import os
import sys
from unittest import TestCase

# srcの下をパスに追加
sys.path.append(os.path.join(os.getcwd(), 'src'))

from fig_package.format.ynf import cYnfLine, cYnfPolyline, cYnfBox
from fig_package.common import IlligalParameterError
class TestCYnfLine(TestCase):
    """
    cYnfLineのテスト
    """
    def test_1_create(self):
        """
        作成
        """
        _ = cYnfLine({
            'p1': [10,20],
            'p2': [30,40]
        })
    
    def test_2_create_with_option(self):
        """
        オプション付きで作成
        """
        _ = cYnfLine({
            'p1': [10,20],
            'p2': [30,40],
            'border-color': '#f00',
            'border-width': 2,
            'unknown': True     # 知らないのがあってもOK
        })
    
    def test_3_option_error1(self):
        """
        p1が不正
        """
        try:
            _ = cYnfLine({
                'p1': [10,20,30],
                'p2': [30,40]
            })
            # raiseされない場合はチェックNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # OK
            pass
        else: 
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')
    
    def test_4_option_error2(self):
        """
        p1が不正
        """
        try:
            _ = cYnfLine({
                'p1': [10,],
                'p2': [30,40]
            })
            # raiseされない場合はチェックNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # OK
            pass
        else: 
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_5_option_error3(self):
        """
        p1が不正
        """
        try:
            _ = cYnfLine({
                'p1': 10,
                'p2': [30,40]
            })
            # raiseされない場合はチェックNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # OK
            pass
        else: 
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_6_option_error4(self):
        """
        p1が不正
        """
        try:
            _ = cYnfLine({
                'p2': [30,40]
            })
            # raiseされない場合はチェックNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # OK
            pass
        else: 
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_7_option_error5(self):
        """
        p2が不正
        """
        try:
            _ = cYnfLine({
                'p1': [10,20],
                'p2': [30,40,50]
            })
            # raiseされない場合はチェックNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # OK
            pass
        else: 
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_8_option_error6(self):
        """
        p2が不正
        """
        try:
            _ = cYnfLine({
                'p1': [10,20],
                'p2': [30]
            })
            # raiseされない場合はチェックNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # OK
            pass
        else: 
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_9_option_error7(self):
        """
        p2が不正
        """
        try:
            _ = cYnfLine({
                'p1': [10,20]
            })
            # raiseされない場合はチェックNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # OK
            pass
        else: 
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')




