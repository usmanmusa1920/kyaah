
from . import Serve
from . import BaseMail


def send():
  pass


def sendMail(_from=None, _to=None, svr=None, _subj=None, _body=None, passwd=None):
  """send simple mail"""
  SS = Serve.mail(svr)
  base = BaseMail(
      from_usr = _from,
      mail_passwd = passwd,
      to_usr = _to,
      subject = _subj,
      body = _body,
      # slicing the first index of the server list, even though it's only one item
      server = SS["server"][0],
      )
  # slicing the first index of the port list, even though it's only one item
  base.send_mail(port=SS["port"][0])


def sendImages(f=None, _from=None, _to=None, svr=None, _subj=None, _body=None, passwd=None):
  """send simple mail with image(s)"""
  SS = Serve.mail(svr)
  base = BaseMail(
      from_usr = _from,
      mail_passwd = passwd,
      to_usr = _to,
      subject = _subj,
      body = _body,
      # slicing the first index of the server list, even though it's only one item
      server = SS["server"][0],
      )
  # slicing the first index of the port list, even though it's only one item
  base.mail_with_image(f, port=SS["port"][0])


def sendFiles(f=None, _from=None, _to=None, svr=None, _subj=None, _body=None, passwd=None):
  """send simple mail with file(s)"""
  SS = Serve.mail(svr)
  base = BaseMail(
      from_usr = _from,
      mail_passwd = passwd,
      to_usr = _to,
      subject = _subj,
      body = _body,
      # slicing the first index of the server list, even though it's only one item
      server = SS["server"][0],
      )
  # slicing the first index of the port list, even though it's only one item
  base.mail_with_file(f, port=SS["port"][0])


def sendPage(f='default', _from=None, _to=None, svr=None, _subj=None, _body=None, passwd=None):
  """send simple mail with page"""
  SS = Serve.mail(svr)
  base = BaseMail(
      from_usr = _from,
      mail_passwd = passwd,
      to_usr = _to,
      subject = _subj,
      body = _body,
      # slicing the first index of the server list, even though it's only one item
      server = SS["server"][0],
      )
  # slicing the first index of the port list, even though it's only one item
  base.mail_with_page(file=f, port=SS["port"][0])
