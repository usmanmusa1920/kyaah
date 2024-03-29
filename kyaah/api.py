# -*- coding: utf-8 -*-
from . import Serve
from . import Faker
from . import Tokens
from . import selector
from rgbpy import log_style
from .base import LOGGER, FetchPOP, FetchIMAP


def send():
    """
    This function can be use for any kind of mail operation, being it, simple mail, attach file for a mail, attach html page with mail, attach image file, etc.
    """
    pass


def localMail(svr=None, env=False, port=False, **kwargs):
    r"""
    To test your mail locally, first boot up the python mail server on a different terminal by:
        `python3 -m smtpd -c DebuggingServer -n localhost:1025`
    and then open another terminal and run your python script including the below code in it:

    Usage:
        >>> import kyaah
        >>> sender = 'youremail@gmail.com'
        >>> receiver = ['receiver_1@gmail.com', 'receiver_2@gmail.com']
        >>> passwd = '*********' # use app password
        >>> mail_serve = 'local'
        >>> subj = f'Hellow world!'
        >>> body = 'Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.'
        
        >>> kyaah.localMail(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
    """

    s_mail = Serve.mail(svr)
    cls = selector(env=env)

    base = cls(
        # slicing the first index of the server list, even though it's only one item
        server = s_mail['server'][0], **kwargs
        )
    
    # slicing the first index of the port list, even though it's only one item
    if port:
        base.local_mail(port=port)
    else:
        base.local_mail()


def sendMail(svr=None, env=False, **kwargs):
    r"""
    Send a simple SMTP mail
    :svr: this is the type of the sender mail, for google -> gmail, for yahoo -> yahoo, etc

    Usage:
        >>> import kyaah
        >>> sender = 'youremail@gmail.com'
        >>> receiver = ['receiver_1@gmail.com', 'receiver_2@gmail.com']
        >>> passwd = '*********' # use app password
        >>> mail_serve = 'gmail'
        >>> subj = f'Hellow world!'
        >>> body = 'Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.'

        >>> kyaah.sendMail(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
    """
    
    s_mail = Serve.mail(svr)
    cls = selector(env=env)

    base = cls(
        # slicing the first index of the server list, even though it's only one item
        server = s_mail['server'][0], **kwargs
        )
    
    # slicing the first index of the port list, even though it's only one item
    base.send_mail(port=s_mail['port'][0])


def sendImages(images=None, env=False, svr=None, **kwargs):
    r"""
    Send simple mail with image(s)

    Usage:
        >>> import kyaah
        >>> sender = 'youremail@gmail.com'
        >>> receiver = ['receiver_1@gmail.com', 'receiver_2@gmail.com']
        >>> passwd = '*********' # use app password
        >>> mail_serve = 'gmail'
        >>> subj = f'Hellow world!'
        >>> body = 'Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.'
        >>> images='my_image.jpg'

        >>> kyaah.sendImages(images=images, from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
    """

    s_mail = Serve.mail(svr)
    cls = selector(env=env)

    base = cls(
        # slicing the first index of the server list, even though it's only one item
        server = s_mail['server'][0], **kwargs
        )
    
    # slicing the first index of the port list, even though it's only one item
    base.mail_with_image(images, port=s_mail['port'][0])


def sendFiles(files=None, env=False, svr=None, **kwargs):
    r"""
    Send simple mail with file(s)

    Usage:
        >>> import kyaah
        >>> sender = 'youremail@gmail.com'
        >>> receiver = ['receiver_1@gmail.com', 'receiver_2@gmail.com']
        >>> passwd = '*********' # use app password
        >>> mail_serve = 'gmail'
        >>> subj = f'Hellow world!'
        >>> body = 'Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.'
        >>> files=['em.py', 'test.py', '/home/usman/Desktop/media/Usman.jpg']

        >>> kyaah.sendFiles(files=files, from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
    """

    s_mail = Serve.mail(svr)
    cls = selector(env=env)

    base = cls(
        # slicing the first index of the server list, even though it's only one item
        server = s_mail['server'][0], **kwargs
        )
    
    # slicing the first index of the port list, even though it's only one item
    base.mail_with_file(files, port=s_mail['port'][0])


def sendPage(page='default', env=False, svr=None, **kwargs):
    r"""
    Send simple mail with page
    
    Usage:
        >>> import kyaah
        >>> sender = 'youremail@gmail.com'
        >>> receiver = ['receiver_1@gmail.com', 'receiver_2@gmail.com']
        >>> passwd = '*********' # use app password
        >>> mail_serve = 'gmail'
        >>> subj = f'Hellow world!'
        >>> body = 'Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.'
        
        >>> kyaah.sendPage(page='index.html', from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)
    """

    s_mail = Serve.mail(svr)
    cls = selector(env=env)

    base = cls(
        # slicing the first index of the server list, even though it's only one item
        server = s_mail['server'][0], **kwargs
        )
    
    # slicing the first index of the port list, even though it's only one item
    base.mail_with_page(file=page, port=s_mail['port'][0])


def fetch(): ...


def fetch_mail_POP(sender, passwd, svr=None, **kwargs):
    r"""
    Fetch mail (POP)

    :svr: this is the type of the sender mail, for google => gmail, for yahoo => yahoo, etc
    #:svr => this is your mail server, if you are using:
        #:yahoo put yahoo,
        #:gmail put gmail
        #:outlook put outlook

    Usage:
        >>> import kyaah

        >>> sender = 'youremail@gmail.com'
        >>> passwd = '*********' # use app password

        >>> f = kyaah.fetch_pop(sender, passwd, 'gmail')

        >>> f.folder()
        >>> f.folder(see=True)
        >>> f.folder(see=True, folder='"[Gmail]/All Mail"')
        >>> f.folder(see=True, folder='"[Imap]/Trash"')
        
        >>> f.fetch('Inbox')
    """

    f = FetchPOP(sender, passwd, svr, **kwargs)
    return f


def fetch_mail_IMAP(sender, passwd, svr=None, **kwargs):
    r"""
    Fetch mail (IMAP)

    :svr: this is the type of the sender mail, for google => gmail, for yahoo => yahoo, etc
    #:svr => this is your mail server, if you are using:
        #:yahoo put yahoo,
        #:gmail put gmail
        #:outlook put outlook

    Usage:
        >>> import kyaah

        >>> sender = 'youremail@gmail.com'
        >>> passwd = '*********' # use app password

        >>> f = kyaah.fetch_imap(sender, passwd, 'gmail')

        >>> f.folder()
        >>> f.folder(see=True)
        >>> f.folder(see=True, folder='"[Gmail]/All Mail"')
        >>> f.folder(see=True, folder='"[Imap]/Trash"')
        
        >>> f.fetch('Inbox')
    """

    f = FetchIMAP(sender, passwd, svr, **kwargs)
    return f


def fk(style: False / True = True):
    """This function generate a random email address for you."""

    if style == False:
        LOGGER.info(Faker().faker())
    else:
        log_style(Faker().faker())


def otp(_range=False):
    """This function give you a random OTP code."""

    if _range:
        return Tokens().mail_otp(_range)
    return Tokens().mail_otp()
