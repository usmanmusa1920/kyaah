:tocdepth: 2

Send page
#########

Kyaah provided **sendFiles** function for sending simple mail with page.

.. code-block:: python

    import kyaah

    sender = 'youremail@gmail.com'
    receiver = ['receiver_1@gmail.com', 'receiver_2@gmail.com']
    passwd = '*********' # use app password

    mail_serve = 'gmail'
    subj = f'Hellow world!'
    body = 'Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.'
    
    kyaah.sendPage(page='index.html', from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)

If you want to test, we provide you with a test feature which in short is to negate the `page` keyword argument like::

    kyaah.sendPage(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)

**FOR SECURITY REASON**

if you added your `email address` and `app password` in your system environment variable, include a keyword `env` to be `True`. And then put the variable name of your email address and email app password, instead of the raw email address and app password. See hint for this in your interpreter by calling the  '''help(Vault)''' class, enable `env` to be `True` in production instead of leaving the default which is `False` example::

    kyaah.sendPage(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd, env=True)
