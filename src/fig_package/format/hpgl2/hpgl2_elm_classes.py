""" HPGL2のデータ用クラス
"""
from typing import List, Tuple, Optional, Union
import math

from fig_package.format.ynf.element.cYnfElment import cYnfElement

from ..ynf import cYnf
from ..ynf import cYnfText, cYnfLine, cYnfPolyline, cYnfBox, cYnfCircle, cYnfArc


BP_PIC_NAME = 'BP Picture name'
PS_LENGTH = 'PS Length'
PS_WIDTH = 'PS Width'
RO_ANGLE = 'RO Rotate angle'

NP_NUMBER_OF_PENS = 'NP Number of pens'
PENS_INFO = 'Pens information'
PEN_NUMBER = 'Pen number'
PEN_COLOR = 'Pen color'
DICT_PEN_COLOR_RGB = {'0':'#FFF', '1':'#000', '2':'#F00', '3':'#0F0',
                      '4':'#FF0', '5':'#00F', '6':'#F0F', '7':'#0FF'}
PEN_DEFAULT_PEN_WIDTH = 'Default Pen width'
PEN_WIDTH = 'Pen width'

PEN_DOWN = 'Pen down'
PEN_POS = 'Pen Position'
PEN_LINETYPE = 'Pen linetype'
PEN_LINETYPE_PREV = 'Pen linetype (prev)'
PEN_LINE_PATTERN_LENGTH = 'Pen line pattern length'
PEN_LINE_PATTERN_MODE = 'Pen line pattern mode'
DICT_LINE_PATTERN = {
    '8':[50,10,0,10,10,10,0,10],
    '7':[70,10,0,10,0,10],
    '6':[50,10,10,10,10,10],
    '5':[70,10,10,10],
    '4':[80,10,0,10],
    '3':[70,30],
    '2':[50,50],
    '1':[0,100],
    '0':[0],
    '-1':[0,100,0],
    '-2':[25,50,25],
    '-3':[35,30,35],
    '-4':[40,10,0,10,40],
    '-5':[35,10,10,10,35],
    '-6':[25,10,10,10,10,10,25],
    '-7':[35,10,0,10,0,10,35],
    '-8':[25,10,0,10,10,10,0,10,25]
}

