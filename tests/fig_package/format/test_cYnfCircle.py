"""
cYnfCircle, cYnfArcのテスト
"""
import os
import sys
from unittest import TestCase

# srcの下をパスに追加
sys.path.append(os.path.join(os.getcwd(), 'src'))

from fig_package.format.ynf import cYnfCircle, cYnfArc
from fig_package.common import IlligalParameterError
class TestCYnfCircle(TestCase):
    """
    cYnfCircleのテスト
    """
    def test_1_create(self):
        """
        作成
        """
        c = cYnfCircle({
            'center': [10,20],
            'r': 5
        })
    
    def test_2_not_enough_parameter1(self):
        """
        不十分なパラメータ1
        """
        try:
            c = cYnfCircle({
                'r': 5
            })
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            pass
        except:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_3_not_enough_parameter2(self):
        """
        不十分なパラメータ2
        """
        try:
            c = cYnfCircle({
                'center': [10],
                'r': 5
            })
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            pass
        except:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_4_not_enough_parameter3(self):
        """
        不十分なパラメータ3
        """
        try:
            c = cYnfCircle({
                'center': [10,20]
            })
            self.assertTrue(False, 'エラーが起こるはず')
        except IlligalParameterError as e:
            pass
        except:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_5_minmax(self):
        """
        min/maxの計算
        """
        center_pos = [100,200]
        r = 5
        c = cYnfCircle({
            'center': center_pos,
            'r': r
        })
        mm = c.get_minmax()
        self.assertEqual(len(mm), 2, "min/maxの戻り値不正")
        self.assertEqual(len(mm[0]), 2, "min/maxの戻り値不正")
        self.assertEqual(len(mm[1]), 2, "min/maxの戻り値不正")
        self.assertEqual(mm[0][0], center_pos[0]-r,
            "min/maxの戻り値不正")
        self.assertEqual(mm[0][1], center_pos[1]-r,
            "min/maxの戻り値不正")
        self.assertEqual(mm[1][0], center_pos[0]+r,
            "min/maxの戻り値不正")
        self.assertEqual(mm[1][1], center_pos[1]+r,
            "min/maxの戻り値不正")


class TestCYnfArc(TestCase):
    """
    cYnfArcのテスト
    """
    def test_1_create(self):
        """
        普通に作成
        """
        a = cYnfArc({
            'start': [100,200],
            'end': [150, 200],
            'center': [125, 200],
            'r': 25,
            'clockwise': True
        })

    def test_2_error1(self):
        """
        rを指定していない
        （本当はいらないけど、Exceptionにしてる）
        """
        try:
            a = cYnfArc({
                'start': [100,200],
                'end': [150, 200],
                'center': [125, 200],
                'clockwise': True
            })
            self.assertTrue(False, "Exceptionが出るはず")
        except IlligalParameterError as e:
            pass
        except:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_3_error2(self):
        """
        centerを指定していない
        （本当はいらないけど、Exceptionにしてる）
        """
        try:
            a = cYnfArc({
                'start': [100,200],
                'end': [150, 200],
                'r': 25,
                'clockwise': True
            })
            self.assertTrue(False, "Exceptionが出るはず")
        except IlligalParameterError as e:
            pass
        except:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')

    def test_4_error3(self):
        """
        clockwiseを指定していない
        """
        try:
            a = cYnfArc({
                'start': [100,200],
                'end': [150, 200],
                'center': [125, 200],
                'r': 25
            })
            self.assertTrue(False, "Exceptionが出るはず")
        except IlligalParameterError as e:
            pass
        except:
            # 別の何かがraiseされたらNG
            self.assertTrue(False, 'IlligalParameterErrorが起こるはず')


    def test_5_minmax(self):
        """
        min/maxの計算
        """
        center_pos = [100,200]
        r = 5
        start_pos = [center_pos[0]-r, center_pos[1]]
        end_pos = [center_pos[0]+r, center_pos[1]]
        a = cYnfArc({
            'start': start_pos,
            'end': end_pos,
            'center': center_pos,
            'r': r,
            'clockwise': True
        })
        mm = a.get_minmax()
        self.assertEqual(len(mm), 2, "min/maxの戻り値不正")
        self.assertEqual(len(mm[0]), 2, "min/maxの戻り値不正")
        self.assertEqual(len(mm[1]), 2, "min/maxの戻り値不正")
        self.assertEqual(mm[0][0], center_pos[0]-r,
            "min/maxの戻り値不正")
        self.assertEqual(mm[0][1], center_pos[1]-r,
            "min/maxの戻り値不正")
        self.assertEqual(mm[1][0], center_pos[0]+r,
            "min/maxの戻り値不正")
        self.assertEqual(mm[1][1], center_pos[1]+r,
            "min/maxの戻り値不正")