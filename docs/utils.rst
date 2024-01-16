:tocdepth: 2

Utils
#####

This documentation include generating `random email` `OTP` `link expiration` etc.

Random email
------------

To get a random email

.. code-block:: python
    
    kyaah.fk()

OTP
---

To get an OTP code

.. code-block:: python

    print(kyaah.otp())
    print(kyaah.otp(30)) # for specifying the range number

Link expire
-----------

This It really work for python app, and secret key must be provided along side with database for storing the session just like password.

.. code-block:: python
    
    l = 'https://kyaah.readthedocs.io'
    a = kyaah.Tokens.link(l)

    print(a)

    secret = a[0]
    data = a[1]

    subj = 'Kyaah link age utility'

    msg = f'Hi! you can follow this link {l} and update your password, it will expire in 60 seconds. Thank you!'

    kyaah.sendMail(
        from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=msg, mail_passwd=passwd)

    print(kyaah.Tokens.unlink(secret, data))