CHARACTER_SET = 'Character set'
DICT_CHARACTER_SET = {
    '0':'Roman8', '1':'Math-7', '2':'Line Draw-7', '3':'HP Large Characters',
    '4':'Norwegian v1', '37':'United Kingdom', '38':'French', '39':'German',
    '263':'Greek-8', '8':'Hebrew-7', '264':'Hebrew-8', '9':'Italian',
    '202':'Microsoft Publishing', '234':'DeskTop', '330':'PS Text',
    '426':'Ventura International', '458':'Ventura U.S.', '11':'JIS ASCII',
    '43':'Katakana', '267':'Kana-8', '299':'Korian-8', '1611':'JIS Kanji-1',
    '1643':'JIS Kanji-2', '12':'Line Draw-7', '44':'HP Block Charcters',
    '76':'Tax Line Draw', '268':'Line Draw-8', '300':'Ventra ITC Zapf Dingbats',
    '332':'PS ITC Zapf Dingbats', '364':'ITC Zapf Dingbats Series 100',
    '396':'ITC Zapf Dingbats Series 200',
    '428':'ITC Zapf Dingbats Series 300', '13':'Math-7', '45':'Tech-7 (DEC)',
    '173':'PS Math', '205':'Ventura Math', '269':'Math-8', 
    '14':'ECMA-94 Latin 1 (8-bit version)', '78':'ECMA-94 Latin 2',
    '174':'ECMA-128 Latin 5', '334':'ECMA-113/88 Latin/Cyrillic',
    '15':'OCR-A', '47':'OCR-B', '79':'OCR-M', '16':'APL (typewriter-paired)',
    '48':'APL (bit-paired)', '145':'PC Line', '18':'Cyrillic ASCII',
    '50':'Cyrillic', '114':'PC Cyrillic', '19':'Swedish for names',
    '83':'Spanish', '243':'HP European Spanish', '275':'HP Latin Spanish',
    '531':'HP-GL Download', '563':'HP-GL Drafting',
    '595':'HP-GL Special Symbols', '20':'Thai-8', '276':'Turkish-8',
    '21':'ANSI US ASCI', '53':'Legal', '181':'HPL Language Set',
    '245':'OEM-1 (DEC Set)', '277':'Roman8', '309':'Windows', '341':'PC-8',
    '373':'PC-8 Denmark/Norway', '405':'PC-850', '501':'Pi Font',
    '565':'PC-852', '22':'Arabic (MacKay\'s Version)', '278':'Arabic-8',
    '25':'3 of 9 Barcode', '57':'Industrial 2 of 5 Barcode',
    '89':'Matrix 2 of 5 Barcode', '153':'Interleaved 2 of 5 Barcode',
    '185':'CODABAR Barcode', '217':'MSI/Plessey Barcode',
    '249':'Code 11 Barcode', '281':'UPC/EAN Barcode', '505':'USPS Zip',
    '26': 'Not used'
}
FONT_SPACING = 'Font spacing'
DICT_FONT_SPACING = {
    '0': 'fixed spacing',
    '1': 'variable spacing'
}
FONT_PITCH = 'Font Pitch'
FONT_HEIGHT = 'Font Height'
FONT_POSTURE = 'Font Posture'
DICT_FONT_POSTURE = {'0':'upright', '1':'italic'}
FONT_WEIGHT = 'Font Weight'
FONT_TYPE_FACE = 'Font Type Face'
DICT_FONT_TYPE_FACE = {
    '0':'Line Printer or Line Draw', '1':'Pica', '2':'Elite',
    '3':'Courier', '4':'Helvetica', '5':'Times Roman',
    '6':'Letter Gothic', '7':'Script', '8':'Prestige',
    '9':'Caslon', '10':'Orator', '11':'Presentation', '13':'Serifa',
    '14':'Futura', '15':'Palatino', '16':'ITC Sourvenir', '17':'Optima',
    '18':'ITC Garamond', '20':'Coronet', '21':'Broadway',
    '23':'Century Schoolbook', '24':'Uninversity Roman',
    '27':'ITC Korinna', '28':'Naskh (generic Arbaic typeface)',
    '29':'Cloister Black', '30':'ITC Galliard',
    '31':'ITC Avant Garde Gothic', '32':'Brush', '33':'Blippo',
    '34':'Hobo', '35':'Windsor', '38':'Peignot', ''
    '39':'Baskerville', '41':'Trade Gothic', '42':'Gordy Old Style',
    '43':'ITC Zapf Chancery', '44':'Clarendon',
    '45':'ITC Zapf Dingbats', '46':'Cooper', '47':'ITC Bookman',
    '48':'Stick (default)', '49':'HP-GL Drafting',
    '50':'HP-GL fixed and variable arc', '51':'Gill Sans',
    '52':'Univers', '53':'Bodoni', '54':'Rockwell', '55':'Melior',
    '56':'ITC Tiffany', '57':'ITC Clearface', '58':'Amelia',
    '59':'Park Avenue', '60':'Handel Gothic', '61':'Dom Casual',
    '62':'ITC Benguiat', '63':'ITC Cheltenham', '64':'Century Expanded',
    '65':'Franklin Gothic', '68':'Plantin', '69':'Trump Mediaeval',
    '70':'Futura Black', '71':'ITC American Typewriter',
    '72':'Antique Olive', '73':'Uncial', '74':'ITC Bauhaus',
    '75':'Century Oldstyle', '76':'ITC Eras', '77':'ITC Friz Quadrata',
    '78':'ITC Lubalin Graph', '79':'Eurostile', '80':'Mincho',
    '81':'ITC Serif Gothic', '82':'Signet Roundhand',
    '83':'Souvenir Gothic', '84':'Stymie', '87':'Bernhard Modern',
    '89':'Excelsior', '90':'Grand Ronde Script', '91':'Ondine',
    '92':'P.T.Barnum', '93':'Kaufman', '94':'ITC Bolt Bold',
    '96':'Helv Monospaced', '97':'Revue', '101':'Garamond (Stemple)',
    '102': 'Garth Graphic', '103':'ITC Ronda', '104':'OCR-A',
    '105':'ITC Century', '106':'Englishe Schreibschrift',
    '107':'Flash', '108':'Gothic Outline (URW)', '109':'Stencil (ATF)',
    '110':'OCR-B', '111':'Akzdenz-Grotesk', '112':'TD Logos',
    '113':'Shannon', '114':'ITC Century', '152':'Maru Gosikku',
    '153':'Gosikku (Kaku)', '154':'Socho', '155':'Kyokasho',
    '156':'Kaisho'
}
DEFAULT_FONT_TYPE_FACE = '48'
DICT_PEN_LINE_PATTERN_MODE = {
    '0': 'Relative mode', '1': 'Absolute mode'
}

