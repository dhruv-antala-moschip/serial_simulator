import pytest
from simulator.message_validator import MessageValidator
from simulator.errors import InvalidMessageError

@pytest.mark.parametrize("message, expected_result", [
    ('{"id": 1, "content": "Hello", "timestamp": "2025-01-07"}', True),
    ('{"id": "string", "content": "Hello", "timestamp": "2025-01-07"}', False),  # Invalid id type
    ])
def test_validate_message(message, expected_result, message_validator):
    if expected_result:
        assert message_validator.validate_message(message) == True
    else:
        with pytest.raises(InvalidMessageError):
            message_validator.validate_message(message)