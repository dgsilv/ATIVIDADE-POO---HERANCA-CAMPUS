from models.curso import Curso

class CursoPos(Curso):
    def __init__(self, nome, carga_horaria, modalidade):
        super().__init__(nome, carga_horaria)
        self.modalidade = modalidade  # ex: Lato Sensu / Stricto Sensu

    def descricao(self):
        return f"[PÓS] {self.nome} - {self.modalidade} - {self.carga_horaria}h"

    def tipo(self):
        return "Curso de Pós-Graduação"
