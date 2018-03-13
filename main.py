import os
from boxReader import BoxReader


EMAIL = os.environ.get('email')
PASS = os.environ.get('passEmail')

ROOT = os.environ.get('fullDir') if os.environ.get('fullDir') is not None else './notas'


if __name__ == "__main__":
    
    box = BoxReader(EMAIL, PASS, root=ROOT).setbox('Notas').savelasts(rm="NFe - [0-9]{8} - ", until=5140).close()



