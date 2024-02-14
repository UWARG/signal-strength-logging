"""
Logs LTE signal strength into a file.
"""
import datetime
import pathlib
import time

import serial


# Parameters
DEVICE_PATH = "/dev/ttyUSB2"
BAUDRATE = 115200
AT_COMMAND = b"AT+CSQ"
OUTPUT_LOG_FILE_PATH = pathlib.Path(f"signal_log_{int(time.time())}.txt")
PERIOD = 2

# Wait 20 seconds becasue the RPi has a setting where it doesn't boot until 20 seconds after power
time.sleep(20)

while True:
    log_file = open(OUTPUT_LOG_FILE_PATH, 'a')

    # Create serial connection
    ser = serial.Serial(
        DEVICE_PATH,
        baudrate=BAUDRATE,
        timeout=1,
    )
    
    # Write AT command to the modem
    ser.write(AT_COMMAND)

    # Get result back from the modem
    result = str(ser.readline())

    # String parsing can be done here if you want to edit the log file output
    log_file.write(datetime.datetime.now().isoformat(timespec="seconds") + "    " + result)

    log_file.close()

    # print("logged...")

    time.sleep(PERIOD)
