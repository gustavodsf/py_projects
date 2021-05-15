import numpy as np
import Legendre
import math

class Eout:

    def calcula(self, grau, xArray, yArray, coeficientesNormalizados, step, nList, Qf):
        legendre = Legendre.Legendre()
        grau = grau + 1
        Eout = 0;
        xArrayGerado = np.ones((nList[step],grau))

        for l in range(nList[step]):
            for m in range(1,grau):
                xArrayGerado[l,m] = legendre.legendreIterativo(m,xArray[l])

        regressao = np.dot(np.linalg.pinv(xArrayGerado),yArray)

        a = 0
        b = 0

        for l in range(Qf+1):

            if (l > Qf+1):
                a = 0
            else:
                a = coeficientesNormalizados[l]
            if ((l+1) > grau):
                b = 0
            else:
                b = regressao[l]

            Eout = Eout + (math.pow((a - b),2) / ((2 * l) + 1) )
        return Eout
