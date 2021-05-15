from numpy import subtract,divide,zeros
from matplotlib import pyplot as plt
from math import ceil
from time import ctime,time
import Generate
import CalThread

class OverFit:

    def __init__(self):

        generate = Generate.Generate()
        #constantes
        self.number_threads = 1
        self.number_iteration = 1
        self.QfList = generate.n(1,102,2)
        self.nList = generate.n(20,130,5)
        self.sigma = 0.1

        self.resultado2 = zeros((len(self.QfList),len(self.nList)))
        self.resultado10 = zeros((len(self.QfList),len(self.nList)))



    def execute(self):
        self.print_time("PROG-Principal")
        qtdCiclos = len(self.nList)/self.number_threads
        qtdCiclos = int(ceil(qtdCiclos));

        for iteration in range(self.number_iteration):

            for i in range(0,self.number_threads*qtdCiclos,self.number_threads):

                arrrayOfThread = []
                numberOfThreadsCreated = 0;

                for idxThread in range(self.number_threads):
                    if idxThread + i < len(self.nList):
                        numberOfThreadsCreated= numberOfThreadsCreated + 1
                        idx     = idxThread + i;
                        arrrayOfThread.append(CalThread.CalThread(idx,self.nList,self.resultado2,self.resultado10,self.QfList,self.sigma))
                        arrrayOfThread[idxThread].start();

                for idxThread in range(numberOfThreadsCreated):
                    arrrayOfThread[idxThread].join();



            if iteration % 1000 == 0:
                resultado = subtract(self.resultado10, self.resultado2)
                resultado = divide(resultado, iteration+1)

                plt.imshow(resultado, cmap="jet", interpolation="gaussian", origin="lower", vmin=-0.2, vmax=0.2, extent=[20,130,1,100], aspect="auto")
                plt.colorbar()
                plt.savefig("charts/ic_fig_2_i="+str(iteration)+".jpg")
                plt.close()
        self.print_time("PROG-Principal")

    def print_time(self,threadName):
        print ("%s: %s" % (threadName, ctime(time())))
