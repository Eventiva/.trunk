# src/error_handling_module.py

import logging


def handle_error(exception):
    # Log the error message
    logging.error(str(exception))

    # Perform any necessary error handling actions
    # ...
