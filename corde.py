import numpy as np

def corde(fname,m,x0,tolx,tolf,nmax):
    """
    Implementa il metodo delle corde per il calcolo degli zeri di un'equazione non lineare.

    Parametri:
    fname: La funzione da cui si vuole calcolare lo zero.
    m: coefficiente angolare della retta che rimane fisso per tutte le iterazioni
    tolx: La tolleranza di errore tra due iterati successivi
    tolf: tolleranza sul valore della funzione
    nmax: numero massimo di iterazione

    Restituisce:
    Lo zero approssimato della funzione, il numero di iterazioni e la lista degli iterati intermedi.
    """
    xk=[]
    fx0 = fname(x0)
    d = fx0 / m
    x1 = x0 - d
    fx1 = fname(x1)
    xk.append(x1)
    it=1
    
    while  it < nmax and abs(fx1) >= tolf and abs(d) >= tolx * abs(x1):
        x0 = x1
        fx0 = fname(x0)
        d = fx0 / m
        '''
        #x1= ascissa del punto di intersezione tra  la retta che passa per il punto
        (xi,f(xi)) e ha pendenza uguale a m  e l'asse x
        '''
        x1 = x0 - d
        fx1=fname(x1)
        it=it+1
        
        xk.append(x1)
        
    if it == nmax:
        print('raggiunto massimo numero di iterazioni \n')
        
    return x1,it,xk