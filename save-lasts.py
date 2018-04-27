import sys

EMAIL = os.environ.get('email')
PASS = os.environ.get('passEmail')
ROOT = os.environ.get('fullDir') if os.environ.get('fullDir') is not None else './notas'
BOX = 'Notas'
REGEX = 'NFe - [0-9]{8} - '

box = BoxReader(EMAIL, PASS, root=ROOT).setbox(BOX)

search = 20

if len(sys.argv) == 1:
  print("Número não definido, salvando ultimos 20 e-mails")
else:
  search = sys.argv[1]

box.savelasts(REGEX, nm=search)
