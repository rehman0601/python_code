import logging

# Set up logging configuration
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def example_function():
    logging.info("This is an info message.")
    logging.error("This is an error message.")

# Test the function
example_function()
