
Kyaah
#####

Kyaah abstract away cognitive over-head of sending SMTP, POP3, and IMAP mail, together with other mailing operations things like, mail with file, tokens etc.

Release v\ |version|


.. image:: https://static.pepy.tech/badge/kyaah/month
    :target: https://pepy.tech/project/kyaah
    :alt: Kyaah Downloads Per Month Badge

.. image:: https://static.pepy.tech/badge/kyaah/week
    :target: https://pepy.tech/project/kyaah
    :alt: Kyaah Downloads Per Week Badge
    
.. image:: https://img.shields.io/pypi/l/kyaah.svg
    :target: https://pypi.org/project/kyaah/
    :alt: License Badge

.. image:: https://img.shields.io/pypi/wheel/kyaah.svg
    :target: https://pypi.org/project/kyaah/
    :alt: Wheel Support Badge

.. image:: https://img.shields.io/pypi/pyversions/kyaah.svg
    :target: https://pypi.org/project/kyaah/
    :alt: Python Version Support Badge

.. image:: https://img.shields.io/github/contributors/usmanmusa1920/kyaah.svg
    :target: https://github.com/usmanmusa1920/kyaah/graphs/contributors
    :alt: Contributors Badge
    
-------------------

Installation & setup of kyaah
=============================

First we recommend creating a virtual environment **python -m venv venv** and then activate it **source venv/bin/activate**

Once that finish now install the library using::

    pip install kyaah
    
Wait for the installation to finish, basically the library was uploaded using `sdist` (Source Distribution) and `bdist_wheel` (Built Distribution).

Send plain mail
---------------

Kyaah provided functionality for sending a simple SMTP mail.

Create a new file let call it **test.py** in the file paste the below code with your credentials.

.. code-block:: python

    import kyaah
        
    creds = dict(
        sender = "myemail@gmail.com",
        receiver = ["receiver1@gmail.com", "receiver2@gmail.com"],
        subject = "Hellow world!",
        body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.",
        password = "**********",
    )

    kyaah.send(credentials=creds)

save the file and navigate to where the file is located in terminal and your are ready to go (run the file)::

    python test.py

Send images mail
----------------

Kyaah provided functionality for sending simple mail with image(s).

Create a new file let call it **test.py** in the file paste the below code with your credentials.

.. code-block:: python

    import kyaah
        
    creds = dict(
        sender = "myemail@gmail.com",
        receiver = ["receiver1@gmail.com", "receiver2@gmail.com"],
        subject = "Hellow world!",
        body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.",
        password = "**********",
        image = ["/home/user/Desktop/media/image1.jpg", "/home/user/Desktop/media/image2.jpg"],
    )

    kyaah.send(include="image", credentials=creds)

save the file and navigate to where the file is located in terminal and your are ready to go (run the file)::

    python test.py

Send files mail
---------------

Kyaah provided functionality for sending simple mail with file(s).

Create a new file let call it **test.py** in the file paste the below code with your credentials.

.. code-block:: python

    import kyaah
        
    creds = dict(
        sender = "myemail@gmail.com",
        receiver = ["receiver1@gmail.com", "receiver2@gmail.com"],
        subject = "Hellow world!",
        body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.",
        password = "**********",
        file = ["requirements.txt", "helloworld.py", "/home/user/Desktop/media/image1.jpg"]
    )

    kyaah.send(include="file", credentials=creds)

save the file and navigate to where the file is located in terminal and your are ready to go (run the file)::

    python test.py

Send page mail
--------------

Kyaah provided functionality for sending simple mail with page.

Create a new file let call it **test.py** in the file paste the below code with your credentials.

.. code-block:: python

    import kyaah
        
    creds = dict(
        sender = "myemail@gmail.com",
        receiver = ["receiver1@gmail.com", "receiver2@gmail.com"],
        subject = "Hellow world!",
        body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.",
        password = "**********",
        page = "/home/user/Desktop/index.html",
    )

    kyaah.send(include="page", credentials=creds)

save the file and navigate to where the file is located in terminal and your are ready to go (run the file)::

    python test.py

Send local mail
---------------

Kyaah provided functionality to test your mail locally. First boot up the python mail server on a different terminal by::

    python -m smtpd -c DebuggingServer -n localhost:1025

and then open another terminal and run your python script including the below code in it

Create a new file let call it **test.py** in the file paste the below code with your credentials.

.. code-block:: python

    import kyaah
        
    creds = dict(
        sender = "myemail@gmail.com",
        receiver = ["receiver1@gmail.com", "receiver2@gmail.com"],
        subject = "Hellow world!",
        body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.",
        password = "**********",
    )

    mail = kyaah.send(local=True, credentials=creds)

If you want to boot up the python mail server with a different port, not `1025`, in our case we will boot it now on port **7000**, is like to do:

.. code-block:: python

    python -m smtpd -c DebuggingServer -n localhost:7000

After that, pass a keyword argument of `port` with the port number as the value in the `send_local_mail` function, like::

    creds = dict(
        sender = "myemail@gmail.com",
        receiver = ["receiver1@gmail.com", "receiver2@gmail.com"],
        subject = "Hellow world!",
        body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.",
        password = "**********",
        port = 7000
    )


**FOR SECURITY REASON**

If you added your `email address` and `app password` (for sender) in your system environment variable, include a dictionary key `env` with a value of `True` in the creds dictionary. And then put the variable name of your email address and email app password, instead of the raw email address and app password. See hint for this in your interpreter by calling the  '''help(Vault)''' class, give `env` value of `True` in production instead of leaving the default which is `False` over-write it with e.g::

    creds["env"] = True


Table of content
----------------

.. toctree::
    :maxdepth: 2

    maa
    utils


Useful links:
-------------

- `Repository <https://github.com/usmanmusa1920/kyaah>`_

- `PYPI Release <https://pypi.org/project/kyaah>`_
