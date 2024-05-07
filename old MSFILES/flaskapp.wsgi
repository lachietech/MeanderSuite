import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/MeanderSuite')
 
from application import app as application