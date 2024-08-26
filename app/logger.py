#!/usr/bin/env python3
"""
Logging everything that happens in the files
"""
import logging
from logging.handlers import RotatingFileHandler
import os

if not os.path.exists("logs"):
    os.makedirs("logs")


def setup_logger(module_name):
    logger = logging.getLogger(module_name)

    # Avoid adding multiple handlers if already exists
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)

        file_handler = RotatingFileHandler(
            f"logs/{module_name}.log", maxBytes=2000000, backupCount=5)
        file_handler.setLevel(logging.INFO)

        # Console handler for outputting logs to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Format for log messages
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add both handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
