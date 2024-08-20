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
        self.__tamanho_fonte_primaria = 100
        self.__tamanho_fonte_secundaria = 35
        self.__fonte_primaria = ImageFont.truetype(os.path.join(os.path.join(
            self.__caminho_base, 'fontes', 'PinyonScript-Regular.ttf')), self.__tamanho_fonte_primaria)
        self.__fonte_secundaria = ImageFont.truetype(os.path.join(os.path.join(
            self.__caminho_base, 'fontes', 'ArbutusSlab-Regular.ttf')), self.__tamanho_fonte_secundaria)

    def abrir_imagem(self):
        self.__imagem_padrao = Image.open(self.__caminho_imagem)
        self.__desenhar = ImageDraw.Draw(self.__imagem_padrao)

    def __escolher_fonte(self, indice: int) -> ImageFont.FreeTypeFont:
        return self.__fonte_primaria if indice == 1 else self.__fonte_secundaria

    def gerar_cooordenada(self, indice: int) -> Tuple[int]:
        match indice:
            case 0:
                return 855, 755
            case 1:
                return 690, 570
            case 2:
                return 228, 880
            case 3:
                return 822, 820
            case 4:
                return 1200, 820
            case 5:
                return 1048, 880
            case 6:
                return 1132, 940

    def desenhar_imagem(self, coordenada_x: int, coordenada_y: int, valor: str, indice: int):
        self.__desenhar.text((coordenada_x, coordenada_y),
                             str(valor), fill='black', font=self.__escolher_fonte(indice=indice))

    def salvar_imagem(self, nome_arquivo: str):
        caminho_salvar_imagem = os.path.join(
            self.__caminho_base, 'imagens_geradas', f'{nome_arquivo}.png')

        self.__imagem_padrao.save(caminho_salvar_imagem)

    def fechar_imagem(self):
        self.__imagem_padrao.close()
