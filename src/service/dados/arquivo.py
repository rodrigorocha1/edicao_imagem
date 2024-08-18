from abc import abstractmethod, ABC
from typing import Generator, Tuple
from src.service.dados.idados import IDados
import os


class Arquivo(IDados, ABC):
    def __init__(self, nome_arquivo) -> None:
        self.__caminho_base = os.getcwd()
        self.__nome_arquivo = nome_arquivo
        self.__caminho_arquivo = os.path.join(
            self.__caminho_base,
            'docs',
            self.__nome_arquivo)

    @abstractmethod
    def listar_dados(self) -> Generator[Tuple[str], None, None]:
        return super().listar_dados()
