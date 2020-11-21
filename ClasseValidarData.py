import os


class Data:
    dia = None
    mes = None
    ano = None

    def __init__(self, dia, mes, ano):
        self.mes = self.validarMes(mes)
        self.dia = self.validarDia(dia)
        self.ano = self.validarAno(ano)

    def validarMes(self, mes):
        (mes <= 0 or mes > 12) and self.sair('Mes invalido')
        return mes

    def validarDia(self, dia):
        diasDoMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        (dia <= 0 or dia > diasDoMes[self.mes]) and self.sair('Dia invalido')
        return dia

    def validarAno(self, ano):
        ano <= 0 and self.sair('Ano invalido')

    def sair(self, mensagem):
        print(mensagem)
        os._exit(0)
