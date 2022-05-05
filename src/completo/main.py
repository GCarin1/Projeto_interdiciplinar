
from Calculator import Calculator

#Declarando as variáveis ​​globais (pelo método de entrada)
numberValue = input("Valor numérico: ") #As letras devem ser definidas como maiúsculas
numberBaseCurrent = int(input("Base numérica atual: "))
numberBaseTarget = int(input("Base numérica desejada: "))


callingCalculator = Calculator(numberValue, numberBaseCurrent, numberBaseTarget)


callingCalculator.selectWorkflow()