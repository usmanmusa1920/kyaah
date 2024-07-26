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

First, you are recommended to create a virtual environment **python -m venv venv** and then activate it **source venv/bin/activate**, next install the library using::

    pip install kyaah
    
Wait for the installation to finish, basically the library was uploaded using `sdist` (Source Distribution) and `bdist_wheel` (Built Distribution).

Usage
=====

To use kyaah, simply import the library and set payload, which include **sender**, **receiver**, **subject**, **body**, and **password** just like the sample below:

.. code-block:: python

    import kyaah
        
    payload = dict(
        sender = "sender@gmail.com",
        receiver = ["receiver@gmail.com"],
        subject = "Hellow world!",
        body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.",
        password = "**********",
    )

With the above configuration, you can now send your mail, by calling the **kyaah.send** function with appropriate keyword arguments.

.. note::

    The password to use, is app password, take note that if you use your traditional mail password that you use to login, it won't give access to!

-   **Send plain mail**

    For sending a simple SMTP mail, by simply calling the send method and pass the **payload** as a keyword, like.

    .. code-block:: python

        kyaah.send(credentials=payload)

-   **Send image(s) mail**

    For sending simple mail with image(s), by adding a dictionary key **payload["image"]** giving it a value of list of image(s) you want to send. And call the send method and pass the **payload** as a keyword value of **credentials**, also ensure to add **include** keyword argument by giving it value of **image**, like.

    .. code-block:: python

        payload["image"] = ["/home/user/Desktop/media/image1.jpg", "/home/user/Desktop/media/image2.jpg"]

        kyaah.send(include="image", credentials=payload)

-   **Send file(s) mail**

    For sending simple mail with file(s), by adding a dictionary key **payload["file"]** giving it a value of list of file(s) you want to send. And call the send method and pass the **payload** as a keyword value of **credentials**, also ensure to add **include** keyword argument by giving it value of **file**, like.

    .. code-block:: python

        payload["file"] = ["requirements.txt", "helloworld.py", "/home/user/Desktop/media/image1.jpg"]

        kyaah.send(include="file", credentials=payload)

-   **Send page(s) mail**

    For sending simple mail with page, by adding a dictionary key **payload["page"]** giving it a value of **test** for testing, or a list of page(s) you want to send. And call the send method and pass the **payload** as a keyword value of **credentials**, also ensure to add **include** keyword argument by giving it value of **page**, like.

    .. code-block:: python

        # for testing
        payload["page"] = "test"

        # for sending your html page (not testing)
        payload["page"] = ["/home/user/Desktop/index.html"]

        kyaah.send(include="page", credentials=payload)

-   **Send local mail**

    Kyaah provided functionality to test your mail locally. By first booting up the mail server on terminal by::

        kyaah localhost

    and then open another terminal and run your python script/code by calling the send method and ensure to add **local** keyword argument by giving it value of **True**, like.

    .. code-block:: python

        kyaah.send(local=True, credentials=payload)

    If you want to boot up the python mail server with a different port, you are to include the port you want when booting the python mail server, by:

    .. code-block:: python

        kyaah localhost --port 7000

    After that, add a dictionary key **payload["port"]** giving it a value of the port number, like so::

        payload["port"] = 7000

        kyaah.send(local=True, credentials=payload)


.. note::
    
    **FOR SECURITY REASON**

    If you added your **email address** and **password** (for sender) in your system environment variable, include a dictionary key **env** with a value of **True** in the payload dictionary. And then put the variable name of your email address and email app password, instead of the raw email address and app password. See hint for this in your interpreter by calling the  '''help(Vault)''' class, give **env** value of **True** in production instead of leaving the default which is **False** over-write it with e.g::

        payload["env"] = True
        

Table of content
----------------

.. toctree::
    :maxdepth: 2

    maa_and_utils


Useful links:
-------------

- `Documentations <https://kyaah.readthedocs.io>`_

- `Repository <https://github.com/usmanmusa1920/kyaah>`_

- `PYPI Release <https://pypi.org/project/kyaah>`_
