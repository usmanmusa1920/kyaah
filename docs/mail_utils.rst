:tocdepth: 2

Mail utilities
##############

Kyaah provided some other utilities such as otp code function, fake email (generated from guerillamail) and others.

Kyaah with token
----------------

There is an OTP code feature if you want to send an OTP code for verification using the otp function provided by:

.. code-block:: python

    from kyaah import otp

    print(otp())

You can also specify the length of numbers you want,
by passing an argument of the range number you want in the function like:

.. code-block:: python

    from kyaah import otp

    print(otp(12))

Kyaah with faker
----------------

Use **Faker** for giving you a random email address from guerillamail

.. code-block:: python

    from kyaah import fk

    fk()