class cHpgl2Status():
    """ HPGL2の描画情報
    """
    def __init__(self):
        self.set_default_values()

    def set_default_values(self) -> None:
        self.params = {
            # 全体
            BP_PIC_NAME: '',
            PS_LENGTH: 0,
            PS_WIDTH: 0,
            RO_ANGLE: 0,

            # ペン
            NP_NUMBER_OF_PENS: 8,
            PEN_NUMBER: '0',
            PEN_COLOR: DICT_PEN_COLOR_RGB['0'],
            PEN_DEFAULT_PEN_WIDTH: 1.0,
            PEN_WIDTH: 1.0,
            PEN_DOWN: False,
            PEN_POS: [0,0],     # このPOSは、HPGL2の座標系
            PEN_LINETYPE: None,
            PEN_LINETYPE_PREV: None,
            PEN_LINE_PATTERN_LENGTH: 4,
            PEN_LINE_PATTERN_MODE: '0',

            # 文字
            CHARACTER_SET: DICT_CHARACTER_SET['0'],
            FONT_SPACING: DICT_FONT_SPACING['0'],
            FONT_PITCH: 3.0,
            FONT_HEIGHT: 12.0,
            FONT_POSTURE: DICT_FONT_POSTURE['0'],
            FONT_WEIGHT: 0,
            FONT_TYPE_FACE: DICT_FONT_TYPE_FACE[DEFAULT_FONT_TYPE_FACE],
        }
        return None

    def set_param(self, key:str, val:str) -> None:
        self.params[key] = val
    
    def get_param(self, key:str) -> Union[str, int, float]:
        return self.params[key]

    def get_wnd_pos(self, x0:int, y0:int) -> Tuple[int,int]:
        """ HPGL2内に書かれている(x,y)（左下が(0,0)右がx上がyの座標系）から
            画面の(x,y)（左上を(0,0),横がx,縦がyとする座標系）へ変換する
            RO要素の回転も考慮する。
        """
        angle = self.get_param(RO_ANGLE)
        length = self.get_param(PS_LENGTH)
        width = self.get_param(PS_WIDTH)

        # y軸を反転
        x1 = x0
        y1 = (-1)*y0

        # 回転
        theta = angle*math.pi/180.0
        x2 = x1*math.cos(theta) - y1*math.sin(theta)
        y2 = x1*math.sin(theta) + y1*math.cos(theta)
        
        # RO_ANGLEによって原点位置が変わる
        x3 = x2
        y3 = y2
        if angle==0:
            # 左下
            y3 = y2 + length
        elif angle==90:
            # 右下
            x3 = x2 + width
            y3 = y2 + length
        elif angle==180:
            # 右上
            x3 = x2 + width

        """
        もしこれをやるとしたら、長さも変換しなくちゃいけない
        # 座標が大きすぎて、ペンの幅が細くなるので
        # 座標を小さくする
        x4 = x3
        y4 = y3
        """

        return (x3,y3)


class cHpgl2ElmCommand(object):
    """ HPGL2のコマンドの親クラス
    """
    def __init__(self, str_cmnd:str):
        self.mnemonic = str_cmnd[:2]
        self.param = str_cmnd[2:].rstrip(';')
    
    def set_status(self, st:cHpgl2Status) -> None:
        """ ステータスを定義・変更する
        引数の cHpgl2Status を更新する。
        """
        return None
    
    def get_ynf(self, st:cHpgl2Status) -> Optional[cYnfElement]:
        """ stを参考にしてcYnfElementを作って返す
        cYnfElementを作らない場合は、Noneを返す。
        """
        return None
    
    def quated_string(self, param_str:str) -> str:
        """ Quated Stringを文字列にして返す
        """
        ret_str = param_str.strip('"')
        ret_str = ret_str.replace('""', '"')
        return ret_str


class cExcHpgl2IgnoreInstruction(Exception):
    """ Intruction(命令)をスキップする例外
    """
    pass

