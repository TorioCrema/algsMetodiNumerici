import numpy as np
from SolveTriangular import Lsolve

def gauss_seidel(A,b,x0,toll,it_max):
    errore=1000
    d = np.diag(A)
    D = np.diag(d)
    E = np.tril(A, -1)
    F = np.triu(A, 1)
    M = D + E
    N = -F
    T = np.linalg.inv(M) @ N
    autovalori=np.linalg.eigvals(T)
    raggiospettrale = np.max(np.abs(autovalori))
    print("raggio spettrale Gauss-Seidel ",raggiospettrale)
    it=0
    er_vet=[]
    while it <= it_max and errore >= toll:
        temp = b - F @ x0
        x, flag = Lsolve(M, temp)
        errore=np.linalg.norm(x-x0)/np.linalg.norm(x)
        er_vet.append(errore)
        x0=x.copy()
        it=it+1
    return x,it,er_vet