from models.curso import Curso
from models.curso_graduacao import CursoGraduacao
from models.curso_pos import CursoPos

def mostrar_info(curso):



    print("\n--- Informações do curso ---")
    print(curso.descricao())
    print("Tipo:", curso.tipo())


    if isinstance(curso, CursoPos):
        print("Este curso é de pós-graduação. A modalidade é:", curso.modalidade)

def main():
    print("===== SISTEMA DE CURSOS UFC - HERANÇA =====")

    print("\n1) Criando um curso comum (superclasse)...")
    c1 = Curso("Inglês Instrumental", 60)
    mostrar_info(c1)

    print("\n2) Criando curso de graduação (subclasse)...")
    c2 = CursoGraduacao("Ciência da Computação", 3600, 2)
    mostrar_info(c2)

    print("\n3) Criando curso de pós (subclasse)...")
    c3 = CursoPos("Segurança da Informação", 420, "Lato Sensu")
    mostrar_info(c3)


    print("\n4) Exemplo de 'coerção' — tratar superclasse como subclasse (NÃO RECOMENDADO):")
    try:
        coerced = CursoPos(c1.nome, c1.carga_horaria, "Lato Sensu")
        print("Coerção funcionou!")
        mostrar_info(coerced)
    except Exception as e:
        print("Falha na coerção:", e)


if __name__ == "__main__":
    main()