# ----------------------- #
# 要素クラス                #
# ----------------------- #
class cHpgl2IN(cHpgl2ElmCommand):
    """ IN, Initialize
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)


class cHpgl2PG(cHpgl2ElmCommand):
    """ PG, Advanced Full Page
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)


class cHpgl2RO(cHpgl2ElmCommand):
    """ RO, Rotate Coordinate System
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)
    
    def set_status(self, st:cHpgl2Status) -> None:
        rotate_angle = 0
        if len(self.param)>0:
            if self.param not in ['0','90','180','270']:
                raise cExcHpgl2IgnoreInstruction(
                    f'RO angle error.{rotate_angle}')
            rotate_angle = int(self.param)
        st.set_param(RO_ANGLE, rotate_angle)

        return None


class cHpgl2AA(cHpgl2ElmCommand):
    """ AA, Arc Absolute
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)

    def get_ynf(self, st:cHpgl2Status) -> Optional[cYnfElement]:
        return self.get_ynf_AAarc(st)
        #return self.get_ynf_AApolyline(st)

    def get_ynf_AAarc(self, st:cHpgl2Status) -> Optional[cYnfElement]:
        params = self.param.split(',')
        try:
            cx = int(params[0])
            cy = int(params[1])
            sweep_angle = float(params[2])
        except:
            raise cExcHpgl2IgnoreInstruction(
                    f'AA のパラメータが不正 ({self.param})')
        
        # 現在の位置
        x1,y1 = st.get_param(PEN_POS)
        # (cx,cy)からsweep_angle度回した点を取得
        clockwise = (sweep_angle<0)
        if not clockwise:
            sweep_angle = sweep_angle % 360.0
        else:
            sweep_angle = sweep_angle % (-360.0)
        #print(f'seep_angle:{sweep_angle}')
        sweep_angle_rad = sweep_angle * math.pi / 180.0
        #print(f'sweep_angle_rad:{sweep_angle_rad}')
        x2 = (x1-cx)*math.cos(sweep_angle_rad) \
            - (y1-cy)*math.sin(sweep_angle_rad) \
            + cx
        y2 = (x1-cx)*math.sin(sweep_angle_rad) \
            + (y1-cy)*math.cos(sweep_angle_rad) \
            + cy
        
        # 半径
        r = math.sqrt( (x1-cx)**2 + (y1-cy)**2 )
        #print(f'r:{r}')
        
        #print(f'center:({cx},{cy})')
        #print(f'p1:({x1},{y1})')
        #print(f'p2:({x2},{y2})')
        #print(f'clockwise:{clockwise}')
        # パラメータを作成
        arc_params = {
            'start': st.get_wnd_pos(x1,y1),
            'end': st.get_wnd_pos(x2,y2),
            'center': st.get_wnd_pos(cx,cy),
            'r': r,
            'clockwise': clockwise
        }
        #print(arc_params)
        # 線の共通パラメータを付け加える
        arc_params.update(get_line_common_param(st))

        return cYnfArc(arc_params)


    def get_ynf_AApolyline(self, st:cHpgl2Status) -> Optional[cYnfElement]:
        """ polyline版の円弧（使わない）
        """
        params = self.param.split(',')
        try:
            cx = int(params[0])
            cy = int(params[1])
            sweep_angle = float(params[2])
            chord_angle = 5.0   # 分解能＝この角度を直線で結ぶ
            if len(params)>3:
                chord_angle = float(params[3])
        except:
            raise cExcHpgl2IgnoreInstruction(
                    f'AA のパラメータが不正 ({self.param})')

        # 円弧ではなく、Polylineで円弧を描く
        # （それがHPGL2の円弧）
        # 角度を丸める
        if sweep_angle>0:
            sweep_angle = sweep_angle % 360.0
        else:
            sweep_angle = sweep_angle % (-360.0)
        sweep_angle_rad = sweep_angle * math.pi / 180.0

        # 現在の座標値
        x1,y1 = st.get_param(PEN_POS)
        str_xy_array = f'{int(x1)},{int(y1)}'
        x1 = float(x1)
        y1 = float(y1)

        abs_rotated_angle = 0.0
        d_theta = chord_angle * math.pi / 180.0
        while abs_rotated_angle < abs(sweep_angle):
            # 回転後の座標を求める
            x2 = (x1-cx)*math.cos(d_theta) \
               - (y1-cy)*math.sin(d_theta) \
               + cx
            y2 = (x1-cy)*math.sin(d_theta) \
               + (y1-cy)*math.cos(d_theta) \
               + cy
            
            str_xy_array += f',{int(x2)},{int(y2)}'

            x1 = x2
            y1 = y2
            abs_rotated_angle += chord_angle
        #print(str_xy_array)

        # Polyline要素を作って返す
        return get_polylinexy_array(str_xy_array, st)


