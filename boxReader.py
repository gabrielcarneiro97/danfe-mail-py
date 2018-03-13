import email
import imaplib
import os
import re
import pathlib


class BoxReader:
    imap = None
    root = None

    def __init__(self, email, password, mail_server='imap.gmail.com', root='./tmp'):

        self.root = root
        self.imap = imaplib.IMAP4_SSL(mail_server)

        pathlib.Path(root).mkdir(parents=True, exist_ok=True)

        try:
            rv, data = self.imap.login(email, password)
        except imaplib.IMAP4.error:
            print('LOGIN FAIL!')

        self.imap.select('INBOX')

    def setbox(self, box='INBOX'):
        rv, _ = self.imap.select(box)

        if rv != 'OK':
            print('Caixa {} não encontrada, Caixa de Entrada selecionada'.format(box))
            rv, _ = self.imap.select('INBOX')

        return self

    # "NFe - [0-9]{8} - "
    def saveallatts(self, rm=''):
        rv, data = self.imap.search(None, "ALL")

        regex = re.compile(rm)

        for num in reversed(data[0].split()):
            rv, data = self.imap.fetch(num, '(RFC822)')

            msg = email.message_from_bytes(data[0][1])

            self.saveatt(msg, regex)

        return self

    def savelasts(self, rm='', until=1):
        rv, data = self.imap.search(None, "ALL")

        regex = re.compile(rm)

        for num in reversed(data[0].split()):

            rv, data = self.imap.fetch(num, '(RFC822)')

            msg = email.message_from_bytes(data[0][1])

            self.saveatt(msg, regex)

            if int(num) == until:
                break

        return self

    def saveatt(self, msg, regex):
        subj = str(email.header.make_header(
            email.header.decode_header(msg['Subject'])))

        folder_name = regex.sub("", subj)

        for part in msg.walk():

            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            folder = os.path.join(self.root, folder_name)
            att_path = os.path.join(folder, filename)

            pathlib.Path(folder).mkdir(parents=True, exist_ok=True)

            file = part.get_payload(decode=True)

            if filename.endswith('.xml'):
                file = file.decode('unicode_escape').replace(
                    '\x00', '').encode('utf-8')

            if not os.path.isfile(att_path):
                fp = open(att_path, 'wb')
                fp.write(file)
                fp.close()

    def close(self):
        self.imap.logout()

        return self
