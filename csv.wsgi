import logging
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/python/csv.wsgi/")

from app import app as application
application.secret_key = "secret key"
