# -*- coding: utf-8 -*-
"""
    ================================
    @ Kyaah software toolkit package
    ================================

          ,-.                                      ,---,     
      ,--/ /|                                    ,--.' |     
    ,--. :/ |                                    |  |  :     
    :  : ' /                                     :  :  :     
    |  '  /        .--,   ,--.--.      ,--.--.   :  |  |,--. 
    '  |  :      /_ ./|  /       \    /       \  |  :  '   | 
    |  |   \  , ' , ' : .--.  .-. |  .--.  .-. | |  |   /' : 
    '  : |. \/___/ \: |  \__\/: . .   \__\/: . . '  :  | | | 
    |  | ' \ \.  \  ' |  ," .--.; |   ," .--.; | |  |  ' | : 
    '  : |--'  \  ;   : /  /  ,.  |  /  /  ,.  | |  :  :_:,' 
    ;  |,'      \  \  ;;  :   .'   \;  :   .'   \|  | ,'     
    '--'         :  \  \  ,     .-./|  ,     .-./`--''       
                  \  ' ;`--`---'     `--`---'                
                   `--`                                      
    
    Kyaah abstract away cognitive over-head of sending SMTP mail, together with other mailing operations things like, mail with file, tokens etc.

    Usage at a glance:
        >>> import kyaah

        >>> sender = 'youremail@gmail.com'
        >>> receiver = ['receiver_1@gmail.com', 'receiver_2@gmail.com']
        >>> passwd = '*********' # use app password

        >>> server = 'gmail'
        >>> subj = f'Hellow world!'
        >>> body = 'Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.'
        
        >>> kyaah.sendMail(from_usr=sender, to_usr=receiver, svr=server, subject=subj, body=body, mail_passwd=passwd)

    Kyaah uses SSL for email, because most of the servers like gmail, require SSL.
"""

from datetime import datetime

__title__ = 'kyaah'
__version__ = '0.1.13'
__author__ = 'Usman Musa'
__author_email__ = 'usmanmusa1920@gmail.com'
__author_website__ = 'https://usmanmusa1920.github.io'
__repository__ = 'https://github.com/usmanmusa1920/kyaah'
__url__ = 'https://kyaah.readthedocs.io'
__license__ = 'MIT'
__copyright__ = f'Copyright (C) 2022 - {datetime.today().year} Usman Musa'
__description__ = 'Kyaah abstract away cognitive over-head of sending SMTP mail, together with other mailing operations things like, mail with file, tokens etc.'


status_codes = {
    # Information.
    200: ('success',),
    # Client Error.
    400: ('bad_request',),
    401: ('unauthorized',),
    404: ('not_found',),
    # Server Error.
    500: ('internal_server_error',),
    503: ('service_unavailable',),
}


def selector(env=None):
    """Decide a class for `environment variable` for security purpose or not."""

    if env:
        cls = Vault
    else:
        cls = BaseMail
    return cls


from .base import BaseMail
from .vault import Vault
from .utils import Tokens
from .utils import Faker
from .server import Serve
from .api import localMail
from .api import sendMail
from .api import sendImages
from .api import sendFiles
from .api import sendPage
from .api import fk
from .api import otp
from .api import fetch_mail_IMAP as fetch_imap
from .api import fetch_mail_POP as fetch_pop
