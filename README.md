# ATIVIDADE-POO---HERANCA-CAMPUS
ATIVIDADE 02/12/2025
# Sistema de Cursos UFC — Herança em POO

Este projeto implementa o **princípio da Herança** usando Python, de acordo com a Aula 8 de POO da UFC.

## 🧱 Estrutura de Herança

### Superclasse
- `Curso`
  - nome
  - carga_horaria
  - métodos: `descricao()`, `tipo()`

### Subclasses
- `CursoGraduacao` — herda de `Curso`
- `CursoPos` — herda de `Curso`

As subclasses reescrevem (`override`) o método `descricao()` e estendem o comportamento da superclasse.

---

## 🔄 Substituição
Segundo o princípio de substituição:

> **Objetos de subclasses podem ser usados no lugar da superclasse.**

Exemplo no código:
```python
mostrar_info(curso)