class cHpgl2CI(cHpgl2ElmCommand):
    """ CI, Circle
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)
    
    def get_ynf(self, st:cHpgl2Status) -> Optional[cYnfElement]:
        if len(self.param)==0:
            raise cExcHpgl2IgnoreInstruction(
                    'CI のパラメータがない')
        
        # 現在の点が中心
        cx,cy = st.get_param(PEN_POS)
        cx1,cy1 = st.get_wnd_pos(cx, cy)

        # 半径
        params = self.param.split(',')
        try:
            radius = float(params[0])
        except:
            raise cExcHpgl2IgnoreInstruction(
                f'CI のパラメータが不正 ({params[0]})')

        # 線のパラメータを作成
        circle_params = {
            'center': [cx1, cy1],
            'r': radius
        }
        # 線の共通パラメータを付け加える
        circle_params.update(get_line_common_param(st))

        return cYnfCircle(circle_params)


class cHpgl2PA(cHpgl2ElmCommand):
    """ PA, Plot Absoliute
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)

    def get_ynf(self, st:cHpgl2Status) -> Optional[cYnfElement]:
        if len(self.param)==0:
            return None
        
        # Polyline要素を作って返す
        return get_polylinexy_array(self.param, st)


def get_polylinexy_array(str_xy_array:str, st:cHpgl2Status) \
    -> cYnfPolyline:
    """ cYnfPolylineインスタンスを作って返す

    いくつかのクラスで使われる処理なので関数化した。
    - st.get_wnd_pos() はこの中でやるので、呼び出し元での st.get_wnd_pos() は不要。
    - st.get_wnd_pos() もこの中で最後の点へ移動するので、呼び出し元は不要。

    Params:
        str_xy_array:str
            x,y,x,y,... の形式の文字列。x,yはint。
        st:cHpgl2Status
            ステータスオブジェクト。
    Returns:
        cYnfPolyline
    """
    #print('get_polylinexy_array!!')
    xy_array = str_xy_array.split(',')
    # x,y,x,y,...
    if len(xy_array)%2!=0:
        raise cExcHpgl2IgnoreInstruction(
            f'xとyのセットになっていない({str_xy_array})')
    
    # Pen-Up だったら最後の座標へ移動するだけ
    if not st.get_param(PEN_DOWN):
        try:
            st.set_param(PEN_POS, 
                [int(xy_array[-2]), int(xy_array[-1])])
        except:
            raise cExcHpgl2IgnoreInstruction(
                    f'PA のパラメータが非整数 ({str_xy_array})')
        return None

    # Pen-Down なので線要素を作成する
    # まずそのための座標群を得る
    wnd_xy_pairs = []
    # 元々の座標値を追加
    x, y = st.get_param(PEN_POS)
    #print(f'元のPOS:{x},{y}')
    wnd_xy_pairs.append(st.get_wnd_pos(x,y))
    # PA要素に含まれている座標を追加
    for i in range(len(xy_array)//2):
        #try:
        if True:
            x = int(xy_array[i*2])
            y = int(xy_array[i*2+1])
        #except:
        #    raise cExcHpgl2IgnoreInstruction(
        #            f'PA のパラメータが非整数 ({str_xy_array})')
        #print(f'新しいPOS:{x},{y}')
        #new_wnd_pos = st.get_wnd_pos(x,y)
        #print(f'新しいwndPOS:{new_wnd_pos[0]},{new_wnd_pos[1]}')
        wnd_xy_pairs.append(st.get_wnd_pos(x,y))
        
    # 現在地を更新
    st.set_param(PEN_POS, [int(x), int(y)])
    
    # 点が３点以上の場合はPolyline、２点の場合はline
    elm = None
    if len(wnd_xy_pairs)>2:
        # パラメータを作成
        polyline_params = {
            'points':wnd_xy_pairs,
            'isClose':False
        }
        # 線の共通パラメータを付け加える
        polyline_params.update(get_line_common_param(st))

        # cYnfPolylineを生成
        elm = cYnfPolyline(polyline_params)

    elif len(wnd_xy_pairs)==2:
        ### 2020/8/13 start
        # 下記は書いてみたものの、距離ゼロでドットを書きたいときがあるかもしれないのでコメントアウトしておく(2020/8/13)
        ## p1とp2の距離が小さいときは何も作らない
        #p1p2_distance = math.sqrt((wnd_xy_pairs[0][0] - wnd_xy_pairs[1][0])**2 + (xy_pairs[0][1] - xy_pairs[1][1])**2)
        #if p1p2_distance<=1.0:
        #    return None
        ### 2020/8/13 end

        # パラメータを作成
        line_params = {
            'p1':wnd_xy_pairs[0],
            'p2':wnd_xy_pairs[1]
        }
        # 線の共通パラメータを付け加える
        line_params.update(get_line_common_param(st))

        # cYnfLineを生成
        elm = cYnfLine(line_params)

    else:
        assert False, f'wnd_xy_pairsが不正 {wnd_xy_pairs}'

    return elm


def get_line_common_param(st:cHpgl2Status) -> dict:
    """ ライン系の共通のパラメータを取得してdictにして返す
    """
    # 現在のペン
    cur_pen_number = int(st.get_param(PEN_NUMBER))
    pens_info = st.get_param(PENS_INFO)
    cur_pen = pens_info[cur_pen_number]

    # ペンの色
    pen_color = cur_pen[PEN_COLOR]

    # 線太さ
    pen_width = cur_pen[PEN_WIDTH]*50

    # 線種
    line_type = st.get_param(PEN_LINETYPE)
    # パターン
    if line_type is None:
        line_pattern = None
    else:
        line_pattern = DICT_LINE_PATTERN[line_type]
    # パターン長
    pattern_length = st.get_param(PEN_LINE_PATTERN_LENGTH)
    # パターン長の単位['0':%, '1':mm]
    pattern_length_unit = st.get_param(PEN_LINE_PATTERN_MODE)

    return {
        'border-color':pen_color,
        'border-width':pen_width,
        'linetype':line_type,
        'line-pattern-length':pattern_length,
        'line-pattern':line_pattern,
        'line-pattern-length-mode':pattern_length_unit
    }


class cHpgl2PD(cHpgl2ElmCommand):
    """ PD, Pen Down
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)
    
    def set_status(self, st:cHpgl2Status) -> None:
        st.set_param(PEN_DOWN, True)
        return None


class cHpgl2PU(cHpgl2ElmCommand):
    """ PU, Pen Up
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)
    
    def set_status(self, st:cHpgl2Status) -> None:
        st.set_param(PEN_DOWN, False)
        return None


