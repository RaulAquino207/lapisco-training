import numpy as np
import statistics
from collections import Counter
import random

'''
Código 5: Utilizando o Código 3, desenhe um número baseado na moda
das cadeias geradas pelo Código 4. Adicione uma aleatoriedade para
criar novos números a cada execução do código.
'''

class ModeChainCode():
    def __init__(self, chain_codes):
        self.chain_codes = np.array(chain_codes)
        print(self.chain_codes.shape)
        self.most_frequent()

    def most_frequent(self):
        self.chain_code_mode = []
        col = 0
        print(self.chain_codes.shape)
        print(self.chain_codes.shape[1])
        while (col != self.chain_codes.shape[1]):
            aux = self.chain_codes.transpose()[col]
            # print(aux)
            value = statistics.multimode(aux)
            # print(value)
            if (len(value) == 1):
                self.chain_code_mode.append(value[0])
            else:
                rand = random.randint(0, 1)
                self.chain_code_mode.append(value[rand])
            col = col + 1
    
        print(self.chain_code_mode)
        return (self.chain_code_mode)
