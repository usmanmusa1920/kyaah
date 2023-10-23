# -*- coding: utf-8 -*-

"""
    =====================
    @ _log package
    =====================

    The `cli_txt.py` is mainly for logging
    The `tcolor.py` is mainly for print (equivalent)

    TODO: for logging
        >>> from kyaah._log import log_style
        
        >>> log_style('I am info logger')
        >>> log_style('I am warning logger', col='yellow')
        >>> log_style('I am error logger', log='error')

    TODO: for print
        >>> from kyaah._log import (header, blue, cyan, green, warning, fail, normal, bold, underline)

        >>> header('I am purple in color')
        >>> blue('I am blue in color')
        >>> cyan('I am cyan in color')
        >>> green('I am green in color')
        >>> warning('I am yellow in color')
        >>> fail('I am red in color')
        >>> normal('I am a normal text')
        >>> bold('I make text bold')
        >>> underline('I underline text')
"""

from .tcolor import *
from .cli_txt import log_style


__all__ = [
    'header',
    'blue',
    'cyan',
    'green',
    'warning',
    'fail',
    'normal',
    'bold',
    'underline',
    'log_style',
]
