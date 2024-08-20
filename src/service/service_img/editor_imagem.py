from PIL import Image, ImageDraw, ImageFont
import os
from typing import Tuple
from typing import Tuple


class EditorImagem:
    def __init__(self) -> None:
        self.__caminho_base = os.getcwd()
        self.__caminho_imagem = os.path.join(
            self.__caminho_base, 'imagens_originais',  'dois.png')
        self.__imagem_padrao = None
        self.__desenhar = None
        self.__tamanho_fonte_primaria = 71
        self.__tamanho_fonte_secundaria = 30
        self.__fonte_primaria = ImageFont.truetype(os.path.join(os.path.join(
            self.__caminho_base, 'fontes', 'AlexBrush-Regular.ttf')), self.__tamanho_fonte_primaria)
        self.__fonte_secundaria = ImageFont.truetype(os.path.join(os.path.join(
            self.__caminho_base, 'fontes', 'Poppins-Regular.ttf')), self.__tamanho_fonte_secundaria)

    def abrir_imagem(self):
        self.__imagem_padrao = Image.open(self.__caminho_imagem)
        self.__desenhar = ImageDraw.Draw(self.__imagem_padrao)

    def __escolher_fonte(self, indice: int) -> ImageFont.FreeTypeFont:
        return self.__fonte_primaria if indice == 1 else self.__fonte_secundaria

    def gerar_cooordenada(self, indice: int) -> Tuple[int]:
        match indice:
            case 0:
                return 420, 648
            case 1:
                return 700, 480
            case 2:
                return 500, 695
            case 3:
                return 438, 750
            case 4:
                return 500, 793
            case 5:
                return 456, 845
            case 6:
                return 500, 896

    def desenhar_imagem(self, coordenada_x: int, coordenada_y: int, valor: str, indice: int):
        self.__desenhar.text((coordenada_x, coordenada_y),
                             str(valor), fill='black', font=self.__escolher_fonte(indice=indice))

    def salvar_imagem(self, nome_arquivo: str):
        caminho_salvar_imagem = os.path.join(
            self.__caminho_base, 'imagens_geradas', f'{nome_arquivo}.png')

        self.__imagem_padrao.save(caminho_salvar_imagem)

    def fechar_imagem(self):
        self.__imagem_padrao.close()
