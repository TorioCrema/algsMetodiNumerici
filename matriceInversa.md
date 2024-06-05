# Calcolo della matrice inversa tramite fatt LU

Sia $PA = LU$ calcoliamo $A^{-1}$ una colonna alla volta:

```py
A = np.array([[4.5, 1, 3, 2], [1, -8, 2, 1], [-1, -2, -3, -1], [2, 6, 0, 1]], dtype=float)

P, L, U = scipy.linalg.lu(A)
Icol = np.zeros((A.shape[0], 1)) # vettore colonna di n righe
invA = np.zeros_like(A)
# Vogliamo risolvere LUx = i dove i e' la i-esima colonna di I
for i in range(A.shape[0]):
    icol = Icol.copy()
    icol[i] = 1 # colonna i-esima di I
    y, _ = SolveTriangular.Lsolve(L, icol) # risolviamo Ly = colonna i-esima di I
    invCol, _ = SolveTriangular.Usolve(U, y) # risolviamo Ux = y
    for j in range(A.shape[0]):
        invA[j, i] = invCol[j,0]
print(invA)
```
