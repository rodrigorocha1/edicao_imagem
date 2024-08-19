from abc import abstractmethod, ABC
from typing import Generator, Tuple
from src.service.dados.idados import IDados
import os


class Arquivo(IDados, ABC):
    def __init__(self, nome_arquivo) -> None:
        self._caminho_base = os.getcwd()
        self._nome_arquivo = nome_arquivo
        self._caminho_arquivo = os.path.join(
            self._caminho_base,
            'docs',
            self._nome_arquivo)

    @abstractmethod
    def listar_dados(self) -> Generator[Tuple[str], None, None]:
        return super().listar_dados()
