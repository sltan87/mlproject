import sys   # Import sys module to access system-specific parameters and exception info
from src.logger import logging

# Function to format detailed error messages
def error_message_detail(error, error_detail: sys):
    
    # Get exception information (type, value, traceback)
    _, _, exc_tb = error_detail.exc_info()
     
    # Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Create a formatted error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,        # File where the error happened
        exc_tb.tb_lineno, # Line number of the error
        str(error)        # Actual error message
    )

    return error_message   # Return the formatted error message


# Custom exception class
class CustomException(Exception):

    # Constructor method
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Call the parent Exception constructor
        
        # Store detailed error message
        self.error_message = error_message_detail(error_message, error_detail)

    # String representation of the error
    def __str__(self):
        return self.error_message  # Return the formatted error message
if __name__=="__main__":
        try:
            a=1/0
        except Exception as e:
            logging.info("Divide by zero") 
            raise CustomException(e,sys)