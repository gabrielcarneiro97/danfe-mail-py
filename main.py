import os
import time
import signal
import sys
from boxReader import BoxReader

EMAIL = os.environ.get('email')
PASS = os.environ.get('passEmail')
ROOT = os.environ.get('fullDir') if os.environ.get('fullDir') is not None else './notas'
BOX = 'Notas'
REGEX = 'NFe - [0-9]{8} - '
SLEEP = 300

if __name__ == '__main__':
    box = BoxReader(EMAIL, PASS, root=ROOT).setbox(BOX)

    def signal_handler(signal, frame):
        box.log.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        box.savelasts(REGEX, nm=20)
        time.sleep(SLEEP)
    
    box.close()
