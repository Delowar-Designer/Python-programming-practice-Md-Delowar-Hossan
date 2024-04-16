# Description of configuration and output formatting of logging
# importing module
import logging
logging.basicConfig(filename="newfile.log",format='%(asctime)s%(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Test messages
logger.debug("Harmless debug Message")
logger.info("just an information")
logger.warning("Its a warning")
logger.error("Did you tr to divide by zero")
logger.critical("internet is down")