import logging
import time
import pytest


class Logger:
    def __init__(self, log_file='communication.log', log_level=logging.INFO):
        self.logger = logging.getLogger('serial_simulator')
        self.logger.setLevel(log_level)
        if not self.logger.handlers:
            handler = logging.FileHandler(log_file)
            handler.setLevel(log_level)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    @pytest.mark.slow
    def log_message(self, direction, message):
        self.logger.info(f'{direction}: {message}')
