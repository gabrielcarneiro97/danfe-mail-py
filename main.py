import os
import time
from boxReader import BoxReader

EMAIL = os.environ.get('email')
PASS = os.environ.get('passEmail')
ROOT = os.environ.get('fullDir') if os.environ.get('fullDir') is not None else './notas'
BOX = 'Notas'
REGEX = "NFe - [0-9]{8} - "
SLEEP = 10

if __name__ == "__main__":
    box = BoxReader(EMAIL, PASS, root=ROOT).setbox(BOX)

    while True:
        box.savelasts(REGEX)
        time.sleep(SLEEP)
