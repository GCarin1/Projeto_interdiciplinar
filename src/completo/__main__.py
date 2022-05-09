import os

#from Utils importar Utilitários
from Calculator import Calculator

def clear():
    
#Limpar tela de prompt do terminal de acordo com o sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

def displayMessageError():
    print("A opção selecionada é inválida!")

def isInteger(string):
    if string[0] == ('-', '+'):
        return string[1:].isdigit()
    else:
        return string.isdigit()

clear()

while True:
  #Lista de opções do menu
    print("[1] Converter número decimal para base binária")
    print("[2] Converter número decimal para base octal")
    print("[3] Converter número decimal para base hexadecimal")
    print("[4] Converter base binária para decimal")
    print("[5] Converter base octal para decimal")
    print("[6] Converter base hexadecimal para decimal")
    print("[7] Exibir cŕeditos")
    print("[0] Sair")

   #Menu opção selecionada pelo usuário
    menuOption = input("Informe a opção desejada: ")

    #Validação da opção selecionada no menu para não quebrar o software
    if isInteger(menuOption) == True:
        menuOption = int(menuOption)

       #Menu fluxo de trabalho de acordo com a opção selecionada
        if menuOption == 0:
            exit(0)
        elif menuOption == 1:
            numberValue = input("Informe número a ser convertido: ")
            callingCalculator = Calculator(numberValue, 10, 2)
            callingCalculator.selectWorkflow()
        elif menuOption == 2:
            numberValue = input("Informe número a ser convertido: ")
            callingCalculator = Calculator(numberValue, 10, 8)
            callingCalculator.selectWorkflow()
        elif menuOption == 3:
            numberValue = input("Informe número a ser convertido: ")
            callingCalculator = Calculator(numberValue, 10, 16)
            callingCalculator.selectWorkflow()
        elif menuOption == 4:
            numberValue = input("Informe número a ser convertido: ")
            callingCalculator = Calculator(numberValue, 2, 10)
            callingCalculator.selectWorkflow()
        elif menuOption == 5:
            numberValue = input("Informe número a ser convertido: ")
            callingCalculator = Calculator(numberValue, 8, 10)
            callingCalculator.selectWorkflow()
        elif menuOption == 6:
            numberValue = input("Informe número a ser convertido: ")
            callingCalculator = Calculator(numberValue, 16, 10)
            callingCalculator.selectWorkflow()
        elif menuOption == 7:
            clear()

            print("\t\tCréditos")
            print("-----------------------------------------")
            print("Guilherme Carini\t\tRGM: 20224435")
            print("Gabriel Pena\t\t\tRGM: 18777651")
            print("Ayrton Feliciano\t\t\tRGM: 29641977")
            print("Nathan de Oliveira\t\tRGM: 30271754")
            print("Nikolas Yan da Silva\t\tRGM: 29908027")
            print("-----------------------------------------")
        else:
            displayMessageError()
    else:
        displayMessageError()

    input("Pressione a tecla ENTER para continuar...")

    clear()
