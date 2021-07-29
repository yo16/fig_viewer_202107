""" 円関係
"""
from .cYnfElment import cYnfElement
from ....common.exceptions import IlligalParameterError

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
        if 'center' not in prop:
            raise IlligalParameterError(f'Center is not defined. {prop}')
        if len(prop['center'])!=2:
            raise IlligalParameterError(
                f'Prop["center"] is invalid. {prop["center"]}')
        if 'r' not in prop:
            raise IlligalParameterError(f'Property "r" is not defined. {prop}')

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
    あと角度でも指定したくなりそうではあるけど、気にしない。

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
            デフォルトの方向がどっちもありうるので必須propとする。
    任意prop
        border-color(str): 線の色 #ffffff or #fff 形式
        border-width(int): 線の幅
    """
    def __init__(self, prop:dict):
        if 'start' not in prop:
            raise IlligalParameterError(f'start is not defined. {prop}')
        if len(prop['start'])!=2:
            raise IlligalParameterError(
                f'prop["start"] is invalid. {prop["start"]}')
        if 'end' not in prop:
            raise IlligalParameterError(f'end is not defined. {prop}')
        if len(prop['end'])!=2:
            raise IlligalParameterError(
                f'prop["end"] is invalid. {prop["end"]}')
        if 'center' not in prop:
            raise IlligalParameterError(
                f'center is not defined. {prop}')
        if len(prop['center'])!=2:
            raise IlligalParameterError(
                f'prop["center"] is invalid. {prop["center"]}')
        if 'r' not in prop:
            raise IlligalParameterError(f'r is not defined. {prop}')
        if 'clockwise' not in prop:
            raise IlligalParameterError(f'clockwise is not defined. {prop}')
        
        if 'border-color' not in prop:
            prop['border-color'] = '#000'
        if 'border-width' not in prop:
            prop['border-width'] = 1

        super().__init__(prop)


    def get_minmax(self) -> list:
        """
        円を描いたmin/maxにする
        判定がめんどくさい
        """
        center = self.prop['center']
        r = self.prop['r']
        
        return [[center[0]-r,center[1]-r],
                [center[0]+r,center[1]+r]]
