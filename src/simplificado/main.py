import os 
import time

class init:
    
    def decB(self):    
                
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[Calculadora Decimal para outras bases\n\n")
            print("[1] Decimal para binário")
            print("[2] Decimal para octal")
            print("[3] Decimal para hexa")
            print("[0] Voltar\n")
                   
            op = int(input('Digite uma opção: '))

            if(op==0): break
            if(op==1): self.convertDB()
            if(op==2): self.convertDO()
            if(op==3): self.convertDH()
            if(op<0 or op>3):
                print("Input invalido, digite novamente...")
                time.sleep(3)
                self.decB()

    def convertDB(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            num=int(input("Digite um valor para ser convertido de Decimal para Binario\n: "))
            print('\n')
            convert = format(num, "b")
            print(f'({num})10 --- ({convert})2')
            print('\n')

            op=int(input("Programa executado com sucesso!\nOque deseja fazer agora ?\n[1] Voltar para o menu\n[2] Executar novamente\n[0] Voltar\n\nDigite uma opção:"))
            if(op==0): break
            if(op==1): self.decB()
            if(op==2): self.convertDB()
            if(op<0 or op>3):
                print("Input invalido, digite novamente...")
                time.sleep(3)
                self.convertDB()

    def convertDO(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            num=int(input("Digite um valor para ser convertido de Decimal para Octal\n: "))
            print('\n')
            convert = format(num, "o")
            print(f'({num})10 --- ({convert})8')
            print('\n')

            op=int(input("Programa executado com sucesso!\nOque deseja fazer agora ?\n[1] Voltar para o menu\n[2] Executar novamente\n[0] Voltar\n\nDigite uma opção:"))
            if(op==0): break
            if(op==1): self.decB()
            if(op==2): self.convertDO()
            if(op<0 or op>3):
                print("Input invalido, digite novamente...")
                time.sleep(3)
                self.convertDO()
    
    def convertDH(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            num=int(input("Digite um valor para ser convertido de Decimal para Hexadecimal\n: "))
            num=format(num,"b")
            print('\n')
            convert = format(num, "x")
            print(f'({num})10 --- ({convert})16')
            print('\n')

            op=int(input("Programa executado com sucesso!\nOque deseja fazer agora ?\n[1] Voltar para o menu\n[2] Executar novamente\n[0] Voltar\n\nDigite uma opção:"))
            if(op==0): break
            if(op==1): self.decB()()
            if(op==2): self.convertDH()
            if(op<0 or op>3):
                print("Input invalido, digite novamente...")
                time.sleep(3)
                self.convertDH()

   

   

start=init()
start.decB()