class cHpgl2LT(cHpgl2ElmCommand):
    """ LT, Line Type
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)
    
    def set_status(self, st:cHpgl2Status) -> None:
        # 前の線種を取得
        prev_linetype = st.get_param(PEN_LINETYPE_PREV)
        # 現在の線種を取得
        st.set_param(PEN_LINETYPE_PREV, st.get_param(PEN_LINETYPE))

        # 次の線種を決定
        if len(self.param)==0:
            # Solid
            st.set_param(PEN_LINETYPE, None)
        
        elif self.param=='99':
            # 前の線種を今の線種にする
            st.set_param(PEN_LINETYPE, prev_linetype)
        
        else:
            # 指定した線種にする
            str_params = self.param.split(',')
            try:
                n_linetype = int(str_params[0])
                if n_linetype not in \
                    [-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8]:
                    raise Exception
                if len(str_params)>1:
                    pattern_length = int(str_params[1])
                    if (pattern_length<=0) or (32767<pattern_length):
                        raise Exception
                if len(str_params)>2:
                    mode = str_params[2]
                    if (mode!='0') and (mode!='1'):
                        raise Exception
            except:
                raise cExcHpgl2IgnoreInstruction(
                        f'LT の linetype が不正 ({self.param})')
            
            if len(str_params)>=1:
                # 線種の変更を、線種番号を指定する
                st.set_param(PEN_LINETYPE, str_params[0])

            if len(str_params)>=2:
                # パターン長を指定する
                pattern_length = int(str_params[1])
                st.set_param(PEN_LINE_PATTERN_LENGTH, pattern_length)
            
            if len(str_params)>=3:
                # パターンモードを指定する
                mode = str_params[2]
                st.set_param(PEN_LINE_PATTERN_MODE, mode)

        return None


class cHpgl2PW(cHpgl2ElmCommand):
    """ PW, Pen Width
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)

    def set_status(self, st:cHpgl2Status) -> None:
        # パラメータがない場合は、未実装
        # （デフォルトの幅を変える？）
        if len(self.param)==0:
            return None
        try:
            params = self.param.split(',')
            if len(params)>1:
                # 0:太さ, 1:ペン番号
                # 指定したペン番号のペンの太さを変更する
                pen_width = float(params[0])
                pen_number = int(params[1])
                pens_info = st.get_param(PENS_INFO)
                pens_info[pen_number][PEN_WIDTH] = pen_width
                st.set_param(PENS_INFO, pens_info)
            elif len(params)>0:
                # 0:太さ
                # すべてのペン太さを変更する
                pen_width = float(params[0])
                pens_info = st.get_param(PENS_INFO)
                for p in pens_info:
                    p[PEN_WIDTH] = pen_width
                st.set_param(PENS_INFO, pens_info)
        except:
            raise cExcHpgl2IgnoreInstruction(
                f'PW のパラメータが不正 ({self.param})')
        
        return None


