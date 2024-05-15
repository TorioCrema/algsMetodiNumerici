from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import SolveTriangular

dati = loadmat('dati.mat')
A = dati['A'].astype(float)
b = dati['b'].astype(float)

# Controllo grandezza
m, n = A.shape
print(f"m = {m}, n = {n}")
print("Matrici piu' piccole di (50 x 50) -> Piccole")
print("Matrici piu' grandi di (400 x 400) -> Grandi")

# Controllo densita'
non_zero = np.count_nonzero(A) # numero di elementi di A diversi da 0
perc = (non_zero / (m * n)) * 100 # percentuale degli elemeti di A diversi da 0
print(f"Percentuale non zero {perc}")
plt.spy(A) # mostra gli elementi diversi da 0 come celle nere, biache altrimenti
plt.show()

# Controllo simmetria
flag = A == A.T
if np.all(flag):
    print("La matrice e' simmetrica")
else:
    print("La matrice non e' simmetrica")

# Controllo definita positiva (tutti autovalori > 0)
autovalori = np.linalg.eigvals(A)
if np.all(autovalori > 0):
    print("La matrice e' difinita positiva")
else:
    print("La matrice non e' definita positiva")
