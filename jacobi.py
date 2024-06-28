import numpy as np

def jacobi(A,b,x0,toll,it_max):
    errore = 1000
    d = np.diag(A)
    n = A.shape[0]
    invM = np.diag(1/d)
    E = np.tril(A, -1)
    F = np.triu(A, 1)
    N = - (E + F)
    T = invM @ N
    autovalori=np.linalg.eigvals(T)
    raggiospettrale = np.max(np.abs(autovalori))
    print("raggio spettrale jacobi", raggiospettrale)
    it=0
    
    er_vet=[]
    while it <= it_max and errore >= toll:
        x = (N @ x0 + b) / d.reshape(n, 1) # x = invM @ N @ x0 + invM @ b
        errore=np.linalg.norm(x-x0)/np.linalg.norm(x)
        er_vet.append(errore)
        x0=x.copy()
        it=it+1
    return x,it,er_vet