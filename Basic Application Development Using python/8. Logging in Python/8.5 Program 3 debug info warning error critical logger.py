# debug info warning error critical logger
import logging

# Create and configure logger using the basic Config Function
logging.basicConfig(filename='newfil555e.log', format='%(asctime)s%(message)s',filemode='w')

# creating an object of the logging
logger = logging.getLogger()

# Test messages
logger.debug("Harmless debug Message")
logger.info("just an information")
logger.warning("Its a warning")
logger.error("Did you tr to divide by zero")
logger.critical("internet is down")