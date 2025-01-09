import pytest


def test_open_port(mocker,serial_handler):
    mock_serial = mocker.patch('simulator.serial_handler.serial.Serial')
    serial_handler.open_port('/dev/ttyACM0', 9600)
    mock_serial.assert_called_once_with('/dev/ttyACM0', 9600)

def test_send_message(mocker,serial_handler):
    mock_serial = mocker.patch('simulator.serial_handler.serial.Serial')
    serial_handler.open_port('/dev/ttyACM0', 9600)
    serial_handler.send_message("hello")
    mock_serial.return_value.write.assert_called_once_with("hello")


@pytest.mark.parametrize('input_val, output_val', [
    ("ping", "pong"),
    ("hello", "world"),
    ("arduino", "rocks")
])
def test_send_and_receive(input_val, output_val, mocker,serial_handler,logger):
    mock_serial = mocker.patch('simulator.serial_handler.serial.Serial')

    mock_serial.return_value.readline.return_value = output_val
    serial_handler.open_port('/dev/ttyACM0', 9600)

    serial_handler.send_message(input_val)
    mock_serial.return_value.write.assert_called_once_with(input_val)


    response = serial_handler.receive_message()
    print(f"Mocked response: {response}", end=" ")
    assert response == output_val

    logger.log_message("SEND", input_val)
    logger.log_message("RECEIVE", output_val)