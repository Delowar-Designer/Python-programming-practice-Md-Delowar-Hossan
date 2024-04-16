# Various methods of the Log in object work
import logging
logging.basicConfig(filename="newffile.log",format='%(asctime)s%(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning('lts a Warning')
logger.error("Did you try to divides by zero")
logger.critical("Internet is down")
