from PIL import Image, ImageDraw, ImageFont
import os
from typing import Tuple
from src.enums.enums_coluna import ColunaEXCEL
from typing import Tuple


class EditorImagem:
    def __init__(self) -> None:
        self.__caminho_base = os.getcwd()
        self.__caminho_imagem = os.path.join(
            self.__caminho_base, 'docs', 'certificado_padrao.jpg')
        self.__imagem_padrao = self.abrir_imagem()
        self.__desenhar = ImageDraw.Draw(self.__imagem_padrao)
        self.__fonte_titulo = ImageFont.truetype(os.path.join(
            self.__caminho_base, 'fontes', 'ubuntu_title', 'Ubuntu-Title.ttf'), 90)
        self.__fonte_geral = ImageFont.truetype(os.path.join(os.path.join(
            self.__caminho_base, 'fontes', 'ubuntu_titling_rg',  'UbuntuTitling-Bold.ttf')), 80)
        self.__fomte_data = ImageFont.truetype(os.path.join(os.path.join(
            self.__caminho_base, 'fontes', 'ubuntu_titling_rg',  'UbuntuTitling-Bold.ttf')), 55)

    def abrir_imagem(self):
        return Image.open(self.__caminho_imagem)

    def gerar_cooordenada(self, indice: int) -> Tuple[int]:
        match indice:
            case 0:
                return 1065, 950
            case 1:
                return 1025, 827
            case 2:
                return 1440, 1065
            case 3:
                return 755, 1770
            case 4:
                return 755, 1930
            case 5:
                return 1485, 1182
            case 6:
                return 2220, 1930

    def desenhar_imagem(self, coordenada_x: int, coordenada_y: int, valor: str):
        self.__desenhar.text((coordenada_x, coordenada_y),
                             str(valor), fill='black', font=self.__fonte_geral)

    def salvar_imagem(self, nome_arquivo: str):
        caminho_salvar_imagem = os.path.join(
            self.__caminho_base, 'imagens_geradas', f'{nome_arquivo}.png')
        self.__imagem_padrao.save(caminho_salvar_imagem)
        self.__imagem_padrao.close()
