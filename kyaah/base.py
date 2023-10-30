# -*- coding: utf-8 -*-
"""
# ============
# Kyaah @ base
# ============
"""

import os
import sys
import time
import imghdr
import poplib
import pprint
import logging
import smtplib
import imaplib
import email.utils
import email.policy
from email.message import EmailMessage
from pstyle import log_style
from .server import Serve

# """
# NOTSET    ---  0
# DEBUG     ---  10
# INFO      ---  20
# WARNING   ---  30  (default)
# ERROR     ---  40
# CRITICAL  ---  50
# """

FORMATTER = '[+] [%(asctime)s] [%(levelname)s] %(message)s'
logging.basicConfig(format=FORMATTER)
LOGGER = logging.getLogger()  # Creating an object
LOGGER.setLevel(logging.DEBUG)  # Setting the threshold of LOGGER to DEBUG
# platform-specific path separator (for linux `/`, for windows `\\`)
OS_SEP = os.path.sep


def ok(msg):
    """Email is ok"""
    print(msg + ' ', end='', flush=True)
    num = 0
    for _ in range(3):
        num += 1
        time.sleep(0.3)
        print('.', end='', flush=True)
    print(' OK')
    time.sleep(1)


class BaseMail:
    """
    Base class for mail
    NOTE:
        in all `BaseMail` mathod there is a keyword argument called `port`, that port is the port of your SMTP server which will listen, make sure to put the port that is convenient to your SMTP server e.g for gmail is 465 (SSL), although kyaah has a dictionary of server, where each server has a list of ports, SMTP server, etc.

        Kyaah uses SSL for email, because most of the servers like gmail, require SSL.
    """

    def __init__(
        self,
        from_usr=None,
        to_usr=None,
        subject=None,
        body=None,
        mail_passwd=None,
        server=None,
    ):
        """
        For iCloud, the username is typically the first part of your email address, for example, my_email, rather than my_email@icloud.com. If your email client cannot connect to iCloud while using only the name portion of your address, try using the full address as a test
        """

        self.from_usr = from_usr
        self.to_usr = to_usr
        self.subject = subject
        self.body = body
        self.mail_passwd = mail_passwd
        self.server = server

        while self.from_usr == None:
            raise UnboundLocalError(f'`from_usr` is required')
        while self.to_usr == None:
            raise UnboundLocalError(f'`to_usr` is required')

    @property
    def from_usr_addr(self):
        """The sender mail address"""
        return self.from_usr

    @property
    def mail_passwd_env(self):
        """The sender mail password"""
        return self.mail_passwd

    @property
    def mail_msg(self):
        """Content of the mail (subject and message body)"""
        subj = self.subject
        body = self.body
        data = f'Subject: {subj}\n\n{body}'
        return data

    def check_required(self):
        """Checking for required values"""
        while self.mail_passwd == None:
            raise UnboundLocalError(f'`mail_passwd` is required')
        while self.server == None:
            raise UnboundLocalError(f'`server` is required')

    def mail_head(self, msg):
        """Contains the sender, receiver and subject"""
        # grab the subject from `mail_msg` method by spliting it,
        # and grab the first index which is the subject,
        # then we slice the first index from index `9` that mean we negate
        # `subj` variable of mail_msg method of this class
        # which is `Subject: `

        msg['From'] = self.from_usr_addr
        # The From field indicates the sender’s address i.e. who sent the e-mail.

        msg['To'] = self.to_usr
        # The To field indicates the recipient’s address i.e. to whom the e-mail is sent.

        msg['Subject'] = self.mail_msg.split('\n')[0][9:]
        # The Subject field indicates the purpose of e-mail. It should be precise and to the point.

        msg['Date'] = email.utils.formatdate(localtime=True)
        # The Date field indicates the date when the e-mail was sent.

        msg['Message-ID'] = email.utils.make_msgid()
        
        # CC (Carbon copy). It includes those recipient addresses whom we want to keep informed but not exactly the intended recipient.
        
        # BCC (Black Carbon Copy). It is used when we do not want one or more of the recipients to know that someone else was copied on the message.
        
        # Greeting is the opening of the actual message. Eg. Hi Sir or Hi Guys etc.

        # Text it represents the actual content of the message.

        # Signature is the final part of an e-mail message. It includes Name of Sender, Address, and Contact Number.

        # Python has EmailMessage class which can be used build email messages. This class ahs the required methods to customize different parts of the email message like - the TO and FROM tags, the Subject Line as well as the content of the email.

        # sys.stdout.buffer.write(msg.as_bytes())

    def mail_open(self, msg, port):
        """
        This open the connection, and login to email address using email address provided together with password/app_password
        """
        with smtplib.SMTP_SSL(self.server, port) as smtp:
            smtp.login(self.from_usr_addr, self.mail_passwd_env)
            smtp.send_message(msg)

    def local_mail(self, port=1025):
        """Localhost mail"""
        with smtplib.SMTP(self.server, port) as smtp:
            smtp.sendmail(self.from_usr_addr, self.to_usr, self.mail_msg)

    def send_mail(self, port=25):
        """Send mail with ssl security"""
        # recepients is the list of receivers email address that you will send emaill address to, if the recepients is not included when call the method it will only send it to the `self.to_usr` that you pass in as the argument when instanciating the `BaseMail` class
        self.check_required()

        if len(self.to_usr) > 1:
            # if there is recepients
            for receiver in self.to_usr:
                with smtplib.SMTP_SSL(self.server, port) as smtp:
                    smtp.login(self.from_usr_addr, self.mail_passwd_env)
                    smtp.sendmail(self.from_usr_addr, receiver, self.mail_msg)
        elif len(self.to_usr) == 1:
            with smtplib.SMTP_SSL(self.server, port) as smtp:
                smtp.login(self.from_usr_addr, self.mail_passwd_env)
                smtp.sendmail(self.from_usr_addr, self.to_usr, self.mail_msg)

    def file_to_send(self, file_to, f_opration, _msg=None, maintype=None):
        """
        Kyaah file to send utility method, used for `mail_with_image` and `mail_with_file`
        """
        # maintype = 'image' for sending image
        # maintype = 'application' for sending files like pdf

        if maintype == 'application':
            with open(file_to, f_opration) as file_send:
                f_read = file_send.read()
                n = file_send.name
                if OS_SEP in n:
                    f_name = n.split(OS_SEP)[-1]
                else:
                    f_name = file_send.name
            _msg.add_attachment(
                f_read, maintype=maintype, subtype='octet-stream', filename=f_name)
        if maintype == 'image':
            with open(file_to, f_opration) as img_send:
                img_read = img_send.read()
                f_type = imghdr.what(img_send.name)
                n = img_send.name
                if OS_SEP in n:
                    f_name = n.split(OS_SEP)[-1]
                else:
                    f_name = img_send.name
            _msg.add_attachment(
                img_read, maintype=maintype, subtype=f_type, filename=f_name)

    def mail_with_image(self, image, port=25):
        """Send mail together with an image"""
        self.check_required()

        if len(self.to_usr) > 1:
            # if the list of to_usr is more than one
            for receiver in self.to_usr:
                msg = EmailMessage()
                msg['From'] = self.from_usr_addr
                msg['To'] = receiver
                msg['Subject'] = self.mail_msg.split('\n')[0][9:]
                msg['Date'] = email.utils.formatdate(localtime=True)
                msg['Message-ID'] = email.utils.make_msgid()
                msg.set_content(self.mail_msg.split('\n')[2])

                if type(image) == list:
                    # send message with more than one image
                    for my_img in image:
                        self.file_to_send(
                            my_img, 'rb', _msg=msg, maintype='image')
                    self.mail_open(msg, port)
                elif type(image) == str:
                    # send message with one image
                    self.file_to_send(image, 'rb', _msg=msg, maintype='image')
                    self.mail_open(msg, port)
                else:
                    LOGGER.error(
                        f'only list or string can be pass as argument in {self.mail_with_image}')
        elif len(self.to_usr) == 1:
            msg = EmailMessage()
            self.mail_head(msg)
            msg.set_content(self.mail_msg.split('\n')[2])

            if type(image) == list:
                # send message with more than one image, for only one destination
                for my_img in image:
                    self.file_to_send(my_img, 'rb', _msg=msg, maintype='image')
                self.mail_open(msg, port)
            elif type(image) == str:
                # send message with one image, for only one destination
                self.file_to_send(image, 'rb', _msg=msg, maintype='image')
                self.mail_open(msg, port)
            else:
                LOGGER.error(
                    f'only list or string can be pass as argument in {self.mail_with_image}')

    def mail_with_file(self, mail_files, port=25):
        """Send mail together with a list of mail_files"""
        self.check_required()

        msg = EmailMessage()
        self.mail_head(msg)
        msg.set_content(self.mail_msg.split('\n')[2])

        for a_file in mail_files:
            self.file_to_send(a_file, 'rb', _msg=msg, maintype='application')
        self.mail_open(msg, port)

    def mail_with_page(self, file=None, port=25):
        """
        Send mail with html page. You can pass a keyword args of `file='default'` which will send a default html page provided within this class method, that is for test.

        But if you want to send yor own html page assign the `file` with a value of the absolute location of your html page
        """

        self.check_required()

        msg = EmailMessage()
        self.mail_head(msg)
        msg.set_content(self.mail_msg.split('\n')[2])

        if file == 'default':
            dummy_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1 style="color:SlateGray;">Hello world mail from {self.from_usr_addr}</h1>
  <p style="color:brown;">Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum voluptate ipsum voluptatum doloribus, incidunt totam doloremque quae quibusdam exercitationem sapiente vel veritatis consequuntur earum et. Quod nobis minus minima repellat.</p>
