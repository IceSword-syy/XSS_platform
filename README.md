# XSS_platform (Unfinished)

[![Python 2.7](https://img.shields.io/badge/python-2.7-yellow.svg)](https://www.python.org/)

A Cross-site Scripting (XSS) vulnerability exploit tool.

# Requirements

* [Python 2.7.x](http://www.python.org/download/)
* [Django 1.9.x](https://pypi.python.org/pypi/django/)

# Installation

XSS_platform works out of the box with [Python](http://www.python.org/download/) version **2.7.x** on any platform.

You can download the latest zipball by clicking [here](https://github.com/lewangbtcc/XSS_platform/archive/master.zip).

Preferably, you can download anti-XSS by cloning the [Git](https://github.com/lewangbtcc/XSS_platform) repository and then install requirements.

    $ git clone https://git@github.com:lewangbtcc/XSS_platform.git XSS_platform
    $ cd XSS_platform
    $ pip install -r requirements.txt

After downloading, follow these steps to create database.

    $ cd XSS_platform
    $ python manage.py makemigrationgs
    $ python manage.py migrate

Then you should create an admin account by following these steps.

    $ cd XSS_platform
    $ python manage.py createsuperuser

Following the admin account creation guild, you can easily register an admin account. Thus XSS_platform has completely installed, enjoy it!
