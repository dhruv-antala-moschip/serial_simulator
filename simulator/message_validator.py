import json
from .errors import InvalidMessageError


class MessageValidator:
    @staticmethod
    def validate_message(message):
        try:
            data = json.loads(message)


            if 'id' not in data or 'content' not in data or 'timestamp' not in data:
                raise InvalidMessageError("Missing required fields")


            return True

        except json.JSONDecodeError:
            raise InvalidMessageError("Invalid JSON format")

        except InvalidMessageError as e:
            raise e
