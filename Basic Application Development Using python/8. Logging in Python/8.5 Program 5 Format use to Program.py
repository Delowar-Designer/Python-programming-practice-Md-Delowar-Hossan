# Format use to Program
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y%H:%M:%S')
logging.warning('Andmin logged out')