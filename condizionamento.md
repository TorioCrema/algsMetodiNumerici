# Condizionamento dei problemi

## Calcolo degli zeri di una funzione non lineare

$K = \frac{1}{\lvert f'(\alpha) \rvert}$

Quindi se $\lvert f'(\alpha) \rvert$ e' molto piccolo, allora il problema e' mal condizionato.
Questo significa che il calcolo di radici multiple di molteplicita' $m > 1$ (quelle in cui oltre la funzione si annullano anche le sue derivate fino all'ordine $m-1$) e' un problema molto difficile.

## Soluzione di sistemi lineari

Dipende dal condizionameto della matrcice dei coefficienti $K(A)$, l'indice di condizionamento in norma 2 e' definito come:
$$K = \frac{\sqrt{\lambda_{max}(A^TA)}}{\sqrt{\lambda_{min}(A^TA)}}$$

## Sistemi sovradeterminati nel senso dei minimi quadrati

### Equazioni normali

Con il metodo delle equazioni normali vogliamo risolvere il sistema $A^TAx=A^Tb$, poiche':
$$K(A^TA) = (K(A))^2$$
il sistema delle equazioni normali puo' essere mal condizionato anche quando il problema nella sua forma originale non lo e'. Utilizziamo le equazioni normali solo con matrici $A$ ben condizionate.

### QRLS

Con il metodo RQLS risolviamo il sistema $R_1x = h_1$ ottenuto tramite la fattorizzazione QR della matrice $A$. Quindi l'indice di condizionamento rimane quello della matrice originale.
