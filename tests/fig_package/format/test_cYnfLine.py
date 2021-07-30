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

    def test_10_minmax(self):
        """
        min/max
        """
        c = cYnfLine({
            'p1': [10,30],
            'p2': [40,20]
        })
        mm = c.get_minmax()
        self.assertEqual(
            mm[0][0], 10,
            'Minがおかしい'
        )
        self.assertEqual(
            mm[0][1], 20,
            'Minがおかしい'
        )
        self.assertEqual(
            mm[1][0], 40,
            'Maxがおかしい'
        )
        self.assertEqual(
            mm[1][1], 30,
            'Maxがおかしい'
        )
        

class TestCYnfPolyline(TestCase):
    """
    cYnfPolyLineのテスト
    """
    def test_1_create(self):
        """
        作成
        """
        _ = cYnfPolyline({
            'points': [[10,20],[30,40],[50,60]]
        })

    def test_2_illigal_parameter(self):
        """
        error
        """
        try:
            _ = cYnfPolyline({
                'points': 10
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_3_illigal_parameter(self):
        """
        error
        """
        try:
            _ = cYnfPolyline({
                'points': 'a'
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_4_illigal_parameter(self):
        """
        error
        """
        try:
            _ = cYnfPolyline({
                'points': [10,20]
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_5_illigal_parameter(self):
        """
        error
        """
        try:
            _ = cYnfPolyline({
                'points': [[10,20],[30,40],[10,]]
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_6_minmax(self):
        """
        min/max
        """
        # ★
        p = cYnfPolyline({
            'points':[
                [50,110],
                [10,10],
                [100,70],
                [0,70],
                [90,10],
            ]
        })
        mm = p.get_minmax()
        self.assertEqual(
            mm[0][0],
            0,
            'minが不正'
        )
        self.assertEqual(
            mm[0][1],
            10,
            'minが不正'
        )
        self.assertEqual(
            mm[1][0],
            100,
            'maxが不正'
        )
        self.assertEqual(
            mm[1][1],
            110,
            'maxが不正'
        )


class TestCYnfBox(TestCase):
    """
    cYnfBoxのテスト
    """
    def test_1_create(self):
        """
        作成
        """
        _ = cYnfBox({
            'p1': [10,20],
            'p2': [30,40]
        })

    def test_2_error(self):
        """
        エラー
        """
        try:
            _ = cYnfBox({
                'p1': [10,20,25],
                'p2': [30,40]
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_3_error(self):
        """
        エラー
        """
        try:
            _ = cYnfBox({
                'p1': [10,],
                'p2': [30,40]
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
        エラー
        """
        try:
            _ = cYnfBox({
                'p1': [10,20],
                'p2': [30,40,50]
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
        エラー
        """
        try:
            _ = cYnfBox({
                'p1': [10,20],
                'p2': [30,]
            })
            # raiseされていない場合はNG
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            # ok
            pass
        else:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_6_minmax(self):
        """
        min/max
        """
        b = cYnfBox({
            'p1': [10,50],
            'p2': [30,20]
        })
        mm = b.get_minmax()
        self.assertEqual(
            mm[0][0],
            10,
            'minが不正'
        )
        self.assertEqual(
            mm[0][1],
            20,
            'minが不正'
        )
        self.assertEqual(
            mm[1][0],
            30,
            'maxが不正'
        )
        self.assertEqual(
            mm[1][1],
            50,
            'maxが不正'
        )

