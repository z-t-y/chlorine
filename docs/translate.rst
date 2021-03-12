chlorine.translate
==================

translate包包含了一个类，这个类是chlorine的核心。

.. py:class:: Translate(to_translate)

    :param to_translate: 要翻译的句子

    chlorine的核心类，是chlorine的核心算法translate的所在类。

    .. py:function:: reserved_keywords()
    :returns: chlorine保留关键字列表，即RESERVED_KEYWORDS（见 :ref:`Chlorine中的常量`）
    reserved_keywords是一个静态函数，它可以用 ``Translate.reserved_keywords()`` 来调用。

    .. py:function:: translate()
    :returns: 翻译过后的句子
    translate函数完成chlorine的主要工作——翻译Translate类的参数 ``to_translate`` 中不规范的中文
