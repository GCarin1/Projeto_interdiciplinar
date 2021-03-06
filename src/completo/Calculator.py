from Utils import Utils

class Calculator:
    def __init__(self, numberValue, numberBaseCurrent, numberBaseTarget):
        self.numberValue = str(numberValue)
        self.numberBaseCurrent = numberBaseCurrent
        self.numberBaseTarget = numberBaseTarget

        #Divida cada dígito em um índice diferente dentro do array
        self.arrayStringNormal = list(self.numberValue)
        self.arrayStringNormal = Utils.convertArrayWithLettersToNumbers(self.arrayStringNormal)
        self.arrayNumberNormal = [ int(x) for x in self.arrayStringNormal ]
        self.arrayStringInverted = list(reversed(self.arrayStringNormal))
        self.arrayNumberInverted = [ int(x) for x in self.arrayStringInverted ]
        
        
        self.numberValue = self.numberValue

    def selectWorkflow(self):
        callingUtils = Utils(self.arrayNumberInverted, self.numberValue, self.numberBaseCurrent, self.numberBaseTarget)
        
        callingUtils.displayAllInfo()

        #Fluxo de trabalho de cálculo da estrutura de decisão
        if self.numberBaseCurrent == self.numberBaseTarget:
            result = self.numberValue
        elif self.numberBaseCurrent > 10:
            result = callingUtils.convertBaseMethodMultiplier(self.arrayNumberNormal)
        elif self.numberBaseTarget > 10:
            result = callingUtils.convertBaseMethodDivider(self.numberValue)
        else:
            if self.numberBaseCurrent <= self.numberBaseTarget:
                result = callingUtils.convertBaseMethodMultiplier(self.numberValue)
            elif self.numberBaseCurrent >= self.numberBaseTarget:
                result = callingUtils.convertBaseMethodDivider(self.numberValue)

        #Display results
        callingUtils.displayResult(result)
        return result