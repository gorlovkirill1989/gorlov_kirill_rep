import logging
import os

from config import LOGS_DIR


def create_logger(name: str, level: int = logging.DEBUG) -> logging.Logger:
    """функция, которая создает логгер"""
    logger = logging.getLogger(name)

    filename = os.path.join(LOGS_DIR, f"{name}.log")
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    logger_file_handler = logging.FileHandler(filename, encoding="utf8", mode="w+")
    logger_formatter = logging.Formatter("%(asctime)s - %(levelname)s - FUNC(%(funcName)s): %(message)s")
    logger_file_handler.setFormatter(logger_formatter)
    logger.addHandler(logger_file_handler)
    logger.setLevel(level)

    return logger
