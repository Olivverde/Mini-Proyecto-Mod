from time import time
import numpy as np
from scipy.stats import gamma, uniform, poisson, expon
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

    def exe_3(self):
        # poisson con distribucion exponencial para tiempos
        lambda_ = 5 # pacientes por hora
        inverse_cdf = lambda x: -log(1 - x) / lambda_
        # tiempos de espera para los primeros 10 pacientes
        times = [inverse_cdf(random.random()) for _ in range(10)]
        for paciente in range(10):
            if paciente == 0:
                print(f'El tiempo para la ocurrencia del paciente {paciente+1} es {times[paciente]} horas')
            else:
                print(f'El tiempo entre la ocurrencia del paciente {paciente} y el {paciente+1} es {times[paciente]} horas')
        # suma de todos los tiempos de espera
        print(f'El tiempo total transcurrido es es {sum(times)} horas')
        # plot de la cdf de distribucion de tiempos de espera
        x = np.linspace(0, 2, 1000)
        y = expon.cdf(x, scale=1/lambda_)
        plt.plot(x, y)
        plt.title("Distribución Exponencial")
        plt.xlabel("Tiempo (horas)")
        plt.ylabel("Probabilidad")
        plt.show()
        # tiempos para los primeros 500 pacientes
        times = [inverse_cdf(random.random()) for _ in range(500)]
        # grafica de dispersion de tiempos de espera
        plt.plot(range(500), times, linestyle='solid')
        plt.title("Tiempos de Espera")
        plt.xlabel("Paciente")
        plt.ylabel("Tiempo (horas)")
        plt.show()
        # cdf de los tiempos de espera para los primeros 500 pacientes
        c_times = [sum(times[:i+1]) for i in range(len(times))]
        plt.plot(range(500), c_times, linestyle='solid')
        plt.title("Tiempos de Espera acumulados")
        plt.xlabel("Paciente")
        plt.ylabel("Tiempo (horas)")
        plt.show()

    def exe_4(self):
        # simulacion de tiempos
        lambda_ = 5 # pacientes por hora
        inverse_cdf = lambda x: -log(1 - x) / lambda_
        # tiempos de espera para los primeros 10 pacientes
        times = [inverse_cdf(random.random()) for _ in range(100)]
        c_times = [sum(times[:i+1]) for i in range(len(times))]
        x = np.linspace(0, max(c_times), 10000)
        # c_times array to numpy array
        c_times = np.array(c_times)
        x = np.append(x, c_times)
        # order the np array
        x.sort()
        y = [1 if time in c_times else 0 for time in x]
        plt.plot(x, y)
        plt.title("Simulación de currencias de los primeros 100 pacientes")
        plt.xlabel("Tiempo (horas)")
        plt.ylabel("Ocurrencia")
        plt.show()
        # pmf
        patients = []
        for i in range(100):
            patients.append(self.poisson(i, lambda_))
        # plot of the distribution of patients
        plt.plot(patients)
        plt.title("Distribución de Pacientes")
        plt.xlabel("Paciente")
        plt.ylabel("Probabilidad")
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
aux.exe_1()