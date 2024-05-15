import numpy as np
import scipy

def SVDLS(A,b):
    #Risolve un sistema sovradeterminato con il metodo SVD-LS
    m, n = A.shape  #numero di righe e  numero di colonne di A
    U, s, VT = scipy.linalg.svd(A)  #Attenzione : Restituisce U, il numpy-array 1d che contiene la diagonale della matrice Sigma e VT=VTrasposta)
    #Quindi 
    V = VT.T
    thresh = np.spacing(1)*m*s[0] ##Calcolo del rango della matrice, numero dei valori singolari maggiori di una soglia
    k = np.count_nonzero(s>thresh)
    print("rango=", k)
    d = U.T @ b
    d1 = d[:k].reshape(k, 1)
    s1 = s[:k].reshape(k, 1)
    #Risolve il sistema diagonale di dimensione kxk avene come matrice dei coefficienti la matrice Sigma
    c = d1 / s1
    x=V[:,:k]@c 
    residuo=np.linalg.norm(d[k:])**2
    return x,residuo