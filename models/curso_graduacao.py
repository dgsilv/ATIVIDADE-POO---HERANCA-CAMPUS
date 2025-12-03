from models.curso import Curso

class CursoGraduacao(Curso):
    def __init__(self, nome, carga_horaria, semestre):
        super().__init__(nome, carga_horaria)
        self.semestre = semestre

    def descricao(self):
        return f"[GRADUAÇÃO] {self.nome} ({self.semestre}º semestre) - {self.carga_horaria}h"

    def tipo(self):
        return "Curso de Graduação"
