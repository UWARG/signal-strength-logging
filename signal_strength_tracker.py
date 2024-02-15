"""
Logs LTE signal strength into a file.
"""
import datetime
import pathlib
import time

import serial


# Parameters
SERIAL_PORT = "/dev/ttyUSB3"  # Change this to match your modem's serial port
BAUDRATE = 115200  # Change this to match your modem's baud rate
AT_COMMAND = b"AT+CSQ\r\n"  # Command to run on modem
OUTPUT_LOG_FILE_PATH = pathlib.Path(f"/media/warg/E3F9-7EE3/signal_log_{int(time.time())}.txt")
PERIOD = 3

# Wait 20 seconds becasue the RPi has a setting where it doesn't boot until 20 seconds after power
time.sleep(20)

while True:
    log_file = open(OUTPUT_LOG_FILE_PATH, 'a')

    # Create serial connection
    ser = serial.Serial(
        SERIAL_PORT,
        baudrate=BAUDRATE,
        timeout=1,
    )
    
    # Write AT command to the modem
    ser.write(AT_COMMAND)

    # Get result back from the modem (reads 1000 bytes)
    response = ser.read(1000)

    # String parsing can be done here if you want to edit the log file output
    log_file.write(
        datetime.datetime.now().isoformat(timespec="seconds") + \
        "    Response: " + response.decode('utf-8') + "\n"
    )

    log_file.close()
    ser.close()

    time.sleep(PERIOD)
