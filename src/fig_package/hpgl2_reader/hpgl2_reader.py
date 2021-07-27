
from logging import Logger
import os
import re
import traceback
from typing import List

from fig_package.format.hpgl2.hpgl2_elm_classes import cHpgl2Status

from ..basic_reader import BasicReader
from .exceptions import BadHpgl2FormatError
from ..format.hpgl2 import cHpgl2ElmCommand, cHpgl2IN, cHpgl2PG, cHpgl2RO, \
    cHpgl2AA, cHpgl2CI, cHpgl2PA, cHpgl2PD, cHpgl2PU, cHpgl2LT, cHpgl2PW, \
    cHpgl2SP, cHpgl2SD, cHpgl2SS, cHpgl2BP, cHpgl2PS, cHpgl2NP
from ..format.ynf import cYnf


class Hpgl2Reader(BasicReader):
    """
    HPGL2Reader クラス
    HPGL2を読む。
    """
    def __init__(self, file_path:str, logger:Logger=None):
        """
        コンストラクタ

        Parameters
        ----------
        file_path: str
            読み込むファイルのパス。
        logger: Logger
            ロガー。指定されない場合は別途定義してあるデフォルトロガー。
        """
        super().__init__(file_path=file_path, logger=logger)


    def __to_ynf(self, file_path:str) -> None:
        """
        YNF形式へ変換する。
        Private method.
        変換した結果を、self.ynf へ格納する。
        BasicReaderクラスを継承したクラスは、主にこの関数を実装する。

        Parameters
        ----------
        file_path: str
            読み込むファイルのパス。
            存在しない場合は FileNotFoundError をraiseする。
        
        Exception
        ---------
        BadHpgl2FormatError
            HPGL2フォーマットの致命的なエラー
        """
        self.logger.debug(f'Start to_ynf')

        # ファイルを読む
        self.logger.debug(f'read_file')
        hpgl2_text = ''
        with open(file_path, mode='r') as f:
            hpgl2_text = f.read()
        
        # パース
        self.logger.debug(f'perse')
        try:
            persed_commands = self.__hpgl2_perse(hpgl2_text)
        except BadHpgl2FormatError as e:
            msg = 'Bad HPGL2 format.'
            self.logger.error(msg)
            raise BadHpgl2FormatError(msg)

        # YNF化
        self.logger.debug(f'to_ynf')
        st = cHpgl2Status()
        for c in persed_commands:
            # ステータスを定義・変更する
            c.set_status(st)

            # コマンドからYnfElementインスタンスを生成
            ynf_elm = c.get_ynf(st)

            # YNF要素を返す場合は追加
            # （ステータスを変更するだけでYnf的には何もしないコマンドもある）
            if ynf_elm is not None:
                self.ynf.append(ynf_elm)

        self.logger.debug(f'End to_ynf')
        return



    def __hpgl2_perse(self, hpgl2_text:str) -> List[cHpgl2ElmCommand]:
        """
        HPGL2をパースして、コマンドインスタンスのリストにする。
        コマンドの１つずつは Hpgl2ElmCommand を継承したクラスのインスタンス。
        ここでは、描画に関する処理はせず、解釈するだけ。

        Parameters
        ----------
        hpgl2_text: str
            HPGL2ファイルの文字列
        
        Returns
        -------
        List[cHpgl2ElmCommand]
            コマンドインスタンスのリスト
        
        Exceptions
        ----------
        BadHpgl2FormatError
            HPGL2ファイルのフォーマットに沿ってなくて読み込めない場合
        """
        # ヘッダ(ESC%-1B の5バイト)
        if(
            (hpgl2_text[:1].encode()!=b'\x1B') or # 先頭だけESCをバイト型で比較
            (hpgl2_text[1:5]!='%-1B')
        ):
            msg = 'Bad initial byte order mark.'
            self.logger.error(msg)
            raise BadHpgl2FormatError(msg)
        
        # アルファベット２文字で始まるコマンドを探す
        ptn_command = re.compile(r'[A-Za-z]{2}[^A-Za-z]*')
        cur_pos = 5
        commands = []
        for m in ptn_command.finditer(hpgl2_text[cur_pos:]):
            # 検索結果を取得
            #print(m.group())
            line = m.group()
            cur_pos = m.end()
            mnemonic = line[:2]
            e = None

            # ['AA', 'BP', 'CI', 'IN', 'LT', 'NP', 'PA', 'PD', 
            #  'PG', 'PS', 'PU', 'PW', 'RO', 'SD', 'SP', 'SS']
            try:
                ## The Instruction Groups
                # The Kernel
                # - The Configuration and Status Group
                # CO/DF/IN/IP/IR/IW/PG/RO/RP/SC
                # IN
                if mnemonic=='IN':
                    e = cHpgl2IN(line)

                # PG
                elif mnemonic=='PG':
                    e = cHpgl2PG(line)

                # RO
                elif mnemonic=='RO':
                    e = cHpgl2RO(line)

                # - The Vector Group
                # AA/AR/AT/CI/PA/PD/PE/PR/PU/RT
                # AA
                elif mnemonic=='AA':
                    e = cHpgl2AA(line)

                # CI
                elif mnemonic=='CI':
                    e = cHpgl2CI(line)

                # PA
                elif mnemonic=='PA':
                    e = cHpgl2PA(line)

                # PD
                elif mnemonic=='PD':
                    e = cHpgl2PD(line)

                # PU
                elif mnemonic=='PU':
                    e = cHpgl2PU(line)

                # - The Polygon Group
                # EA/EP/ER/EW/FP/PM/RA/RR/WG

                # - The Line and Fill Attributes Group
                # AC/FT/LA/LT/PW/RF/SM/SP/UL/WU
                # LT
                elif mnemonic=='LT':
                    e = cHpgl2LT(line)

                # PW
                elif mnemonic=='PW':
                    e = cHpgl2PW(line)

                # SP
                elif mnemonic=='SP':
                    e = cHpgl2SP(line)

                # - The Character Group
                # AD/CF/CP/DI/DR/DT/DV/ES/LB/LO/SA/SD/SI/SL/SR/SS/TD
                # SD
                elif mnemonic=='SD':
                    e = cHpgl2SD(line)

                # SS
                elif mnemonic=='SS':
                    e = cHpgl2SS(line)

                # The Extensions
                # - The Technical Graphics Extension
                # BP/CT/DL/EC/FR/MC/MG/MT/NR/OE/OH/OI/OP/OS/PS/QL/ST/VS
                # BP
                elif mnemonic=='BP':
                    e = cHpgl2BP(line)

                # PS
                elif mnemonic=='PS':
                    e = cHpgl2PS(line)

                # - The Palette Extension
                # CR/NP/PC/SV/TR
                # NP
                elif mnemonic=='NP':
                    e = cHpgl2NP(line)

                # - The Dual-Context Extension
                # FI/FN/SB/ESC%#A/ESCE

                # - The Digitizing Extension
                # DC/DP/OD

                # - The Advanced Drawing Extension
                # BR/BZ/MC/PP

                # - The Advanced Text Extension
                # LM/SB

                # 未知のmnemonicの場合は警告を出す
                if e is None:
                    msg = f'Unknown mnemonic!:{line}'
                    self.logger.warning(msg)
                    assert e is not None, f'Unknown mnemonic!:{line}'

                # コマンドを追加
                commands.append(e)

            except BadHpgl2FormatError as e:
                # スキップ
                self.logger.warning(
                    traceback.format_exception_only(type(e),e))
                continue

        return commands

