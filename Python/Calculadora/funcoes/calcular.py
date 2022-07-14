class Calcular:
    def __init__(self, principal, valor_secundario):
        self.__principal = principal
        self.valor_secundario = valor_secundario

    def soma(self):
        resultado = self.__principal + self.valor_secundario
        self.__principal = resultado
        print(self.__principal)
    
    def subtração(self):
        resultado = self.__principal - self.valor_secundario
        self.__principal = resultado
        print(self.__principal)
    
    def multiplicação(self):
        resultado = self.__principal * self.valor_secundario
        self.__principal = resultado
        print(self.__principal)

    def divisão(self):
        resultado = self.__principal / self.valor_secundario
        self.__principal = resultado
        print(self.__principal)