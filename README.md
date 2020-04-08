# csv.wsgi
CSV parsing interface using Flask under Apache

This application is a basic tutorial on:

- setting up [Flask](https://flask.palletsprojects.com/en/1.1.x/) ([Werkzeug](https://palletsprojects.com/p/werkzeug/), [Jinja](https://palletsprojects.com/p/jinja/)) inside [Apache](http://httpd.apache.org/) as [wsgi](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface).
- Python code to run a basic CSV (aka, Tab separated) parser
- Web interface

## Installation
Basic Installation:
 - `sudo apt-get install libapache2-mod-wsgi-py3 python3-dev`
 - `sudo a2enmod wsgi`

Configuring:
 - `sudo nano /etc/apache2/sites-available/csv.wsgi.conf`
 - Paste the contents of [vhost.conf](vhost.conf) in csv.wsgi.conf          
 - `sudo a2ensite csv.wsgi`
 - `cd /var/www/python/csv.wsgi/`
 - `chmod 755 csv.wsgi`
 - `sudo systemctl reload apache2`
 - `tail -n20 /var/log/apache2/error.log`

Paths (/var/www/python/csv.wsgi/) to be configured in:
 - [csv.wsgi](csv.wsgi)
 - [www.py](www.py) - Flask debugging server (optional)

The commands list may not be accurate. You should consider this document as a reference only.
