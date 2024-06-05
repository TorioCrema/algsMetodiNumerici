# Calcolo determinante di PA tramite fattorizzazione LU

$PA = LU$ con $L$ matrice triangolare inferiore con elementi diagonali uguali ad $1$ e $U$ matrice triangolare superiore.
Allora: $det(PA) = det(U)$ dove $det(U)$ e' la produttoria degli elemeti sulla diagonale di $U$: $\prod^n_{i=1}u_{ii}$ (`np.prod(np.diag(U))`)
$det(P) = (-1)^s$ dove $s$ e' il numero di scambi effettuati.

```py
A = np.array([[4.5, 1, 3, 2], [1, -8, 2, 1], [-1, -2, -3, -1], [2, 6, 0, 1]], dtype=float)

P, L, U = scipy.linalg.lu(A)
print(P) #Se P = I det(P) = 1
du = np.diag(U)
print(np.prod(du))
print(np.linalg.det(A))
```
