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

# for Mac OS X only:
# brew install libevent

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
* When an entity is created (probably using POST) response code is 201 (not 200). See RFC
* A message should not be NULL and less than 255 chars.
* Usernames and topic cannot have special characters in them
* Communication is JSON based
* on POST /topic/user/ we will create any of them if they do not exist.

TO DO
~~~~~
* Better testing, initial version had only basic tests for validating initial spec
* validation of parameters for special chars, length
* load testing and documenting solution limits
* daemon scripts
* watchdog to restart the daemon if it does crash
* investigate docker usage for packaging/deployment 
* have beer with the customer!
