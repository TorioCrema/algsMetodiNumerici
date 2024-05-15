import numpy as np

def newton(fname,fpname,x0,tolx,tolf,nmax):
    """
    Implementa il metodo di Newton per il calcolo degli zeri di un'equazione non lineare.

    Parametri:
    fname: La funzione di cui si vuole calcolare lo zero.
    fpname: La derivata prima della funzione di  cui si vuole calcolare lo zero.
    x0: iterato iniziale
    tolx: La tolleranza di errore tra due iterati successivi
    tolf: tolleranza sul valore della funzione
    nmax: numero massimo di iterazione

    Restituisce:
    Lo zero approssimato della funzione, il numero di iterazioni e la lista degli iterati intermedi.
    """ 
    xk=[]
    fx0=fname(x0)
    if abs(fpname(x0)) <= np.spacing(1): #to do
        print(" derivata prima nulla in x0")
        return None, None,None
    
    d = fx0 / fpname(x0)
    x1 = x0 - d
    
    fx1=fname(x1)
    xk.append(x1)
    it=1
    
    while it < nmax:
        x0 = x1
        fx0 = fname(x0)
        #Se la derivata prima e' pià piccola della precisione di macchina stop
        if abs(fpname(x0)) <= np.spacing(1):
            print(" derivata prima nulla in x0")
            return None, None,None
        d = fx0 / fpname(x0)
        
        x1 = x0 - d
        fx1=fname(x1)
        it=it+1
        
        xk.append(x1)
        
    if it==nmax:
        print('raggiunto massimo numero di iterazioni \n')
        
    return x1,it,xk