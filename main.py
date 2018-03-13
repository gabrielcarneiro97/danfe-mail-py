import os
from boxReader import BoxReader


EMAIL = os.environ['email']
PASS = os.environ['passEmail']


if __name__ == "__main__":
    
    box = BoxReader(EMAIL, PASS, root='./notas').setbox('Notas').savelasts(rm="NFe - [0-9]{8} - ", until=5140).close()



