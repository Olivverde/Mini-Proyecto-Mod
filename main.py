import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
from math import exp, pow, factorial, log

import random

class project(object):

    def __init__(self):
        pass

    def poisson(self, x, lambda_):
        res = (exp(-lambda_) * pow(lambda_, x))/factorial(x)
        return res

    def PCDF(self, xMax, lambda_):
        result = []
        cum = 0.0
        i = 0
        while i <= xMax:
            cum += self.poisson(i, lambda_)
            result.append(cum)
            i += 1

        return result

    def GPDF(x, lam, k):
        res = (lam * exp(-lam * x) * pow(lam * x, k - 1)) / factorial(k - 1)
        return res


    def exe_1(self):
        xMin = 0 
        xMax = 16 
        lambda_ = 7
        x, y = [], []
        for current in range(xMax + 1):
            x.append(current)
            y.append(self.poisson(current, lambda_))

        plt.plot(x, y)
        plt.title("Función de Probabilidad")
        plt.xlabel('Número de Huracanes')
        plt.ylabel('PRobabilidad')
        plt.show()
        y = self.PCDF(16, 7)
        # --------------------------------------
        plt.plot(x, y)
        plt.title("Función de Ditribución Acumulativa")
        plt.xlabel('Número de Huracanes')
        plt.ylabel('Probabilidad')     
        plt.show()


    def exe_2(self):
        xMin = 0 
        xMax = 100 
        lambda_ = 2

        x, y = [], []

        for current in range(xMax + 1):
            x.append(current)
            y.append(self.poisson(current, lambda_))
        
        plt.plot(x, y)
        plt.title("Probabilidad de Paradas")
        plt.xlabel('Tiempo')
        plt.ylabel('Probabilidad')
        plt.show()

    def exe_5(self):
        k = 3 
        x = np.linspace(0, 50, 1000)

        lambda_ = 2
        y1 = gamma.pdf(x, k, scale=1/lambda_)

        lambda_ = 1
        y2 = gamma.pdf(x, k, scale=1/lambda_)

        lambda_ = 0.5
        y3 = gamma.pdf(x, k, scale=1/lambda_)

        # Plot graph with three values
        plt.title("Distribución Gamma PDF")
        plt.xlabel("Tiempo")
        plt.ylabel("Densidad de Prob")
        plt.plot(x, y1, label="lambda = 2", color='green')
        plt.plot(x, y2, label="lambda = 1", color='pink')
        plt.plot(x, y3, label="lambda = 1/2", color='red')
        plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=1, fontsize=12)
        plt.ylim([0, 0.60])
        plt.xlim([0, 20])
        plt.show()



aux = project()
aux.exe_5()