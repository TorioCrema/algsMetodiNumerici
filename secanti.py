import numpy as np

def secanti(fname,xm1,x0,tolx,tolf,nmax):
    """
    Implementa il metodo delle secanti per il calcolo degli zeri di un'equazione non lineare.

    Parametri:
    fname: La funzione di cui si vuole calcolare lo zero.
    xm1, x0: primi due iterati
    tolx: La tolleranza di errore tra due iterati successivi
    tolf: tolleranza sul valore della funzione
    nmax: numero massimo di iterazione

    Restituisce:
    Lo zero approssimato della funzione, il numero di iterazioni e la lista degli iterati intermedi.
    """
    xk=[]
    fxm1 = fname(xm1)
    fx0= fname(x0)
    d = fx0 * (x0 - xm1) / (fx0 - fxm1)
    x1 = x0 - d
    xk.append(x1)
    fx1=fname(x1)
    it=1
    
    while it<nmax and abs(fx1)>=tolf and abs(d)>=tolx*abs(x1):
        xm1 = x0
        x0 = x1
        fxm1 = fname(xm1)
        fx0 = fname(x0)
        d = fx0 * (x0 - xm1) / (fx0 - fxm1)
        x1 = x0 - d 
        fx1=fname(x1)
        xk.append(x1)
        it=it+1;
    
    if it==nmax:
        print('Secanti: raggiunto massimo numero di iterazioni \n')
    
    return x1,it,xk