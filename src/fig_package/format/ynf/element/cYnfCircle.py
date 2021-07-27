""" 円関係
"""
from .cYnfElment import cYnfElement

class cYnfCircle(cYnfElement):
    """ Ynf円要素クラス

    必須prop
        center:List[int,int]
            中心座標
        r:int
            半径
    任意prop
        border-color(str): 線の色 #ffffff or #fff 形式
        border-width(int): 線の幅
    """
    def __init__(self, prop:dict):
        assert 'center' in prop, f'center is not defined. {prop}'
        assert len(prop['center'])==2, f'prop["center"] is invalid. {prop["center"]}'
        assert 'r' in prop, f'r is not defined. {prop}'

        if 'border-color' not in prop:
            prop['border-color'] = '#000'
        if 'border-width' not in prop:
            prop['border-width'] = 1

        super().__init__(prop)


    def get_minmax(self) -> list:
        center = self.prop['center']
        r = self.prop['r']

        return [[center[0]-r,center[1]-r],
                [center[0]+r,center[1]+r]]


class cYnfArc(cYnfElement):
    """ Ynf円弧要素クラス
    引数が冗長だが、気にしない。

    必須prop
        start:List[int,int]
            開始位置
        end:List[int,int]
            終了位置
        center:List[int,int]
            中心点
        r:int
            半径
        clockwise:bool
            回転角度[True:時計回り | False:反時計回り]
    任意prop
        border-color(str): 線の色 #ffffff or #fff 形式
        border-width(int): 線の幅
    """
    def __init__(self, prop:dict):
        assert 'start' in prop, f'start is not defined. {prop}'
        assert len(prop['start'])==2, f'prop["start"] is invalid. {prop["start"]}'
        assert 'end' in prop, f'end is not defined. {prop}'
        assert len(prop['end'])==2, f'prop["end"] is invalid. {prop["end"]}'
        assert 'center' in prop, f'center is not defined. {prop}'
        assert len(prop['center'])==2, f'prop["center"] is invalid. {prop["center"]}'
        assert 'r' in prop, f'r is not defined. {prop}'
        assert 'clockwise' in prop, f'clockwise is not defined. {prop}'

        if 'border-color' not in prop:
            prop['border-color'] = '#000'
        if 'border-width' not in prop:
            prop['border-width'] = 1

        super().__init__(prop)


    def get_minmax(self) -> list:
        center = self.prop['center']
        r = self.prop['r']
        
        return [[center[0]-r,center[1]-r],
                [center[0]+r,center[1]+r]]
