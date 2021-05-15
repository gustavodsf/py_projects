from numpy import random,zeros,ones,divide
from math import pow,sqrt

class Legendre:
    def legendreIterativo(self,grau,x):
        if grau == 0:
            return 1.0
        elif grau == 1:
            return x
        else:
            legendre = 0
            legendre0 = ones(x.shape)
            legendre1 = x
            for idx in  range(2,grau+1):
                legendre = ( (2 * idx - 1) / idx) * x * legendre1 - ((idx - 1) / idx) * legendre0
                legendre0 = legendre1
                legendre1 = legendre
            return legendre

    def geraCoeficientes(self,Qf):
        coeficientes = random.randn(Qf+1)
        k = 0
        for l in range(Qf+1):
            k = k + (pow(coeficientes[l],2) / (2 * l + 1))
        return divide(coeficientes,sqrt(2*k))

    def gerandoFuncaoAlvo(self,xArray,sigma,nlist,Qf,i,coeficientes):
        eArray = random.randn(nlist[i])
        yArray = zeros(nlist[i])
        for l in range(nlist[i]):
            valor = 0
            for m in range(Qf+1):
                valor = valor + (coeficientes[m] * self.legendreIterativo(m,xArray[l]))
            yArray[l] = valor + (sqrt(sigma) * eArray[l])
        return yArray
