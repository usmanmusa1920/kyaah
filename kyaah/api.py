
import logging
from . import Serve
from . import Faker
from . import Tokens
from . import selector


def send():
  """this function can be use for any kind of mail operation, being it,
  simple mail, attach file for a mail, attach html page with mail,
  attach image file, etc
  """
  pass


def localMail(svr=None, env=False, port=False, **kwargs):
  r"""To tests your mail locally, boot up the python mail server on a different terminal by:
        `python3 -m smtpd -c DebuggingServer -n localhost:1025`
    and then open another terminal and run your python script including the below code in it:

    USAGE:
      >>> import kyaah
      >>> sender = "youremail@gmail.com"
      >>> receiver = ["receiver_1@gmail.com", "receiver_2@gmail.com"]
      >>> passwd = "*********"
      >>> mail_serve = "local"
      >>> subj = f"Hellow world!"
      >>> body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt."
      
      >>> kyaah.localMail(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
    -----------------------------------------------------------------------------------
    if you want to boot up the python mail server with a different port, not `1025`, is like:
      `python3 -m smtpd -c DebuggingServer -n localhost:7000`

      After that, pass a keyword argument of `port` with the port number as the value in the `localMail` function.
      >>> kyaah.localMail(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd, port=7000)
    -----------------------------------------------------------------------------------
    FOR SECURITY REASON
      if you added your `email address` and `app password` in your system environment variable, include a keyword `env` to be `True`. And then put the variable name of your email address and email app password, instead of the raw email address and app password. See hint for this in your interpreter by calling the  '''help(Vault)''' class, enable `env` to be `True` in production instead of leaving the default which is `False` example:

      >>> kyaah.localMail(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd, port=7000, env=True)
  """

  s_mail = Serve.mail(svr)
  cls = selector(env=env)
  base = cls(
    # slicing the first index of the server list, even though it's only one item
    server = s_mail["server"][0], **kwargs
    )
  # slicing the first index of the port list, even though it's only one item
  if port:
    base.local_mail(port=port)
  else:
    base.local_mail()


def sendMail(svr=None, env=False, **kwargs):
  r"""send a simple SMTP mail
  :svr: this is the type of the sender mail, for google -> gmail, for yahoo -> yahoo, etc

  USAGE:
    >>> import kyaah
    >>> sender = "youremail@gmail.com"
    >>> receiver = ["receiver_1@gmail.com", "receiver_2@gmail.com"]
    >>> passwd = "*********"
    >>> mail_serve = "gmail"
    >>> subj = f"Hellow world!"
    >>> body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt."

    >>> kyaah.sendMail(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
  -----------------------------------------------------------------------------------
  FOR SECURITY REASON
    if you added your `email address` and `app password` in your system environment variable, include a keyword `env` to be `True`. And then put the variable name of your email address and email app password, instead of the raw email address and app password. See hint for this in your interpreter by calling the  '''help(Vault)''' class, enable `env` to be `True` in production instead of leaving the default which is `False` example:
      
    >>> kyaah.sendMail(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd, env=True)
  """

  s_mail = Serve.mail(svr)
  cls = selector(env=env)
  base = cls(
    # slicing the first index of the server list, even though it's only one item
    server = s_mail["server"][0], **kwargs
    )
  # slicing the first index of the port list, even though it's only one item
  base.send_mail(port=s_mail["port"][0])
  

