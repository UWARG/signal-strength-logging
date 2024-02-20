"""
Logs LTE signal strength into a file.
"""
import datetime
import pathlib
import time

import serial


SERIAL_PORT = "/dev/ttyUSB3"  # Change this to match the LTE modem's serial port
BAUDRATE = 115200  # Change this to match the LTE modem's baud rate
AT_COMMAND = b"AT+CSQ\r\n"  # Command to run on modem (returns signal strength)
OUTPUT_LOG_FILE_PATH = pathlib.Path(
    "/",
    "media",
    "warg",
    "E3F9-7EE3",
    f"signal_log_{int(time.time())}.txt"
)
TIMEOUT = 1  # Seconds
BYTES_TO_READ = 1000  # Maximum bytes to read after command is run

SETUP_TIME = 20  # Wait 20s since the RPi has a setting where it doesn't boot until 20s after power
PERIOD = 3  # Seconds


if __name__ == "__main__":
    time.sleep(SETUP_TIME)

    while True:
        log_file = open(OUTPUT_LOG_FILE_PATH, 'a', encoding="utf-8")

        # Create serial connection
        ser = serial.Serial(
            SERIAL_PORT,
            baudrate=BAUDRATE,
            timeout=TIMEOUT,
        )
        
        # Write AT command to the modem
        ser.write(AT_COMMAND)

        # Get result back from the modem (reads 1000 bytes)
        response = ser.read(BYTES_TO_READ)

        # String parsing can be done here if you want to edit the log file output
        log_file.write(
            datetime.datetime.now().isoformat(timespec="seconds") + \
            "    Response: " + response.decode("utf-8") + "\n"
        )

        log_file.close()
        ser.close()

        time.sleep(PERIOD)
