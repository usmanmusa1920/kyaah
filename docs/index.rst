
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

Simple use of kyaah
===================

First we recommend creating a virtual environment **python -m venv venv** and then activate it **source venv/bin/activate**

Once that finish now install the library using::

    pip install kyaah
    
Wait for the installation to finish, basically the library was uploaded using `sdist` (Source Distribution) and `bdist_wheel` (Built Distribution). After that create a new file let call it **test.py** in the file paste the below code with your credentials.

.. code-block:: python

    import kyaah

    sender = 'my_email@gmail.com'
    receiver = ['receiver_1@gmail.com', 'receiver_2@gmail.com']
    passwd = '*********' # use app password

    server = 'gmail'
    subj = f'Hellow world!'
    body = 'Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.'

    kyaah.sendMail(
        from_usr=sender, to_usr=receiver, svr=server, subject=subj, body=body, mail_passwd=passwd
    )

save the file and navigate to where the file is located in terminal and your are ready to go (run the file)::

    python test.py


Table of content
----------------

.. toctree::
    :maxdepth: 2

    local_mail
    send_mail
    send_images
    send_files
    send_page
    mail_utils
    pop3_and_imap
    utils


Useful links:
-------------

- `Repository <https://github.com/usmanmusa1920/kyaah>`_

- `PYPI Release <https://pypi.org/project/kyaah>`_
