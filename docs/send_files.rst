:tocdepth: 2

Send files
##########

Kyaah provided **sendFiles** function for sending simple mail with file(s).

.. code-block:: python

  import kyaah

  sender = "youremail@gmail.com"
  receiver = ["receiver_1@gmail.com", "receiver_2@gmail.com"]
  passwd = "*********" # use app password

  mail_serve = "gmail"
  subj = f"Hellow world!"
  body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt."
  files=['em.py', 'test.py', '/home/usman/Desktop/media/Usman.jpg']

  kyaah.sendFiles(files=files, from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)

**FOR SECURITY REASON**

if you added your `email address` and `app password` in your system environment variable, include a keyword `env` to be `True`. And then put the variable name of your email address and email app password, instead of the raw email address and app password. See hint for this in your interpreter by calling the  '''help(Vault)''' class, enable `env` to be `True` in production instead of leaving the default which is `False` example::
      
  kyaah.sendFiles(files=files, from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd, env=True)
