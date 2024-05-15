import numpy as np

def my_newtonSys_sham(fun, jac, x0, tolx, tolf, nmax):
    """
    Funzione per la risoluzione del sistema f(x)=0
    mediante il metodo di Newton, con variante delle shamanski, in cui lo Jacobiano viene
    aggiornato ogni un tot di iterazioni, deciso dall'utente.

    Parametri
    ----------
    fun : funzione vettoriale contenente ciascuna equazione non lineare del sistema.
    jac : funzione che calcola la matrice Jacobiana della funzione vettoriale.
    x0 : array
        Vettore contenente l'approssimazione iniziale della soluzione.
    tolx : float
        Parametro di tolleranza per l'errore tra due soluzioni successive.
    tolf : float
        Parametro di tolleranza sul valore della funzione.
    nmax : int
        Numero massimo di iterazioni.

    Restituisce
    -------
    x : array
        Vettore soluzione del sistema (o equazione) non lineare.
    it : int
        Numero di iterazioni fatte per ottenere l'approssimazione desiderata.
    Xm : array
        Vettore contenente la norma dell'errore relativo tra due iterati successivi.
    """

    matjac = jac(x0)
    if np.linalg.det(matjac) == 0:
        print("La matrice dello Jacobiano calcolata nell'iterato precedente non è a rango massimo")
        return None,None,None

    s = -np.linalg.solve(matjac, fun(x0))
    # Aggiornamento della soluzione
    it = 1
    x1 = x0 + s
    fx1 = fun(x1)

    Xm = [np.linalg.norm(s, 1)/np.linalg.norm(x1,1)]
    update=10  #Numero di iterazioni durante le quali non si aggiorna la valutazione dello Jacobiano nell'iterato attuale
    while it <= nmax and np.linalg.norm(fx1, 1) >= tolf and np.linalg.norm(s, 1) >= tolx * np.linalg.norm(x1, 1):
        x0 = x1
        it += 1
        if it % update==0:   #Valuto la matrice di iterazione nel nuovo iterato ogni "update" iterazioni
            matjac = jac(x0)
    
            if np.linalg.det(matjac) == 0:
                print("La matrice dello Jacobiano calcolata nell'iterato precedente non è a rango massimo")
                return None,None,None
            else:
                s = -np.linalg.solve(matjac, fun(x0))
        else:
            s = -np.linalg.solve(matjac, fun(x0))

        # Aggiornamento della soluzione
        x1 = x0 + s
        fx1 = fun(x1)
        Xm.append(np.linalg.norm(s, 1)/np.linalg.norm(x1,1))

    return x1, it, Xm