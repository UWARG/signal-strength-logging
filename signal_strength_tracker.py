"""
Logs LTE signal strength into a file.
"""
import datetime
import pathlib
import subprocess
import time


# Parameters
INITIAL_COMMAND = ["minicom", "-o", "-D", "/dev/ttyUSB2"]
# For this file, just type AT+CSQ. A newline character at the end should not affect the results
AT_COMMAND_FILE_PATH = pathlib.Path("AT_command.txt")
# INITIAL_COMMAND = ["python3"]
# AT_COMMAND_FILE_PATH = pathlib.Path("input.txt")  # Used for testing, just has print("hello world")
OUTPUT_LOG_FILE_PATH = pathlib.Path(f"signal_log_{int(time.time())}.txt")
PERIOD = 2

while True:
    AT_command = open(AT_COMMAND_FILE_PATH, 'r')
    log_file = open(OUTPUT_LOG_FILE_PATH, 'a')

    result = subprocess.run(
        INITIAL_COMMAND,
        shell=True,
        capture_output=True,
        encoding='utf_8',
        stdin=AT_command
    )

    # String parsing can be done here if you want to edit the log file output
    log_file.write(datetime.datetime.now().isoformat() + "  " + result.stdout)

    AT_command.close()
    log_file.close()

    # print("logged...")

    time.sleep(PERIOD)
