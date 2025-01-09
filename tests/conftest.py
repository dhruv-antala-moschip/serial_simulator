import pytest
from simulator.serial_handler import SerialHandler
from simulator.message_validator import MessageValidator
from simulator.logger import Logger

@pytest.fixture
def serial_handler():
    return SerialHandler()

@pytest.fixture
def message_validator():
    return MessageValidator()

@pytest.fixture
def logger():
    return Logger()

@pytest.fixture
def valid_message():
    return '{"id": 1, "content": "Test message", "timestamp": "2025-01-01T12:00:00"}'

@pytest.fixture
def invalid_message():
    return '{"id": 1, "content": "Test message"}'  # Missing timestamp