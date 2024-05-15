import numpy as np
import scipy
from SolveTriangular import Lsolve, Usolve

def eqnorm(A,b):
    #Risolve un sistema sovradeterminato con il metodo delle equazioni normali
    G = A.T @ A
    f = A.T @ b
    
    L = scipy.linalg.cholesky(G, lower=True)
    U = L.T
        
   
    z, flag = Lsolve(L, f)
    if flag == 0:
        x, flag = Usolve(U, z)
    
    return x