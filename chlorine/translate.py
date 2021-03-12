"""
    chlorine.translate
    ~~~~~~~~~~~~~~
    :copyright: (c) 2021 by the Fluorine Team.
    :license: GPL-3.0, see LICENSE for more details.
"""
from . import RESERVED_KEYWORDS


class Translate(object):
    """
    The translation object for chlorine
    """
    def __init__(self, string: str):
        self.to_translate = string

    @staticmethod
    def reserved_keywords() -> list:
        """
        The reserved of Chlorine.

        :return: chlorine关键字列表
        """
        return RESERVED_KEYWORDS

    def translate(self) -> str:
        # TODO: Complete the translation algorithm
        return self.to_translate
