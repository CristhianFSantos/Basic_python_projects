class ConversaoDeUnidadesDeArea:
    @staticmethod
    def conversaoMetroPes(valor):
        resultado = int(valor) * 10.76
        return resultado

    @staticmethod
    def conversaoPesCent(valor):
        resultado = int(valor) * 30.48
        return resultado

    @staticmethod
    def conversaoMilhaAcre(valor):
        resultado = int(valor) * 640
        return resultado

    @staticmethod
    def conversaoAcrePes(valor):
        resultado = int(valor) * 43560
        return resultado
