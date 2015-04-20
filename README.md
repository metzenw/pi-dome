pi-dome
=======

Home automation via a python sockets.

Summary: This is a client server based HA system. All wire traffic is secured
through openssl.

Versions: v1.0 and v1.1. 1.0 is a beta and should not be used. It was a proof of concept for a
REST API but lacked the real "meat" needed in a full home automation solution.


Quick start v1.1
------------
- Comming soon


Depricated v1.0 install instructions:

Note: In order to use this you will need to install falsk. Please see the following links for details:
- [Flask Setup](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
- [Flask Mega setup](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

Quick start v1.0  (Depricated)
------------
[RASPBIN]http://www.raspberrypi.org/downloads/)

    - 0) apt-get install apache2 php5 libapache2-mod-php5 virtualenvwrapper python-virtualenv
    - 1) cd /var/
    - 2) mkdir pi-dome
    - 3) cd pi-dome
    - 4) virtualenv flask
    - 5) flask/bin/pip install flask
    - 6) git clone https://github.com/miguelgrinberg/Flask-HTTPAuth.git
    - 7) cd Flask-HTTPAuth/
    - 8) python setup.py install

-----------------------------------
Once you have cloned the repo copy the pi-dome.py into your /var/pi-dome/ directory. 




