import matplotlib.pyplot as plt

'''
4. Código 4: Implemente o algoritmo para ajustar o tamanho do código
da cadeia de todos os números. Todos deverão ter o mesmo tamanho.
'''

class BlackBox():
    def __init__(self, chain_codes, signals):
        self.chain_codes = chain_codes
        self.signals = signals
        self.black_box_normalization()

    def black_box_normalization(self):
        self.new_chain_codes = []
        # print(self.chain_codes)
        # print(self.signals)
        self.smaller = 9999
        for value in self.signals:
            if value < self.smaller:
                self.smaller = value
                # print('smaller', smaller)

        print('the smaller', self.smaller)

        for i in range(len(self.signals)):
            proportion = self.signals[i] / self.smaller
            # print(self.signals[i], self.smaller)
            # print(proportion)
            aux = []
            idx = 0
            rest = 0
            if (self.signals[i] == self.smaller):
                self.new_chain_codes.append(self.chain_codes[i])
                plt.plot(self.chain_codes[i])
                plt.show()
            else:
                while (len(aux) != self.smaller):
                    # print(proportion)
                    # print(idx, self.smaller)
                    # print(self.chain_codes[i][idx])
                    aux.append(self.chain_codes[i][idx])
                    rest = (rest + proportion) % 1
                    idx = (int(idx + proportion + rest)//1)
                    # print(len(aux))

                self.new_chain_codes.append(aux)
                plt.plot(aux)
                plt.show()

        return (self.new_chain_codes)