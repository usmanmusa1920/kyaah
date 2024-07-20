
Kyaah
#####

Kyaah abstract away cognitive over-head of sending SMTP, POP3, and IMAP mail, together with other mailing operations things like, mail with file, tokens etc.

Release v\ |version|


.. image:: https://static.pepy.tech/badge/kyaah/month
    :target: https://pepy.tech/project/kyaah
    :alt: Kyaah Downloads Per Month Badge
    
.. image:: https://img.shields.io/pypi/l/kyaah.svg
    :target: https://pypi.org/project/kyaah/
    :alt: License Badge

.. image:: https://img.shields.io/pypi/wheel/kyaah.svg
    :target: https://pypi.org/project/kyaah/
    :alt: Wheel Support Badge

.. image:: https://img.shields.io/pypi/pyversions/kyaah.svg
    :target: https://pypi.org/project/kyaah/
    :alt: Python Version Support Badge
    
-------------------

Installation
============

First, you are recommended to create a virtual environment **python -m venv venv** and then activate it **source venv/bin/activate**

Once that finish now install the library using::

    pip install kyaah
    
Wait for the installation to finish, basically the library was uploaded using `sdist` (Source Distribution) and `bdist_wheel` (Built Distribution).

Usage
=====

To use kyaah, simply import the module and set your credentials, which include **sender**, **receiver**, **subject**, **body**, and **password** just like the sample below:

.. code-block:: python

    import kyaah
        
    creds = dict(
        sender = "myemail@gmail.com",
        receiver = ["receiver1@gmail.com", "receiver2@gmail.com"],
        subject = "Hellow world!",
        body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.",
        password = "**********",
    )

With the above configuration, you can now send your mail, by calling the **kyaah.send** function with appropriate keyword arguments.

-   **Send plain mail**

    For sending a simple SMTP mail, by simply calling the send method and pass the **creds** as a keyword, like.

    .. code-block:: python

        kyaah.send(credentials=creds)

-   **Send image(s) mail**

    For sending simple mail with image(s), by adding a dictionary key **creds["image"]** giving it a value of list of image(s) you want to send. And call the send method and pass the **creds** as a keyword value of **credentials**, also ensure to add **include** keyword argument by giving it value of **image**, like.

    .. code-block:: python

        creds["image"] = ["/home/user/Desktop/media/image1.jpg", "/home/user/Desktop/media/image2.jpg"]

        kyaah.send(include="image", credentials=creds)

-   **Send file(s) mail**

    For sending simple mail with file(s), by adding a dictionary key **creds["file"]** giving it a value of list of file(s) you want to send. And call the send method and pass the **creds** as a keyword value of **credentials**, also ensure to add **include** keyword argument by giving it value of **file**, like.

    .. code-block:: python

        creds["file"] = ["requirements.txt", "helloworld.py", "/home/user/Desktop/media/image1.jpg"]

        kyaah.send(include="file", credentials=creds)

-   **Send page(s) mail**

    For sending simple mail with page, by adding a dictionary key **creds["page"]** giving it a value of list of page(s) you want to send. And call the send method and pass the **creds** as a keyword value of **credentials**, also ensure to add **include** keyword argument by giving it value of **page**, like.

    .. code-block:: python

        creds["page"] = ["/home/user/Desktop/index.html"]

        kyaah.send(include="page", credentials=creds)

-   **Send local mail**

    Kyaah provided functionality to test your mail locally. By first booting up the python mail server on a different terminal by::

        python -m smtpd -c DebuggingServer -n localhost:1025

    and then open another terminal and run your python script/code by calling the send method and ensure to add **local** keyword argument by giving it value of **True**, like.

    .. code-block:: python

        kyaah.send(local=True, credentials=creds)

    If you want to boot up the python mail server with a different port, you are to include the port you want when booting the python mail server, is like to do:

    .. code-block:: python

        python -m smtpd -c DebuggingServer -n localhost:7000

    After that, add a dictionary key **creds["port"]** giving it a value of the port number, like so::

        creds["port"] = 7000

        kyaah.send(local=True, credentials=creds)


.. note::
    
    **FOR SECURITY REASON**

    If you added your **email address** and **password** (for sender) in your system environment variable, include a dictionary key **env** with a value of **True** in the creds dictionary. And then put the variable name of your email address and email app password, instead of the raw email address and app password. See hint for this in your interpreter by calling the  '''help(Vault)''' class, give **env** value of **True** in production instead of leaving the default which is **False** over-write it with e.g::

        creds["env"] = True
        

Table of content
----------------

.. toctree::
    :maxdepth: 2

    maa_and_utils


Useful links:
-------------

- `Repository <https://github.com/usmanmusa1920/kyaah>`_

- `PYPI Release <https://pypi.org/project/kyaah>`_
