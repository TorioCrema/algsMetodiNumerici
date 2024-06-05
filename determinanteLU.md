# Calcolo determinante di PA tramite fattorizzazione LU

`PA = LU` con `L` matrice triangolare inferiore con elementi diagonali uguali ad `1` e `U` matrice triangolare superiore.
Allora: `det(PA) = det(U)` dove `det(U)` e' la produttoria degli elemeti sulla diagonale di `U` (`np.prod(np.diag(U))`)
`det(P) = (-1)^s` dove `s` e' il numero di scambi effettuati.
