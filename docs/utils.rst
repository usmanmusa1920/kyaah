:tocdepth: 2

Utils
#####

Kyaah provided utilities such as `OTP` code function, `link expiration`, `random email` (fake email generated from guerillamail) etc.

Random email
------------

Use **Faker** for giving you a random email address from guerillamail

.. code-block:: python
    
    kyaah.fk()

Kyaah with token (OTP)
----------------------

To get an OTP code

.. code-block:: python

    import kyaah

    print(kyaah.otp())

You can also specify the length of numbers you want, by passing an argument of the range number you want in the function like:

.. code-block:: python

    import kyaah

    print(kyaah.otp(12)) # for specifying the range number

Link expire
-----------

This It really work for python app, and secret key must be provided along side with database for storing the session just like password.

.. code-block:: python
    
    import kyaah

    url = "https://kyaah.readthedocs.io"
    tokenised_link = kyaah.Tokens.link(url)

    creds = dict(
        sender = "myemail@gmail.com",
        receiver = ["receiver1@gmail.com", "receiver2@gmail.com"],
        subject = "Kyaah link age utility",
        body = f"Hi! you can follow this link {url} and update your password, it will expire in 60 seconds. Thank you!",
        password = "**********",
    )

    print(tokenised_link)
    secret = tokenised_link[0]
    data = tokenised_link[1]
    
    mail = kyaah.send(credentials=creds)
    print(kyaah.Tokens.unlink(secret, data))
