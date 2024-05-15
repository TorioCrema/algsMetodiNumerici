import numpy as np
import scipy
from SolveTriangular import Usolve

def qrLS(A,b):
    #Risolve un sistema sovradeterminato con il metodo QR-LS
    n = A.shape[1]  # numero di colonne di A
    Q, R = scipy.linalg.qr(A)
    h = Q.T @ b
    x, flag = Usolve(R[0:n,:], h[0:n])
    residuo = np.linalg.norm(h[n:])**2
    return x, residuo