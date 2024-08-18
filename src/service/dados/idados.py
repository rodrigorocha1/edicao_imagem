from abc import ABC, abstractmethod
from typing import Generator, Tuple
Generator[Tuple[str], None, None]


class IDados(ABC):

    @abstractmethod
    def listar_dados(self) -> Generator[Tuple[str], None, None]:
        """Método para retornar os dados

        Yields:
            Generator[Tuple[str], None, None]: _description_
        """
        pass
