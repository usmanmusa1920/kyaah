
"""
        #    #   #   #    ##      ##    #    #
        #   #     # #    #  #    #  #   #    #
        ####       #    #    #  #    #  ######
        #  #       #    ######  ######  #    #
        #   #      #    #    #  #    #  #    #
        #    #     #    #    #  #    #  #    #

        Kyaah abstract away SMTP mail operations

        Simplify your email message with `kyaah`

        Usage at a glance:
        
            >>> import kyaah
            
            >>>    sender = "my_email@gmail.com"
            >>>    receiver = ["receiver_1@gmail.com", "receiver_2@gmail.com"]
            >>>    passwd = "*********"

            >>>    server = "gmail"
            >>>    subj = f"Hellow world!"
            >>>    body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt."

            >>> kyaah.sendMail(
                    from_usr=sender, to_usr=receiver, svr=server, subject=subj, body=body, mail_passwd=passwd)
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
