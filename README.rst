.. image:: https://api.travis-ci.org/ssbarnea/zzz-homework.svg?branch=master
        :target: https://travis-ci.org/ssbarnea/zzz-homework

.. image:: https://img.shields.io/coveralls/ssbarnea/zzz-homework.svg
        :target: https://coveralls.io/r/ssbarnea/zzz-homework

===============================
Homework : Basic HTTP messaging
===============================

Getting the code
~~~~~~~~~~~~~~~~

git clone https://github.com/ssbarnea/zzz-homework.git

Installing
~~~~~~~~~~

# You need python 2.7-3.4 to run it as it requires latest stable django (1.8)

pip install -r requirements.txt

Testing
~~~~~~~

python manage.py test

Running the server
~~~~~~~~~~~~~~~~~~

python manage.py runserver


Implementation
~~~~~~~~~~~~~~
We picked Django because is mature, popular and easy to use. 

While a gevent could seem a a very scalable solution it could be an over-engineering for such a task. Reference http://nichol.as/benchmark-of-python-web-servers

Assumptions made during initial implementation:

* Following HTTP specification when initial spec is not really clear.
* When an entity is created (probably using POST) response code is 201 (not 200). See `RFC2616 <https://www.ietf.org/rfc/rfc2616.txt>`_
* A message should not be NULL and less than 255 chars.
* Usernames and topic cannot have special characters in them
* Communication is JSON based
* on POST /topic/user/ we will create any of user or topic if they do not exist.

TO DO
~~~~~

* Better testing, initial version had only basic tests for validating initial spec
* validation of parameters for special chars, length
* load testing and documenting solution limits (tried implementing nose but discovered that `django-nose is broken <https://github.com/django-nose/django-nose/issues/186>`_
* daemon scripts
* watchdog to restart the daemon if it does crash
* investigate docker usage for packaging/deployment 
* have beer with the customer!
