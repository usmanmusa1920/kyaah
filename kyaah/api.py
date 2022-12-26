
from . import Serve
from . import BaseMail
from . import Vault


def send():
  pass


def sendMail(svr=None, env=False, **kwargs):
  r"""send a simple SMTP mail
  :svr: this is the type of the sender mail, for google -> gmail, for yahoo -> yahoo, etc
  
  USAGE:

    >>> import kyaah
    >>> kyaah.sendMail(
          from_usr="sender@gmail.com", to_usr=["receiver_1@mail.com"],
          svr="gmail", subject="Hello world", body="lorem lip sum dolor!",
          mail_passwd="********")
  """

  s_mail = Serve.mail(svr)
  if env:
    cls = Vault
  else:
    cls = BaseMail
  base = cls(
    # slicing the first index of the server list, even though it's only one item
    server = s_mail["server"][0], **kwargs
    )
  # slicing the first index of the port list, even though it's only one item
  base.send_mail(port=s_mail["port"][0])
  

def sendImages(images=None, env=False, svr=None, **kwargs):
  """send simple mail with image(s)"""
  s_mail = Serve.mail(svr)
  if env:
    cls = Vault
  else:
    cls = BaseMail
  base = cls(
      # slicing the first index of the server list, even though it's only one item
      server = s_mail["server"][0], **kwargs
      )
  # slicing the first index of the port list, even though it's only one item
  base.mail_with_image(images, port=s_mail["port"][0])
  

def sendFiles(files=None, env=False, svr=None, **kwargs):
  """send simple mail with file(s)"""
  s_mail = Serve.mail(svr)
  if env:
    cls = Vault
  else:
    cls = BaseMail
  base = cls(
      # slicing the first index of the server list, even though it's only one item
      server = s_mail["server"][0], **kwargs
      )
  # slicing the first index of the port list, even though it's only one item
  base.mail_with_file(files, port=s_mail["port"][0])
  

def sendPage(page='default', env=False, svr=None, **kwargs):
  """send simple mail with page"""
  s_mail = Serve.mail(svr)
  if env:
    cls = Vault
  else:
    cls = BaseMail
  base = cls(
      # slicing the first index of the server list, even though it's only one item
      server = s_mail["server"][0], **kwargs
      )
  # slicing the first index of the port list, even though it's only one item
  base.mail_with_page(file=page, port=s_mail["port"][0])
