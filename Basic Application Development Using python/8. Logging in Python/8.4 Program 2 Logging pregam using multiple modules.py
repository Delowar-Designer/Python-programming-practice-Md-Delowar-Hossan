# Logging pregam using multiple modules
'''import logging
import mylib
def main():
    logging.basicConfig(filename="myapp.log", level=logging.INFO)
    logging.info("Started")
    mylib.do_something()
    logging.info("Finished")
if __name__ == "__main__":
\main()'''
import logging
import mylib

def main():
    logging.basicConfig(filename="myapp.log", level=logging.INFO)
    logging.info("Started")
    mylib.do_something()
    logging.info("Finished")

if __name__ == "__main__":
    main()
