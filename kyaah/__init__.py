
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
      NOTE:
          in all `BaseMail` mathod there is a keyword argument called `port`, that port is the port of your SMTP server which will listen, make sure to put the port that is convenient to your SMTP server e.g for gmail is 465
          
          
      To tests your mail locally, boot up the python mail server on a different terminal by:
      $:/~    `python3 -m smtpd -c DebuggingServer -n localhost:7000`
          
      and then open another terminal and run your python script including the below code in it:
      >>>    import 
      >>>    subj = f"Hellow world!"
      >>>    body = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum voluptate ipsum voluptatum doloribus, incidunt totam doloremque."
      
      >>>    kyaah.localMail(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
      ------------------------------------------------------------------------------------------------------
      To send a text mail to someone:
          
      >>>    import kyaah
      >>>    subj = f"Hellow world!"
      >>>    body = "Lorem ipsum dolor sit amet consectetur adipisicing elit, rerum voluptate ipsum volupt."
      
      >>>    kyaah.sendMail(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
      ------------------------------------------------------------------------------------------------------
      To send a text mail together with an image:
      >>>    import kyaah
      >>>    subj = f"Hellow world!"
      >>>    body = "Lorem ipsum dolor sit amet consectetur adipisicing elit, rerum voluptate ipsum volupt."
      
      >>>    images="my_image.jpg"
      >>>    kyaah.sendImages(images=images, from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
          
      If you want to send more than one image, make a list of the images like:
      >>>    images=['image_1.jpg', 'image_2.jpg']
      >>>    kyaah.sendImages(images=images, from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
      ------------------------------------------------------------------------------------------------------
      To send mail together with files, pass a list of the files you want to send as an argument in the `mail_with_file` method like:
      >>>    import kyaah
      >>>    subj = f"Hellow world!"
      >>>    body = "Lorem ipsum dolor sit amet consectetur adipisicing elit, rerum voluptate ipsum volupt."
      
      >>>    files=['em.py', 'test.py', '/home/usman/Desktop/media/Usman.jpg']
      >>>    kyaah.sendFiles(files=files, from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
      ------------------------------------------------------------------------------------------------------
      To send mail together with html page call the `mail_with_page` method and pass a keyword args `file` with a value of the absolute location of your html file in the `mail_with_page` method, like:
      
      >>>    import kyaah
      >>>    subj = f"Hellow world!"
      >>>    body = "Lorem ipsum dolor sit amet consectetur adipisicing elit, rerum voluptate ipsum volupt."
      
      >>>    kyaah.sendPage(page='index.html', from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
      
      If you want to test, we provide you with a test feature which in short is to negate the `page` keyword argument like:
      >>>    kyaah.sendPage(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
      ------------------------------------------------------------------------------------------------------
      
  ####   ######   ####   #    #  #####      #     #####   #   #
 #       #       #    #  #    #  #    #     #       #      # #
  ####   #####   #       #    #  #    #     #       #       #
      #  #       #       #    #  #####      #       #       #
 #    #  #       #    #  #    #  #   #      #       #       #
  ####   ######   ####    ####   #    #     #       #       #
      
      FOR SECURITY REASON
      we provide you a keyword called `env` to be true. This keyword will look your email address and password/app_password in your sysytem environment variable. And you don't need to change anything in your code, all the mothods is thesame. Look more for this class in your interpreter by calling the  '''help(Vault)'''  Use this class in production instead of the  '''BaseMail'''  class. example:
      
      >>>    import kyaah
      >>>    subj = f"Hellow world!"
      >>>    body = "Lorem ipsum dolor sit amet consectetur adipisicing elit, rerum voluptate ipsum volupt."
      
      >>>    kyaah.sendMail(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd, env=True)
      ------------------------------------------------------------------------------------------------------
      
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
