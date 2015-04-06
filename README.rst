===============================
Homework : Basic HTTP messaging
===============================

Getting the code
~~~~~~~~~~~~~~~~

git clone https://github.com/ssbarnea/zzz-homework.git

Testing
~~~~~~~

python manage.py test

Running the server
~~~~~~~~~~~~~~~~~~

python manage.py runserver


Implementation
~~~~~~~~~~~~~~

Following HTTP specification when spec is not really clear.

* When an entity is created (probably using POST) response code is 201 (not 200). See RFC
* A message should not be NULL and less than 255 chars.
* Usernames and topic cannot have special characters in them
* Communication is JSON based
* on POST /topic/user/ we will create any of them if they do not exist.
