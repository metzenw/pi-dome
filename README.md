pi-dome
=======

Home automation via a python REST api and Raspberry PI
-----------------------------------
Note: In oder to use this you would install falsk. Please see the following links for details:
- [http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask]
- [http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world]
-----------------------------------

Quick start on RASPBIAN ( - [http://www.raspberrypi.org/downloads/] )
-----------------------------------
apt-get install apache2 php5 libapache2-mod-php5 virtualenvwrapper python-virtualenv

1) cd /var/
2) mkdir pi-dome
3) cd pi-dome
4) virtualenv flask
5) flask/bin/pip install flask
6) git clone https://github.com/miguelgrinberg/Flask-HTTPAuth.git
7) cd Flask-HTTPAuth/
8) python setup.py install

-----------------------------------
Once you have cloned the repo copy the pi-dome.py into your /var/pi-dome/ directory. 
