import numpy as np

def newton_mod(fname,fpname,m,x0,tolx,tolf,nmax):
    """
    Implementa il metodo di Newton modificato da utilizzato per il calcolo degli zeri di un'equazione non lineare
    nel caso di zeri multipli.
    Convergenza locale, ordine p = 2.

    Parametri:
    fname: La funzione di cui si vuole calcolare lo zero.
    fpname: La derivata prima della funzione di  cui si vuole calcolare lo zero.
    m: molteplicità della radice
    x0: iterato iniziale
    tolx: La tolleranza di errore tra due iterati successivi
    tolf: tolleranza sul valore della funzione
    nmax: numero massimo di iterazione

    Restituisce:
    Lo zero approssimato della funzione, il numero di iterazioni e la lista degli iterati intermedi.
    """ 

    xk = []
    fx0 = fname(x0)
    if abs(fpname(x0)) <= np.spacing(1):
        print("Derivata prima nulla in x0")
        return None, None, None

    d = m * fx0 / fpname(x0)
    x1 = x0 - d
    
    fx1 = fname(x1)
    xk.append(x1)
    it=1
    
    while it < nmax and abs(fx1) >= tolf and abs(d) >= tolx * abs(x1):
        x0 = x1
        fx0 = fname(x0)
        if abs(fpname(x0)) <= np.spascing(1): #Se la derivata prima e' pià piccola della precisione di macchina stop
            print("Derivata prima nulla in x0")
            return None, None, None
        d = m * fx0 / fpname(x0)
        
        x1 = x0 - d
        fx1 = fname(x1)
        it = it + 1
        
        xk.append(x1)
        
    if it == nmax:
        print('Raggiunto massimo numero di iterazioni')
        
    return x1, it, xk