class cHpgl2SP(cHpgl2ElmCommand):
    """ SP, Select Pen
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)

    def set_status(self, st:cHpgl2Status) -> None:
        pen_used = 0
        if (len(self.param)==0) or (self.param=='0'):
            pen_used = 0
        
        else:
            try:
                pen_no = int(self.param)
                if pen_no<0:
                    raise
            except:
                raise cExcHpgl2IgnoreInstruction(
                    f'SPのパラメータが不正 {self.param}')
        
            # 定義されたペンの中からペン番号を決める
            number_of_pens = st.get_param(NP_NUMBER_OF_PENS)
            pen_used = ((pen_no-1)%(number_of_pens-1))+1
        
        #print(f'pen_used:{pen_used}')
        # ペンを選択する
        st.set_param(PEN_NUMBER, str(pen_used))
        pen_info = st.get_param(PENS_INFO)[pen_used]
        st.set_param(PEN_COLOR, pen_info[PEN_COLOR])

        return None


class cHpgl2SD(cHpgl2ElmCommand):
    """ SD, Standard Font Definition
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)

    def set_status(self, st:cHpgl2Status) -> None:
        kvs = self.param.split(',')
        # kind,value,kind,value...
        if len(kvs)%2!=0:
            raise cExcHpgl2IgnoreInstruction(
                f'kindとvalueのセットになっていない({self.param})')

        kv_pairs = []
        for i in range(len(kvs)//2):
            kind = kvs[i*2]
            value = kvs[i*2+1]
            if kind not in ['1','2','3','4','5','6','7']:
                raise cExcHpgl2IgnoreInstruction(
                    f'SDのkeyが不正{self.param}')

            if kind==1:
                # Character set（文字セット）
                if value not in CHARACTER_SET:
                    raise cExcHpgl2IgnoreInstruction(
                        f'SD の Character set が不正 ({self.param})')
                st.set_param(CHARACTER_SET, DICT_CHARACTER_SET[value])

            elif kind==2:
                # Font Spacing（文字間隔）
                if value not in DICT_FONT_SPACING:
                    raise cExcHpgl2IgnoreInstruction(
                        f'SD の Font Spacing が不正 ({self.param})')
                st.set_param(FONT_SPACING, DICT_FONT_SPACING[value])

            elif kind==3:
                # Pitch（文字ピッチ）
                try:
                    f_pitch = float(value)
                    if f_pitch<0 or 32767<f_pitch:
                        raise Exception
                except:
                    raise cExcHpgl2IgnoreInstruction(
                        f'SD の Pitch が不正 ({self.param})')
                st.set_param(FONT_SPACING, f_pitch)

            elif kind==4:
                # Height（サイズ）
                try:
                    f_height = float(value)
                    if f_height<0 or 32767<f_height:
                        raise Exception
                except:
                    raise cExcHpgl2IgnoreInstruction(
                        f'SD の height が不正 ({self.param})')
                st.set_param(FONT_HEIGHT, f_height)

            elif kind==5:
                # posture（スタイル）
                if value not in DICT_FONT_POSTURE:
                    raise cExcHpgl2IgnoreInstruction(
                        f'SD の Posture が不正 ({self.param})')
                st.set_param(FONT_POSTURE, DICT_FONT_POSTURE[value])

            elif kind==6:
                # Stroke Weight（太さ）
                try:
                    f_weight = int(value)
                    if f_weight!=9999 and (f_weight<-7 or 7<f_weight):
                        raise Exception
                except:
                    raise cExcHpgl2IgnoreInstruction(
                        f'SD の weight が不正 ({self.param})')
                st.set_param(FONT_WEIGHT, f_weight)

            elif kind==7:
                # Typeface（書体）
                if value not in DICT_FONT_TYPE_FACE:
                    raise cExcHpgl2IgnoreInstruction(
                        f'SD の Typeface が不正 ({self.param})')
                st.set_param(FONT_TYPE_FACE, DICT_FONT_TYPE_FACE[value])
        
        return None


class cHpgl2SS(cHpgl2ElmCommand):
    """ SS, Select Standard Font
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)

    def set_status(self, st:cHpgl2Status) -> None:
        st.set_param(FONT_TYPE_FACE, DICT_FONT_TYPE_FACE[DEFAULT_FONT_TYPE_FACE])

        return None


class cHpgl2BP(cHpgl2ElmCommand):
    """ BP, Begin Plot
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)
    
    def set_status(self, st:cHpgl2Status) -> None:
        if len(self.param)==0:
            return None

        kvs = self.param.split(',')
        # kind,value,kind,value...
        assert len(kvs)%2==0, f'kindとvalueのセットになっていない({self.param})'
        kv_pairs = []
        for i in range(len(kvs)//2):
            kind = kvs[i*2]
            value = kvs[i*2+1]
            assert kind not in [1,2,3,4,5], f'keyが不正{self.param}'

            if kind==1:
                # Picture Name
                st.set_param(BP_PIC_NAME, self.quated_string(value))
            # これ以外のkindは本プログラムに関係ないので見ない

        return None


class cHpgl2PS(cHpgl2ElmCommand):
    """ PS, Plot Size
    物理的な紙の軸方向ごとの上限値。
    length: 紙が出る方向の長さ
    width: 紙の幅
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)

    def set_status(self, st:cHpgl2Status) -> None:
        if len(self.param)==0:
            return None

        params = self.param.split(',')
        if len(params)>0:
            int_length = int(params[0])
            if int_length<=0:
                raise cExcHpgl2IgnoreInstruction(
                        f'PS length error. {params[0]}')
            st.set_param(PS_LENGTH, int_length)
        if len(params)>1:
            int_width = int(params[1])
            if int_width<=0:
                raise cExcHpgl2IgnoreInstruction(
                        f'PS width error. {params[1]}')
            st.set_param(PS_WIDTH, int_width)

        return None


class cHpgl2NP(cHpgl2ElmCommand):
    """ NP, Number of Pens
    """
    def __init__(self, str_cmnd:str):
        super().__init__(str_cmnd)

    def set_status(self, st:cHpgl2Status) -> None:
        if len(self.param)==0:
            st.set_param(NP_NUMBER_OF_PENS, 8)
            return None
        
        # ペン数を設定
        num_of_pens = None
        try:
            num_of_pens = int(self.param)
            if num_of_pens&(num_of_pens-1)!=0:  # num_of_pens が２のべき乗でない
                raise Exception
            elif num_of_pens<2:
                raise Exception
        except:
            raise cExcHpgl2IgnoreInstruction(
                    f'NP の パラメータが不正 ({num_of_pens})')
        st.set_param(NP_NUMBER_OF_PENS, num_of_pens)

        # すべてのペンの幅と色を決定する
        default_pen_width = st.get_param(PEN_DEFAULT_PEN_WIDTH)
        len_DICT_PEN_COLOR_RGB = len(DICT_PEN_COLOR_RGB)
        pens = [
            {
                PEN_WIDTH: default_pen_width,
                PEN_COLOR: DICT_PEN_COLOR_RGB[str(i%len_DICT_PEN_COLOR_RGB)]
            }
            for i in range(num_of_pens)
        ]
        st.set_param(PENS_INFO, pens)

        return None

