:tocdepth: 2

Message accessing agent (POP3 and IMAP)
#######################################

POP3 `Post Office Protocol 3` and IMAP `Internet Message Access Protocol` both are MAA `Message accessing agent`, both of these protocols are used to retrieve messages from the mail server to the receivers system. Both of these protocols are accounted for spam and virus filters. IMAP is more flexible and complex than POP3.

`POP3` mail, it downloads the emails in the `inbox folder` on the email server to your device. This means that POP3 doesn't retrieve emails located in other folders such as `Sent, Draft, custom folders` and so on.

`IMAP`` mail, it enables us to take any action such as downloading, delete the mail without reading the mail. It enables us to create, manipulate and delete remote message folders called mail boxes. IMAP enables the users to search the e-mails. It allows concurrent access to multiple mailboxes on multiple mail servers.

Difference Between POP3 and IMAP:
---------------------------------

-   `POP3` POP is a simple protocol that only allows downloading messages from your Inbox to your local computer.
  -  `IMAP` IMAP (Internet Message Access Protocol) is much more advanced and allows the user to see all the folders on the mail server.

-   `POP3` The POP server listens on port 110, and the POP with SSL secure(POP3DS) server listens op    rt 995
  -  `IMAP` The IMAP server listens on port 143, and the IMAP with SSL secure(IMAPDS) server listens on port 993.

-   `POP3` In POP3 the mail can only be accessed from a single device at a time.
    `IMAP` Messages can be accessed across multiple devices

-   `POP3` To read the mail it has to be downloaded on the local system.
    `IMAP` The mail content can be read partially before downloading.

-   `POP3` The user can not organize mails in the mailbox of the mail server.
    `IMAP` The user can organize the emails directly on the mail server.

-   `POP3` The user can not create, delete or rename email on the mail server.
    `IMAP` The user can create, delete or rename an email on the mail server.

-   `POP3` It is unidirectional i.e. all the changes made on a device do not affect the content ps  nt on the server.
  -  `IMAP` It is Bi-directional i.e. all the changes made on the server or device are made on the other side too.

-   `POP3` It does not allow a user to sync emails.
    `IMAP` It allows a user to sync their emails.

-   `POP3` It is fast.
    `IMAP` It is slower as compared to POP3.

-   `POP3` A user can not search the content of mail before downloading it to the local system.
    `IMAP` A user can search the content of mail for a specific string before downloading.

-   `POP3` It has two modes: delete mode and keep mode. In delete mode, the mail is deleted from t  ailbox after retrieval. In keep mode, the mail remains in the mailbox after retrieval.
  -  `IMAP` Multiple redundant copies of the message are kept at the mail server, in case of loss of message of a local server, the mail can still be retrieved

-   `POP3` Changes in the mail can be done using local email software.
    `IMAP` Changes made to the web interface or email software stay in sync with the server.

-   `POP3` All the messages are downloaded at once.
    `IMAP` The Message header can be viewed prior to downloading.


Kyaah with POP3
---------------

Simple usage of kyaah with POP3. The `fetch` method it return a list of the available mails.

.. code-block:: python

    from kyaah import fetch

    creds = dict(sender="myemail@gmail.com", password="**********")

    f = fetch(credentials=creds)
    r = f.fetch()
    print(r)

In other to get message count and mailbox size, the below should be use. The `count` method result is tuple of 2 ints (message count, mailbox size).

.. code-block:: python
    
    r = f.count()
    print(r)


Kyaah with IMAP
---------------

Simple usage of kyaah with IMAP. The `folder` method it return list of mail folders.

.. code-block:: python

    from kyaah import fetch

    creds = dict(sender="myemail@gmail.com", password="**********")

    f = fetch(maa="imap", credentials=creds)
    r = f.folder()
    print(r)

By default it will seach the `Inbox` folder, but you can assign a different folder of your choice, by passing a key-word argument of `folder` in the method and give the folder name. NOTE: when pass folder name like `[Gmail]/All Mail` ensure to wrapp it with double qoute "" to avoid error, like `folder='"[Gmail]/All Mail"'` Below are some examples:

.. code-block:: python

    r = f.fetch(folder='Inbox', query='SUBJECT "Kyaah subject of testing"')
    r = f.fetch(folder="INBOX")
    r = f.fetch(folder="Trash")
    r = f.fetch(folder='"[Gmail]/All Mail"')
    r = f.fetch(folder='"[Gmail]/Drafts"')
    r = f.fetch(folder='"[Gmail]/Important"')
    r = f.fetch(folder='"[Gmail]/Sent Mail"')
    r = f.fetch(folder='"[Gmail]/Spam"')
    r = f.fetch(folder='"[Gmail]/Starred"')
    r = f.fetch(folder='"[Gmail]/Trash"')

Also a query for a specific mail `subject`, `date` can be, by passing a key-word of `query` in the method and specify what to query, by default it will query all. Example:

To get for specific mails by sender:

.. code-block:: python

    query='FROM "googlealerts-noreply@google.com"'

To get mails by subject:

.. code-block:: python
    
    query='SUBJECT "Thanks for Subscribing to our Newsletter !"'

To get mails after a specific date:

.. code-block:: python
    
    query='SINCE "01-JAN-2020"'

To get mails before a specific date:

.. code-block:: python
    
    query='BEFORE "01-JAN-2020"'

To create a folder with kyaah use the `create` method.

.. code-block:: python

    f.create('mynewfolder')

To rename a folder with kyaah use the `rename` method.

.. code-block:: python

    f.rename('mynewfolder', 'myrecentnewfolder')

To delete a folder with kyaah use the `delete` method.

.. code-block:: python
    
    f.delete('myrecentnewfolder')
