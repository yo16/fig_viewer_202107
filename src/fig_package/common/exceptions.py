"""
パッケージ共通で使用する例外
"""

class IlligalParameterError(Exception):
    """
    パラメータ不正
    """

class WriteFileAlreadyExists(Exception):
    """
    出力ファイルが既に存在している
    """