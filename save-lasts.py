import sys
import os
from boxReader import BoxReader

EMAIL = os.environ.get('email')
PASS = os.environ.get('passEmail')
ROOT = os.environ.get('fullDir') if os.environ.get('fullDir') is not None else './notas'


BOX_CAR = 'Notas'
REGEX_CAR = 'NFe - [0-9]{8} - (.*)'

BOX_AUT = 'Notas2'
REGEX_AUT = 'Nota Fiscal número [0-9]{4} emitida por (.*)'

BOX_RV = 'RevendaMais'
REGEX_RV = 'NFe: [0-9]{4}, Série: [0-9]{1}, Emitente [0-9]{2}.[0-9]{3}.[0-9]{3}/[0-9]{4}-[0-9]{2} - (.*) foi autorizada'

boxAut = BoxReader(EMAIL, PASS, root=ROOT).setbox(BOX_AUT)
boxCar = BoxReader(EMAIL, PASS, root=ROOT).setbox(BOX_CAR)
boxRv = BoxReader(EMAIL, PASS, root=ROOT).setbox(BOX_RV)

search = 20

if len(sys.argv) == 1:
  print("Número não definido, salvando ultimos 20 e-mails")
else:
  search = sys.argv[1]

if len(sys.argv) >= 3:
  if sys.argv[2] == 'aut':
    boxAut.savelasts(REGEX_AUT, nm=int(search))
  elif sys.argv[2] == 'rv':
    boxRv.savelasts(REGEX_RV, nm=int(search))
else:
  boxCar.savelasts(REGEX_CAR, nm=int(search))
