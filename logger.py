import datetime
import pathlib
import os


class Logger:
    def __init__(self, folder= os.path.join('.', 'tmp')):
        self.init = datetime.datetime.now().isoformat()
        pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
        self.path = os.path.join(folder, 'log.txt')

        with open(self.path, "a") as myfile:
            myfile.write("INIT -> {}\n".format(self.init))

    def write(self, msg):
        now = datetime.datetime.now().isoformat()
        wr = "WRITE -> {}: {}\n".format(now, msg)
        print(wr, end='')

        with open(self.path, "a") as myfile:
            myfile.write(wr)
    
    def close(self):
        now = datetime.datetime.now().isoformat()
        wr = "CLOSE -> {}\n".format(now)
        print(wr, end='')

        with open(self.path, "a") as myfile:
            myfile.write(wr)
