import os
from boxReader import BoxReader


EMAIL = os.environ.get('email')
PASS = os.environ.get('passEmail')

ROOT = os.environ.get('fullDir') if os.environ.get('fullDir') is not None else './notas'

REGEX = "NFe - [0-9]{8} - "


if __name__ == "__main__":
    
    box = BoxReader(EMAIL, PASS, root=ROOT).setbox('Notas')
    
    box.savelasts(REGEX, 1, one_call=True)()
    



