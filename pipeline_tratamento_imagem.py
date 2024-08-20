from src.service.dados.arquivo import Arquivo
from src.service.dados.arquivo_planilha import ArquivoPlanilha
from src.service.service_img.editor_imagem import EditorImagem
from unidecode import unidecode


class PipelineTratamentoImagem:
    def __init__(self, arquivo: Arquivo, servico_imagem: EditorImagem) -> None:
        self.__arquivo = arquivo
        self.__servico_imagem = servico_imagem

    def rodar_pipeline_imagem(self):
        for dados in self.__arquivo.listar_dados():
            nome_arquivo_imagem_curso = dados[0]
            nome_arquivo_participandte = dados[1]
            nome_participante_tratado = unidecode(
                nome_arquivo_participandte.lower().replace(' ', '_'))
            nome_curso_tratado = unidecode(
                nome_arquivo_imagem_curso.lower().replace(' ', '_'))
            nome_arquivo_salvar_imagem = f'{nome_curso_tratado}_{nome_participante_tratado}'
            print(nome_arquivo_salvar_imagem)
            imagem = self.__servico_imagem
            imagem.abrir_imagem()
            for indice,  dado in enumerate(dados):
                coordenada = imagem.gerar_cooordenada(
                    indice=indice)
                coordenada_x = coordenada[0]
                coordenada_y = coordenada[1]
                imagem.desenhar_imagem(
                    coordenada_x=coordenada_x,
                    coordenada_y=coordenada_y,
                    valor=dado,
                    indice=indice
                )
            imagem.salvar_imagem(nome_arquivo=nome_arquivo_salvar_imagem)
            imagem.fechar_imagem()


if __name__ == '__main__':
    pti = PipelineTratamentoImagem(
        arquivo=ArquivoPlanilha(
            nome_arquivo='dados_ficticios.xlsx',

        ),
        servico_imagem=EditorImagem()
    )
    pti.rodar_pipeline_imagem()
