import threading
from numpy import random
import Legendre
import Eout


class CalThread(threading.Thread):

    def __init__(self,i,nList,resultado2,resultado10,QfList,sigma):
        threading.Thread.__init__(self)
        self.idx = i
        self.nList = nList
        self.resultado2 = resultado2
        self.resultado10 = resultado10
        self.QfList = QfList
        self.sigma = sigma

    def run(self):
        eout = Eout.Eout()
        legendre = Legendre.Legendre()
        for j in range(len(self.QfList)):
            xArray = random.uniform(-1, 1, self.nList[self.idx])
            coeficientesNormalizados = legendre.geraCoeficientes(self.QfList[j])
            yArray = legendre.gerandoFuncaoAlvo(xArray,self.sigma,self.nList,self.QfList[j],self.idx,coeficientesNormalizados)

            self.resultado2[j,self.idx]  = self.resultado2[j,self.idx] + eout.calcula(2, xArray, yArray, coeficientesNormalizados, self.idx, self.nList,self.QfList[j])
            self.resultado10[j,self.idx] = self.resultado10[j,self.idx] + eout.calcula(10, xArray, yArray, coeficientesNormalizados, self.idx,self.nList,self.QfList[j])
