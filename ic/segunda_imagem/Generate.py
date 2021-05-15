import numpy as np
import numpy.polynomial.legendre as l

class Generate:

    def sigmas(self,start,end,increment):
        return np.arange(start,end,increment)

    def n(self,start,end,increment):
        return list(range(start,end,increment))

    def Qf(self,star,end,increment):
        return list(range(start,end,increment))

    def matrizResultado(self,line,row):
        return np.zeros([line,row])
