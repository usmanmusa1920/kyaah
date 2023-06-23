:tocdepth: 2

Local mail
##########

Kyaah provided **localMail** function, to test your mail locally. First boot up the python mail server on a different terminal by::

  python -m smtpd -c DebuggingServer -n localhost:1025

and then open another terminal and run your python script including the below code in it

.. code-block:: python

  import kyaah

  sender = 'youremail@gmail.com'
  receiver = ['receiver_1@gmail.com', 'receiver_2@gmail.com']
  passwd = '*********' # use app password

  mail_serve = 'local'
  subj = f'Hellow world!'
  body = 'Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.'

  kyaah.localMail(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)

Different port
==============

if you want to boot up the python mail server with a different port, not `1025`, in our case we will boot it now on port **7000**, is like to do:

.. code-block:: python

  python -m smtpd -c DebuggingServer -n localhost:7000

After that, pass a keyword argument of `port` with the port number as the value in the `localMail` function, like::

  kyaah.localMail(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd, port=7000)

**FOR SECURITY REASON**

if you added your `email address` and `app password` in your system environment variable, include a keyword `env` to be `True`. And then put the variable name of your email address and email app password, instead of the raw email address and app password. See hint for this in your interpreter by calling the  '''help(Vault)''' class, enable `env` to be `True` in production instead of leaving the default which is `False` example::

  kyaah.localMail(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd, port=7000, env=True)
