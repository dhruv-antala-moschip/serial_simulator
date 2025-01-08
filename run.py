import time
import serial
from simulator.serial_handler import SerialHandler
from simulator.message_validator import MessageValidator
from simulator.logger import Logger
from simulator.errors import SerialPortError, InvalidMessageError

# Initialize components
logger = Logger("communication.log")
serial_handler = SerialHandler()
# Simulated Messages
valid_message = '{"id": 1, "content": "Hello", "timestamp": "2025-01-01T10:00:00"}'
invalid_message = '{"id": , "content": "Invalid", "timestamp": "2025-01-01T10:00:00"}'


def run_simulator():
    try:
        port_1 = "/dev/pts/15"
        port_2 = "/dev/pts/16"
        print("Opening virtual serial ports...")
        serial_handler.open_port(port_1, 9600)
        receiver = serial.Serial(port_2, 9600, timeout=1)
        time.sleep(1)
        print("Sending valid message...")
        try:
            if MessageValidator.validate_message(valid_message):
                serial_handler.send_message(valid_message.encode('utf-8'))
                logger.log_message("SEND", valid_message)
        except InvalidMessageError as e:
            print(e)
        print("Simulating reception of message...")
        receiver.write(valid_message.encode('utf-8'))
        received_message = receiver.readline().decode('utf-8')

        try:
            if MessageValidator.validate_message(received_message):

                logger.log_message("received"
                                   "", received_message)
                print(f"Received valid message: {received_message}")
        except InvalidMessageError as e:
            logger.log_message("error", str(e))
            print(f"Invalid message received: {received_message}")
        print("Simulating invalid message...")
        try:
            MessageValidator.validate_message(invalid_message)
        except InvalidMessageError as e:
            logger.log_message("error", str(e))
            print(f"Validation failed: {e}")
    except SerialPortError as e:
        logger.log_message("error", str(e))
        print(f"Serial port error: {e}")
    finally:
        print("Closing virtual ports...")
        serial_handler.close_port()
        receiver.close()


if __name__ == "__main__":
    run_simulator()

