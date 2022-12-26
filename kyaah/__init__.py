# -*- coding: utf-8 -*-

#   __
#  /__)  _  _     _   _ _/   _
# / (   (- (/ (/ (- _)  /  _)
#          /
class mapp:
    pass
"""
Requests HTTP Library
~~~~~~~~~~~~~~~~~~~~~

Requests is an HTTP library, written in Python, for human beings.
Basic GET usage:

   >>> import requests
   >>> r = requests.get('https://www.python.org')
   >>> r.status_code
   200
   >>> b'Python is a programming language' in r.content
   True

... or POST:

   >>> payload = dict(key1='value1', key2='value2')
   >>> r = requests.post('https://httpbin.org/post', data=payload)
   >>> print(r.text)
   {
     ...
     "form": {
       "key1": "value1",
       "key2": "value2"
     },
     ...
   }

The other HTTP methods are supported - see `requests.api`. Full documentation
is at <https://requests.readthedocs.io>.

:copyright: (c) 2017 by Kenneth Reitz.
:license: Apache 2.0, see LICENSE for more details.
"""


"""
        #    #   #   #    ##      ##    #    #
        #   #     # #    #  #    #  #   #    #
        ####       #    #    #  #    #  ######
        #  #       #    ######  ######  #    #
        #   #      #    #    #  #    #  #    #
        #    #     #    #    #  #    #  #    #

        Simplify your email message with `kyaah`
"""

__title__ = "kyaah"
__author__ = "Usman Musa"
__author_email__ = "usmanmusa1920@gmail.com"
__author_website__ = "https://usmanmusa1920.github.io"
__copyright__ = "Copyright 2022 Usman Musa"


"""
      
  #####   ####   #    #  ######  #    #   ####
    #    #    #  #   #   #       ##   #  #
    #    #    #  ####    #####   # #  #   ####
    #    #    #  #  #    #       #  # #       #
    #    #    #  #   #   #       #   ##  #    #
    #     ####   #    #  ######  #    #   ####
    
      There is a OTP code feature if you want to send an OTP code for verification by:
      >>>  from kyaah import Tokens
      >>>  otp_code = Tokens.mail_otp()
      636937
      
      You can also specify the length of numbers you want by passing a key argument of `_range` in the method like:
      >>>  otp_code = Tokens.mail_otp(_range = 10)
      5373593635
      ------------------------------------------------------------------------------------------------------
      Use `Faker` class for giving you random email address
      
      >>>  import logging
      >>>  from kyaah import Faker
      
      >>>  formatter = "[+] [%(asctime)s] [%(levelname)s] %(message)s"
      >>>  logging.basicConfig(format = formatter)

      >>>  logger = logging.getLogger()
      >>>  logger.setLevel(logging.DEBUG)
      
      >>>  logger.info(Faker().faker())
      ------------------------------------------------------------------------------------------------------
"""

from . base import BaseMail
from . vault import Vault

from . utils import Tokens
from . utils import Faker
from . server import Serve

from . api import localMail
from . api import sendMail
from . api import sendImages
from . api import sendFiles
from . api import sendPage
