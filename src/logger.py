import logging   # Used to record events, errors, and messages from the program
import os        # Used to interact with the operating system (files, folders, paths)
from datetime import datetime   # Used to get the current date and time


# Create a log file name using the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


# Create a path for the logs folder inside the current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)


# Create the logs folder if it does not already exist
os.makedirs(logs_path, exist_ok=True)


# Create the full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


# Configure the logging system
logging.basicConfig(

    filename=LOG_FILE_PATH,  # File where logs will be stored

    # Format of each log message
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",

    level=logging.INFO  # Log messages of level INFO and above
)

if __name__=="__main__":
    logging.info("logging has started") 