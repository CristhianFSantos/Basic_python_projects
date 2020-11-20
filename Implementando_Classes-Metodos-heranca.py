from typing import List


class Pessoa:
    nome = None
    idade = None
    endereco = None

    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return nome

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEndereco(self):
        return endereco

    def setIdade(self, idade):
        self.idade = idade

    def getIdade(self):
        return idade


class Professor(Pessoa):
    salario = None
    curriculo = None

    def __init__(self, salario, curriculo, nome, idade, endereco):
        self.salario = salario
        self.curriculo = curriculo
        super().__init__(nome, idade, endereco)

    def setSalario(self, salario):
        self.salario = salario

    def getSalario(self):
        return salario

    def setCurriculo(self, curriculo):
        self.curriculo = curriculo

    def getCurriculo(self):
        return curriculo

    def printCurriculo(self):
        print(self.curriculo)


class Disciplina:
    nome: str = None
    horaAula: int = None

    def __init__(self, nome, horaAula):
        self.horaAula = horaAula
        self.nome = nome


class Aluno(Pessoa):
    matricula: int = None
    curso: str = None
    disciplinas: List[Disciplina] = []

    def __init__(self, matricula, curso, nome, idade, endereco):
        self.matricula = matricula
        self.curso = curso
        super().__init__(nome, idade, endereco)

    def getMatricula(self):
        return matricula

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getCurso(self):
        return curso

    def setCurso(self, curso):
        self.curso = curso

    def addDisciplina(self, disciplina: Disciplina):
        self.disciplinas.append(disciplina)


objAluno = Aluno(123, 'Adm', 'Bruna', 23, 'Av 5')
objAluno.addDisciplina(Disciplina('Sistema de Informação', 800))
print(objAluno.disciplinas)