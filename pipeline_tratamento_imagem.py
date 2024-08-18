from src.service.dados.arquivo_planilha import Arquivo

from typing import Union


class PipelineTratamentoImagem:
    def __init__(self, arquivo: Arquivo) -> None:
        self.__arquivo = arquivo

    def rodar_pipeline_imagem(self):
        for dados in self.__arquivo.listar_dados():
            print(dados)


if __name__ == '__main__':
