# Metodi di soluzione per sistemi Ax = b

## Matrice A quadrata (n x n)

### Piccole dimensioni e densa

Se ben condizionata:

- Fattorizzazione di Gauss
  - La fattorizzazione di Gauss esiste se ogni sottomatrice di testa di A formata dalle prime `k` righe e le prime `k` colonne di A con `k = 1,...,n-1` e' non singolare, cioe' ha determinante diverso da 0.

Se mal condizionata:

- Fattorizzazione QR
  - La fattorizzazione QR di A `(n x n)` esiste se `rank(A) = n`

Se simmetrica e definita positiva

- Fattorizzazione di Cholesky (`A = L @ L.T`)

### Grandi dimensioni e sparsa

Se a diagonale strettamente dominante (ogni elemento della diagonale != 0):

- Jacobi
- Gauss Seidel
- Gauss Seidel SOR

Se simmetrica e definita positiva

- Gauss Seidel
- Gauss Seidel SOR
- Metodo di discesa del gradiente
- Metodo di discesa del gradiente coniugato

## Matrice A rettangolare (m x n), m > n

Se ben condizionata (`<= 10^2`) e a rango massimo:

- Metodo delle equazioni normali

Se mediamente condizionata (`10^3` o `10^4`) e a rango massimo:

- Metodo QRLS

Se altamente mal condizionata (`> 10^4`) e non a rango massimo:

- Metodo SVDLS
