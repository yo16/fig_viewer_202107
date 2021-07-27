""" 線関係
"""
from .cYnfElment import cYnfElement

class cYnfLine(cYnfElement):
    """ Ynf線分要素クラス

    必須prop
        p1(list): １点目の座標値
        p2(list): ２点目の座標値
    任意prop
        border-color(str): 線の色 #ffffff or #fff 形式
        border-width(int): 線の幅

    ２点を指示して線分を表現する。
    """
    def __init__(self, prop:dict):
        # cYnfLineの場合は、p1,p2のチェックをする
        # （このクラスを継承した子クラスの場合はチェックしない）
        if self.__class__.__name__=='cYnfLine':
            assert 'p1' in prop, 'p1 not in cYnfLine'
            assert (type(prop['p1']) is list) or (type(prop['p1']) is tuple), f'p1 is not list.{type(prop["p1"])}'
            assert 'p2' in prop, 'p2 not in cYnfLine'
            assert (type(prop['p2']) is list) or (type(prop['p2']) is tuple), f'p2 is not list.{type(prop["p2"])}'

        if 'border-color' not in prop:
            prop['border-color'] = '#000'
        if 'border-width' not in prop:
            prop['border-width'] = 1

        super().__init__(prop)


    def get_minmax(self) -> list:
        point1 = [self.prop['p1'][0], self.prop['p1'][1]]
        point2 = [self.prop['p2'][0], self.prop['p2'][1]]
        min_pos = [
            min(point1[0], point2[0]),
            min(point1[1], point2[1])
        ]
        max_pos = [
            max(point1[0], point2[0]),
            max(point1[1], point2[1])
        ]
        return [min_pos, max_pos]


class cYnfPolyline(cYnfLine):
    """ 線分クラスをつなげたポリライン

    必須prop
        points(list): 点群の座標
    任意prop
        isClose(bool): 閉じた線かどうか True/False
    """
    def __init__(self, prop:dict):
        assert 'points' in prop, 'points not in cYnfPolyline'
        assert type(prop['points']) is list, 'points is not list'
        super().__init__(prop)

        if 'isClose' not in prop:
            self.prop['isClose'] = False

        self.prop['points'] = []
        for p in prop['points']:
            assert (type(p) is list) or (type(p) is tuple), f'elm in points is not list.{type(p)}'
            self.prop['points'].append([p[0], p[1]])


    def get_minmax(self) -> list:
        min_pos = [
            min([p[0] for p in self.prop['points']]),
            min([p[1] for p in self.prop['points']])
        ]
        max_pos = [
            max([p[0] for p in self.prop['points']]),
            max([p[1] for p in self.prop['points']])
        ]
        return [min_pos, max_pos]


class cYnfBox(cYnfPolyline):
    """ ２点を指示するBox

    必須prop
        p1(list): 点１の座標
        p2(list): 点２の座標
    """
    def __init__(self, prop:dict):
        assert 'p1' in prop, 'p1 not in cYnfBox'
        assert (type(prop['p1']) is list) or (type(prop['p1']) is tuple), 'p1 is not list'
        assert 'p2' in prop, 'p2 not in cYnfBox'
        assert (type(prop['p2']) is list) or (type(prop['p2']) is tuple), 'p2 is not list'

        # 左上
        p1 = [
            min(prop['p1'][0],prop['p2'][0]),
            min(prop['p1'][1],prop['p2'][1])
        ]
        # 右下
        p2 = [
            max(prop['p1'][0],prop['p2'][0]),
            max(prop['p1'][1],prop['p2'][1])
        ]
        prop['points'] = [
            [p1[0],p1[1]],
            [p1[0],p2[1]],
            [p2[0],p2[1]],
            [p2[0],p1[1]]
        ]
        prop['isClose'] = True

        # p1、p2からpointsを作り出すことと、isCloseを作り出すため、
        # 処理の後に__init__を呼び出している。
        super().__init__(prop)
