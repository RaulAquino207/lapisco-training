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
        self.most_frequent()

    def most_frequent(self):
        self.chain_code_mode = []
        col = 0
        print(self.chain_codes.shape[1])
        while (col != self.chain_codes.shape[1]):
            aux = self.chain_codes.transpose()[col]
            aux2 = []
            # print(aux)
            # value = statistics.mode(aux)
            test = Counter(aux)
            # print('Counter')
            # print(test)
            if (len(test) == 1):
                for i in test:
                    self.chain_code_mode.append(i)
            else:
                rand = random.randint(0, 1)
                for i in test:
                    aux2.append(i)
                # print(aux2)
                # print(rand)
                # print(aux2[rand])
                self.chain_code_mode.append(aux2[rand])

            # self.chain_code_mode.append(value)
            col = col + 1

        return (self.chain_code_mode)