</body>
</html>
'''
            msg.add_alternative(dummy_page, subtype='html')
        elif file != None:
            with open(file) as f_html:
                html_f = f_html.read()
                n = f_html.name
                if OS_SEP in n:
                    f_name = n.split(OS_SEP)[-1]
                else:
                    f_name = f_html.name
            msg.add_attachment(html_f, subtype='html', filename=f_name)
        self.mail_open(msg, port)


"""
POP3 (Post Office Protocol 3) and IMAP (Internet Message Access Protocol) both are MAA (Message accessing agent), both of these protocols are used to retrieve messages from the mail server to the receivers system. Both of these protocols are accounted for spam and virus filters. IMAP is more flexible and complex than POP3.

Difference Between POP3 and IMAP:

    POP3
        IMAP
    
    POP is a simple protocol that only allows downloading messages from your Inbox to your local computer.
        IMAP (Internet Message Access Protocol) is much more advanced and allows the user to see all the folders on the mail server.

    The POP server listens on port 110, and the POP with SSL secure(POP3DS) server listens on port 995
        The IMAP server listens on port 143, and the IMAP with SSL secure(IMAPDS) server listens on port 993.

    In POP3 the mail can only be accessed from a single device at a time.
        Messages can be accessed across multiple devices

    To read the mail it has to be downloaded on the local system.
        The mail content can be read partially before downloading.

    The user can not organize mails in the mailbox of the mail server.
        The user can organize the emails directly on the mail server.

    The user can not create, delete or rename email on the mail server.
        The user can create, delete or rename an email on the mail server.

    It is unidirectional i.e. all the changes made on a device do not affect the content present on the server.
        It is Bi-directional i.e. all the changes made on the server or device are made on the other side too.

    It does not allow a user to sync emails.
        It allows a user to sync their emails.

    It is fast.
        It is slower as compared to POP3.

    A user can not search the content of mail before downloading it to the local system.
        A user can search the content of mail for a specific string before downloading.

    It has two modes: delete mode and keep mode. In delete mode, the mail is deleted from the mailbox after retrieval. In keep mode, the mail remains in the mailbox after retrieval.
        Multiple redundant copies of the message are kept at the mail server, in case of loss of message of a local server, the mail can still be retrieved

    Changes in the mail can be done using local email software.
        Changes made to the web interface or email software stay in sync with the server.

    All the messages are downloaded at once.
        The Message header can be viewed prior to downloading.
"""

class FetchPOP:
    """
    Fetch POP mail

    Pyhton`s poplib module provides classes named pop() and pop3_SSL() which are used to achieve this requirement.

    1	LOGIN
    This command opens the connection.
    2	STAT
    It is used to display number of messages currently in the mailbox.
    3	LIST
    It is used to get the summary of messages where each message summary is shown.
    4	RETR
    This command helps to select a mailbox to access the messages.
    5	DELE
    It is used to delete a message.
    6	RSET
    It is used to reset the session to its initial state.
    7	QUIT
    It is used to log off the session.
    """

    def __init__(self, sender, passwd, svr):
        """Kyaah POP init"""
        self.sender = sender
        self.passwd = passwd
        self.svr = svr
        self.mail_box = None

    def conn(self):
        """
        Making connection
        """
        # s_mail = Serve.mail(self.svr)
        # # connect to host using SSL
        # imap = imaplib.IMAP4_SSL(s_mail['server'][2])
        # # login to server
        # imap.login(self.sender, self.passwd)
        # # return imap
        # self.imapp = imap
        s_mail = Serve.mail(self.svr)

        if s_mail['server'][1] == 'icloud':
            log_style('Not supported')
            raise PermissionError
        
        # Connect to the mail box
        mail_box = poplib.POP3_SSL(s_mail['server'][1], s_mail['port'][2])
        mail_box.user(self.sender)
        mail_box.pass_(self.passwd)
        self.mail_box = mail_box
        
    def count(self, n):
        """
        Fetch POP mail (count)
        :svr: this is the type of the sender mail, for google => gmail, for yahoo => yahoo, etc
        """

        # s_mail = Serve.mail(svr)
        
        # # Connect to the mail box
        # mail_box = poplib.POP3_SSL(s_mail['server'][1], s_mail['port'][2])
        # mail_box.user(sender)
        # mail_box.pass_(passwd)
        self.conn()
        NumofMessages = len(self.mail_box.list()[1])
        rr = range(1,NumofMessages+1)
        print(rr)
        if n not in rr:
            print('Out of range, range is {}'.format(range(1,NumofMessages+1)))
            exit()
        # print(self.mail_box.retr(n+1)[1])
        for msg in self.mail_box.retr(n+1)[1]:
            # print(msg.decode())
            print(msg)
            # print()
        # for i in range(NumofMessages):
        #     for msg in self.mail_box.retr(i+1)[1]:
        #         print(msg)
        #         print()
        # print(mail_box.retr(255)[1])
        print(self.mail_box.stat())
        self.mail_box.quit()
        
    def fetch(self):
        """
        Fetch POP mail
        :svr: this is the type of the sender mail, for google => gmail, for yahoo => yahoo, etc
        """

        # s_mail = Serve.mail(svr)
        
        # # Connect to the mail box
        # mail_box = poplib.POP3_SSL(s_mail['server'][1], s_mail['port'][2])
        # mail_box.user(sender)
        # mail_box.pass_(passwd)
        self.conn()
        NumofMessages = len(self.mail_box.list()[1])
        for i in range(NumofMessages):
            for msg in self.mail_box.retr(i+1)[1]:
                print(msg)
                print()
        # print(mail_box.retr(255)[1])
        print(self.mail_box.stat())
        self.mail_box.quit()


class FetchIMAP:
    """
    Fetch IMAP mail

    It enables us to take any action such as downloading, delete the mail without reading the mail.It enables us to create, manipulate and delete remote message folders called mail boxes.

    IMAP enables the users to search the e-mails.

    It allows concurrent access to multiple mailboxes on multiple mail servers.

    1	IMAP_LOGIN
    This command opens the connection.
    2	CAPABILITY
    This command requests for listing the capabilities that the server supports.
    3	NOOP
    This command is used as a periodic poll for new messages or message status updates during a period of inactivity.
    4	SELECT
    This command helps to select a mailbox to access the messages.
    5	EXAMINE
    It is same as SELECT command except no change to the mailbox is permitted.
    6	CREATE
    
    7	DELETE
    
    8	RENAME
    
    9	LOGOUT
    
    """

    def __init__(self, sender, passwd, svr):
        """Kyaah IMAP init"""
        self.sender = sender
        self.passwd = passwd
        self.svr = svr
        self.imapp = None

    def conn(self):
        """
        Making connection
        """
        s_mail = Serve.mail(self.svr)
        # connect to host using SSL
        imap = imaplib.IMAP4_SSL(s_mail['server'][2], s_mail['port'][2])
        # login to server
        imap.login(self.sender, self.passwd)
        self.imapp = imap

    def folder(self, folder: str='Inbox', see: bool = False) -> list:
        """
        Fetch IMAP mail folder
        
        :svr: this is the type of the sender mail, for google => gmail, for yahoo => yahoo, etc
        :see: if true, it will loop over the folders and display them on terminal

        it return list of mail folders
        """
        
        self.conn()
        s_status, b = self.imapp.select(folder)

        if s_status == 'OK':
            ok('Processing mailbox')
        else:
            print('ERROR: Unable to open mailbox ', s_status)
            sys.exit()

        if see:
            print('Folders:\n')
        _list_1 = self.imapp.list()
        _list_2 = []

        for f in _list_1[1]:
            a = f.decode().replace('\\', '')
            b = a.replace('"/"', '==>')
            if see:
                print(b)
                print()
            _list_2.append(b)
        return _list_2
    
    def fetch(self, folder: str='Inbox'):
        """
        Fetch IMAP mail
        :svr: this is the type of the sender mail, for google => gmail, for yahoo => yahoo, etc

        NOTE
            when pass folder name like:
                [Gmail]/All Mail
            ensure to wrapp it with double qoute "" like:
                folder='"[Gmail]/All Mail"'
            to avoid error
        """
        
        self.conn()
        s_status, b = self.imapp.select(folder)
        tmp, data = self.imapp.search(None, 'ALL')
        # status, messages = self.imapp.search(None, 'ALL')
        if tmp == 'OK':
            ok('Searching mailbox')
        else:
            print('ERROR: Unable to search mailbox ', tmp)
            sys.exit()

        # for i in data[0].split():
        #     print(i)
        #     print()
        print(len(data[0].split()))
        for num in data[0].split():
            tmp, data = self.imapp.fetch(num, '(RFC822)')
            # print(tmp)
            print()
            print('Message: {0}\n'.format(num))
            # pprint.pprint(data[0][1])
            # pprint.pprint(data)
            # print(data)
            for d in data[0][1].decode().split('\r\n'):
                print(d)
            print()
            print()
            print()
            if num == b'5': break
        self.imapp.close()

    def create(self, folder):
        """It is used to create mailbox with a specified name"""
        self.conn()
        self.imapp.create(folder)
        
    def rename(self, old_box, new_box):
        """It is used to change the name of a mailbox"""
        self.conn()
        self.imapp.rename(old_box, new_box)
        
    def delete(self, folder):
        """It is used to permanently delete a mailbox with a given name"""
        self.conn()
        self.imapp.delete(folder)
        
    def logout(self):
        """
        This command informs the server that client is done with the session. The server must send BYE untagged response before the OK response and then close the network connection
        """
        self.conn()
        self.imapp.logout()
