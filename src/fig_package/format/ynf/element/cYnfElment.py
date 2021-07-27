class cYnfElement():
    """ Ynf要素クラス

    このクラスを継承して、要素を作成する。
    過剰かもしれないけど、全要素にツールインスタンスを持つ。
    順番を入れ替えたり一部を非表示にしたときに、
    前後がない単独の状態でも正しく表示できるように。
    """
    def __init__(self, prop:dict):
        # 必須項目（全要素共通）
        self.prop = {
            'display': True,
            'fill-color': None,
            'border-color': None,
            'border-width': 1.0,
        }

        # 任意項目（要素個別）
        for k,v in prop.items():
            self.prop[k] = v


    def move(self, dx, dy):
        """ dx, dy分だけ移動する
        """
        return


    def get_minmax(self) -> list:
        """ minとmaxの２点を返す
        """
        return [[0,0],[0,0]]


    def is_display(self) -> bool:
        """ 表示状態か非表示状態かを返す
        """
        if 'display' in self.prop:
            if self.prop['display']==False:
                return False
        return True
