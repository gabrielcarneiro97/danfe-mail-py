import datetime
import pathlib
import os


class Logger:
    """Classe Logger.

    Attributes:
        init (str): atributo que guarda o momento da inicialização da instância.
        path (str): guarda o caminho do arquivo 'log.txt' 
    """
    init = None
    path = None

    def __init__(self, folder= os.path.join('.', 'tmp')):
        """Metodo __init__ da classe Logger.

        Metodo de inicialização da classe.
        
        Args:
            folder (str): contém o diretório onde o 'log.txt' será salvo, tem como default './tmp'.
        """
        self.init = datetime.datetime.now().isoformat()
        pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
        self.path = os.path.join(folder, 'log.txt')

        with open(self.path, "a") as myfile:
            myfile.write("INIT -> {}\n".format(self.init))

    def write(self, msg):
        """Metodo write da classe Logger.

        Metodo recebe uma mensagem para ser escrita no log que é ao mesmo tempo impressa na tela.

        Args:
            msg (str): mensagem a ser impressa na tela e escrita no log.
        """
        now = datetime.datetime.now().isoformat()
        wr = "WRITE -> {}: {}\n".format(now, msg)
        print(wr, end='')

        with open(self.path, "a") as myfile:
            myfile.write(wr)
    
    def close(self):
        """Metodo close da classe Logger.
        
        Quando esse metodo é chamado ele grava uma mensagem expecifica que registra quando ele foi chamado,
            para sinalizar o final de um ciclo.
        """
        now = datetime.datetime.now().isoformat()
        wr = "CLOSE -> {}\n".format(now)
        print(wr, end='')

        with open(self.path, "a") as myfile:
            myfile.write(wr)
