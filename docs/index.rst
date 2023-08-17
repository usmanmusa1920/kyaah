
Kyaah
#####

Kyaah abstract away cognitive over-head of sending SMTP mail, together with other mailing operations things like, mail with file, tokens etc.

Simple use of kyaah
===================

First we recommend creating a virtual environment **python -m venv venv** and then activate it **source venv/bin/activate**

Once that finish now install the library using::

    pip install kyaah
    
Wait for the installation to finish, basically the library was uploaded using **sdist** (Source Distribution). After that create a new file let call it **test.py** in the file paste the below code with your credentials.

.. code-block:: python

    import kyaah

    sender = 'my_email@gmail.com'
    receiver = ['receiver_1@gmail.com', 'receiver_2@gmail.com']
    passwd = '*********' # use app password

    server = 'gmail'
    subj = f'Hellow world!'
    body = 'Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt.'

    kyaah.sendMail(from_usr=sender, to_usr=receiver, svr=server, subject=subj, body=body, mail_passwd=passwd)

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


Useful links:
-------------

- `Repository <https://github.com/usmanmusa1920/kyaah>`_

- `PYPI Release <https://pypi.org/project/kyaah>`_
