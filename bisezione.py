import numpy as np
import math

def sign(x):
    return math.copysign(1, x)

def metodo_bisezione(fname, a, b, tolx,tolf):
    """
    Implementa il metodo di bisezione per il calcolo degli zeri di un'equazione non lineare.

    Parametri:
    f: La funzione da cui si vuole calcolare lo zero.
    a: L'estremo sinistro dell'intervallo di ricerca.
    b: L'estremo destro dell'intervallo di ricerca.
    tol: La tolleranza di errore.

    Restituisce:
    Lo zero approssimato della funzione, il numero di iterazioni e la lista di valori intermedi.
    """
    fa=fname(a)
    fb=fname(b)
    if sign(fa) * sign(fb) > 0:
        print("Non è possibile applicare il metodo di bisezione \n")
        return None, None,None

    it = 0
    v_xk = []

    maxit = math.ceil(math.log((b - a) / tolx) / math.log(2))-1

    
    while it <= maxit and abs(b - a) > tolx:
        xk = a + (b - a) / 2 
        v_xk.append(xk)
        it += 1
        fxk=fname(xk)
        if fxk==0:
            return xk, it, v_xk

        
        if sign(fa)*sign(fxk)>0:   
            a = xk
            fa = fxk
        elif sign(fxk)*sign(fb)>0:    
            b = xk
            fb = fxk
    
    return xk, it, v_xk