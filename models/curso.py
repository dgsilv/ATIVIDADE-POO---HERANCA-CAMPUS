class Curso:
    def __init__(self, nome, carga_horaria):
        self.nome = nome
        self.carga_horaria = carga_horaria

    def descricao(self):
        return f"{self.nome} - {self.carga_horaria}h"

    def tipo(self):
        return "Curso"