def sendImages(images=None, env=False, svr=None, **kwargs):
  r"""send simple mail with image(s)

  USAGE:
    >>> import kyaah
    >>> sender = "youremail@gmail.com"
    >>> receiver = ["receiver_1@gmail.com", "receiver_2@gmail.com"]
    >>> passwd = "*********"
    >>> mail_serve = "gmail"
    >>> subj = f"Hellow world!"
    >>> body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt."
    >>> images="my_image.jpg"

    >>> kyaah.sendImages(images=images, from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
    -----------------------------------------------------------------------------------
    If you want to send more than one image, make a list of the images like:

    >>> images=['image_1.jpg', 'image_2.jpg']
    >>> kyaah.sendImages(images=images, from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
  -----------------------------------------------------------------------------------
  FOR SECURITY REASON
    if you added your `email address` and `app password` in your system environment variable, include a keyword `env` to be `True`. And then put the variable name of your email address and email app password, instead of the raw email address and app password. See hint for this in your interpreter by calling the  '''help(Vault)''' class, enable `env` to be `True` in production instead of leaving the default which is `False` example:
      
    >>> images=['image_1.jpg', 'image_2.jpg']
    >>> kyaah.sendImages(images=images, from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd, env=True)
  """
  s_mail = Serve.mail(svr)
  cls = selector(env=env)
  base = cls(
      # slicing the first index of the server list, even though it's only one item
      server = s_mail["server"][0], **kwargs
      )
  # slicing the first index of the port list, even though it's only one item
  base.mail_with_image(images, port=s_mail["port"][0])
  

def sendFiles(files=None, env=False, svr=None, **kwargs):
  r"""send simple mail with file(s)

  USAGE:
    >>> import kyaah
    >>> sender = "youremail@gmail.com"
    >>> receiver = ["receiver_1@gmail.com", "receiver_2@gmail.com"]
    >>> passwd = "*********"
    >>> mail_serve = "gmail"
    >>> subj = f"Hellow world!"
    >>> body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt."
    >>> files=['em.py', 'test.py', '/home/usman/Desktop/media/Usman.jpg']

    >>> kyaah.sendFiles(files=files, from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
  -----------------------------------------------------------------------------------
  FOR SECURITY REASON
    if you added your `email address` and `app password` in your system environment variable, include a keyword `env` to be `True`. And then put the variable name of your email address and email app password, instead of the raw email address and app password. See hint for this in your interpreter by calling the  '''help(Vault)''' class, enable `env` to be `True` in production instead of leaving the default which is `False` example:
      
    >>> kyaah.sendFiles(files=files, from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd, env=True)
  """
  s_mail = Serve.mail(svr)
  cls = selector(env=env)
  base = cls(
      # slicing the first index of the server list, even though it's only one item
      server = s_mail["server"][0], **kwargs
      )
  # slicing the first index of the port list, even though it's only one item
  base.mail_with_file(files, port=s_mail["port"][0])
  

def sendPage(page='default', env=False, svr=None, **kwargs):
  r"""send simple mail with page
  
  USAGE:
    >>> import kyaah
    >>> sender = "youremail@gmail.com"
    >>> receiver = ["receiver_1@gmail.com", "receiver_2@gmail.com"]
    >>> passwd = "*********"
    >>> mail_serve = "gmail"
    >>> subj = f"Hellow world!"
    >>> body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt."
    
    >>> kyaah.sendPage(page='index.html', from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
    -----------------------------------------------------------------------------------
    If you want to test, we provide you with a test feature which in short is to negate the `page` keyword argument like:

    >>> kyaah.sendPage(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
  -----------------------------------------------------------------------------------
  FOR SECURITY REASON
    if you added your `email address` and `app password` in your system environment variable, include a keyword `env` to be `True`. And then put the variable name of your email address and email app password, instead of the raw email address and app password. See hint for this in your interpreter by calling the  '''help(Vault)''' class, enable `env` to be `True` in production instead of leaving the default which is `False` example:
      
    >>> kyaah.sendPage(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd, env=True)
  """
  s_mail = Serve.mail(svr)
  cls = selector(env=env)
  base = cls(
      # slicing the first index of the server list, even though it's only one item
      server = s_mail["server"][0], **kwargs
      )
  # slicing the first index of the port list, even though it's only one item
  base.mail_with_page(file=page, port=s_mail["port"][0])


def fk():
  r"""this function generate a random email address for you"""
  formatter = "[+] [%(asctime)s] [%(levelname)s] %(message)s"
  logging.basicConfig(format = formatter)
  logger = logging.getLogger()
  logger.setLevel(logging.DEBUG)
  logger.info(Faker().faker())


def otp(_range=False):
  r"""this function give you a random OTP code"""
  if _range:
    return Tokens().mail_otp(_range)
  return Tokens().mail_otp()
