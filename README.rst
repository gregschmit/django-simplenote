simplenote
##########

.. inclusion-marker-do-not-remove

.. image:: https://readthedocs.org/projects/django-simplenote/badge/?version=latest
    :target: https://django-simplenote.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Documentation: https://django-simplenote.readthedocs.io

Source: https://github.com/gregschmit/django-simplenote

PyPI: https://pypi.org/project/django-simplenote/

simplenote is a reusable Django app for posting simple notes to a board. You can
secure access with authentication, but the default is to provide public access.

**The Problem**: I wanted to transfer text between different devices (or to
other people) without having to authenticate, relying on secrecy of the domain
to prevent abuse, but accepting that this isn't a secure solution.

**The Solution**: You can set this app up on the internet on your own domain to
use for notes. Optionally you can secure this service with authentication, but
by default it's a public board.

How to Use
##########

.. code-block:: shell

    $ pip install django-simplenote

Include :code:`django_simplenote` in your :code:`INSTALLED_APPS`.

If you want to change the defaults, add these to your :code:`settings.py`:

.. code-block:: python

    SIMPLENOTE_MAX_NOTES = 10
    SIMPLENOTE_MAX_NOTE_LENGTH = 5000

Then, run migrations and add :code:`django_simplenote.urls` to your URLconf.

Contributing
############

Email gschmi4@uic.edu if you want to contribute. You must only contribute code
that you have authored or otherwise hold the copyright to, and you must
make any contributions to this project available under the MIT license.

To collaborators: don't push using the :code:`--force` option.

Dev Quickstart
##############

simplenote comes with a `settings.py` file, technically making it a Django project as well as a Django app. First clone, the repository into a location of your choosing:

.. code-block:: shell

    $ git clone https://github.com/gregschmit/django-simplenote

Then you can go into the :code:`django-simplenote` directory and do the initial migrations and run the server (you may need to type :code:`python3` rather than :code:`python`):

.. code-block:: shell

    $ cd django-simplenote
    $ python manage.py makemigrations django_simplenote
    $ python manage.py migrate
    $ python manage.py createsuperuser
    ...
    $ python manage.py runserver

Then you can see the models at http://127.0.0.1:8000/admin.
