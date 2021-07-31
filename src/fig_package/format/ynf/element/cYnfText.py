""" 線関係
"""
from typing import Tuple

from .cYnfElment import cYnfElement
from ....common.exceptions import IlligalParameterError

class cYnfText(cYnfElement):
    """ Ynf文字列要素クラス

    必須prop
        text(str): 表示する文字列
        pos(list): 配置位置
    任意prop
        text-align(str): 横方向の位置 left/center/right
        text-valign(str): 縦方向の位置 top/middle/bottom
        text-color(str): 文字列の色　#ffffff または #fff 形式の文字列。
        font-size(float): フォントサイズ

    text、pos、text-align、text-valignで指示。背景は透過。
    posは、text-align、text-valignの示す場所。（左上なら左上）
    """
    def __init__(self, prop:dict):
        if 'text' not in prop:
            raise IlligalParameterError('text not in cYnfText')
        if prop['text'] is None:
            raise IlligalParameterError('text is None')
        if 'pos' not in prop:
            raise IlligalParameterError('pos not in cYnfText')
        if (type(prop['pos']) is not list) and \
           (type(prop['pos']) is tuple):
            raise IlligalParameterError(
                f'pos type is invalid.{str(type(prop["pos"]))}')
        super().__init__(prop)

        if 'text-align' not in prop:
            prop['text-align'] = 'left'
        if 'text-valign' not in prop:
            prop['text-valign'] = 'top'
        if 'font-size' not in prop:
            prop['font-size'] = 8.0
        if prop['text-align'] not in ['left', 'center', 'right']:
            raise IlligalParameterError(
                f'text-align value is invalid.{prop["text-align"]}')
        if prop['text-valign'] not in ['top', 'middle', 'bottom']:
            raise IlligalParameterError(
                f'text-valign value is invalid.{prop["text-valign"]}')
        if (type(prop['font-size']) is not int) and \
           (type(prop['font-size']) is not float):
            raise IlligalParameterError(
                f'font-size type is invalid.{str(type(prop["font-size"]))}')
        
        self.prop['text-align'] = prop['text-align']
        self.prop['text-valign'] = prop['text-valign']
        self.prop['font-size'] = prop['font-size']

        # fill-colorがNoneのときは、背景のboxを描かないようにするため、fill-color属性自体を消す
        if 'fill-color' in self.prop:
            if self.prop['fill-color'] is None:
                del self.prop['fill-color']


    def move(self, dx:int=0, dy:int=0):
        """ dx, dy分だけ移動する
        """
        self.prop['pos'][0] += dx
        self.prop['pos'][1] += dy

        return None


    def get_minmax(self) -> list:
        # font-size:20ptの前提
        width = len(self.prop['text'])*10
        height = 20
        left = self.prop['pos'][0]
        if self.prop['text-align']=='center':
            left -= width/2
        elif self.prop['text-align']=='right':
            left -= width
        top = self.prop['pos'][1]
        if self.prop['text-valign']=='middle':
            top -= height/2
        elif self.prop['text-valign']=='bottom':
            top -= height
        min_pos = [
            left,
            top
        ]
        max_pos = [
            left + width,
            top + height
        ]
        return [min_pos, max_pos]
