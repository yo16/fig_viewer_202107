# YNF(Yo Neutral Format) class
import datetime
import pickle
from typing import Dict

from ...common.funcs import get_default_logger
from .element import cYnfElement

class cYnf():
    def __init__(self, canvas_info:Dict, logger=None):
        self.logger = logger or get_default_logger()

        # Ynf要素リスト
        self.elements = []

        # 要素を置く画像全体のサイズ
        self.canvas_width = canvas_info['canvas_width'] if 'canvas_width' in canvas_info else 300
        self.canvas_height = canvas_info['canvas_height'] if 'canvas_height' in canvas_info else 200

        # タイトル
        now = datetime.datetime.now()
        self.title = canvas_info['title'] if 'title' in canvas_info else now.strftime('%Y%m%d_%H%M%S')

        """
        delete for #28
        # 初期のツール情報
        self.current_tool = cYnfDrawingTool({
            'line_width': 1.0,
            'line_color': {'r':0, 'g':0, 'b':0},
            'fill_color': [255, 255, 255, 0.0]
        })
        """

    
    def append(self, element:cYnfElement) -> None:
        """ Ynf要素を追加する
        """
        self.elements.append(element)

        return None
        
    
    def set_canvas_size(self, canvas_width:int=None, canvas_height:int=None) -> None:
        """ キャンバスサイズを変更する
        """
        if canvas_width is not None:
            self.canvas_width = canvas_width
        if canvas_height is not None:
            self.canvas_height = canvas_height

        return None


    def get_minmax(self) -> list:
        """ min/maxの位置を返す
        """
        min_pos = [0,0]
        max_pos = [0,0]
        for i, e in enumerate(self.elements):
            cur_minmax = e.get_minmax()
            if i==0:
                min_pos[0] = cur_minmax[0][0]
                min_pos[1] = cur_minmax[0][1]
                max_pos[0] = cur_minmax[1][0]
                max_pos[1] = cur_minmax[1][1]
            min_pos[0] = min(min_pos[0], cur_minmax[0][0])
            min_pos[1] = min(min_pos[1], cur_minmax[0][1])
            max_pos[0] = max(max_pos[0], cur_minmax[1][0])
            max_pos[1] = max(max_pos[1], cur_minmax[1][1])
        
        return [min_pos, max_pos]


    def serialize(self, file_path: str) -> None:
        """
        シリアライズ（保存）する。
        """
        with open(file_path, 'wb') as f:
            pickle.dump(self, f)
    
    
    @classmethod
    def deserialize(cls, file_path: str) -> 'cYnf':
        """
        デシリアライズして返す
        """
        with open(file_path, 'rb') as f:
            y = pickle.load(f)
        
        return y
    

    def to_str(self) -> str:
        """
        文字列化してみる
        """
        ret_str = self.__class__.__name__

        self_vars = vars(self)
        # 変数
        for k, v in self_vars.items():
            ret_str += f'\n{k}:{v}'
        
        return ret_str