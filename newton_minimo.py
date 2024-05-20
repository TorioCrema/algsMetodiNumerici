import numpy as np

def my_newton_minimo_MOD(gradiente, Hess, x0, tolx, tolf, nmax):
    """
    Funzione di newton-raphson per calcolare il minimo di una funzione in più variabili, modificato nel caso in cui si utilizzando sympy 
    per calcolare Gradiente ed Hessiano. Rispetto alla precedente versione cambia esclusivamente il modo di valutare il vettore gradiente e la matrice Hessiana in un punto 
    Parametri
    ----------
    fun : 
        Nome della funzione che calcola il gradiente della funzione non lineare.
    Hess :  
        Nome della funzione che calcola la matrice Hessiana della funzione non lineare.
    x0 : array
        Vettore contenente l'approssimazione iniziale della soluzione.
    tolx : float
        Parametro di tolleranza per l'errore assoluto.
    tolf : float
        Parametro di tolleranza per l'errore relativo.
    nmax : int
        Numero massimo di iterazioni.

    Restituisce
    -------
    x : array
        Vettore soluzione del sistema (o equazione) non lineare.
    it : int
        Numero di iterazioni fatte per ottenere l'approssimazione desiderata.
    Xm : array
        Vettore contenente la norma del passo ad ogni iterazione.
    """
        
    matHess = np.array([[Hess[0, 0](x0[0], x0[1]), Hess[0, 1](x0[0], x0[1])],
                        [Hess[1, 0](x0[0], x0[1]), Hess[1, 1](x0[0], x0[1])]])
    

    gradiente_x0 = np.array([gradiente[0](x0[0], x0[1]),gradiente[1](x0[0], x0[1])])
    
    if np.linalg.det(matHess) == 0:
        print("La matrice Hessiana calcolata nell'iterato precedente non è a rango massimo")
        return None, None, None
        
    s = -np.linalg.solve(matHess, gradiente_x0)
    
    # Aggiornamento della soluzione
    it = 1
    x1 = x0 + s
    grad_fx1 = np.array([gradiente[0](x1[0],x1[1]), gradiente[1](x1[0],x1[1])])
    Xm = [np.linalg.norm(s, 1)]
    
    while it <= nmax and np.linalg.norm(grad_fx1, 1) >= tolf and np.linalg.norm(s, 1) >= tolx * np.linalg.norm(x1, 1):
        
        x0 = x1
        it += 1
        matHess = np.array([[Hess[0, 0](x0[0], x0[1]), Hess[0, 1](x0[0], x0[1])],
                            [Hess[1, 0](x0[0], x0[1]), Hess[1, 1](x0[0], x0[1])]])

        grad_fx0 = grad_fx1
        
        if np.linalg.det(matHess) == 0:
            print("La matrice Hessiana calcolata nell'iterato precedente non è a rango massimo")
            return None, None, None

        s = -np.linalg.solve(matHess, grad_fx1)
        
        # Aggiornamento della soluzione
        x1 = x0 + s
        #Aggiorno il gradiente per la prossima iterazione 
        grad_fx1 = np.array([gradiente[0](x1[0],x1[1]), gradiente[1](x1[0],x1[1])])
        print(np.linalg.norm(s, 1))
        Xm.append(np.linalg.norm(s, 1))

    return x1, it, Xm


def my_newton_minimo(gradiente, Hess, x0, tolx, tolf, nmax):
    """
    DA UTILIZZARE NEL CASO IN CUI CALCOLATE DRIVATE PARZIALI PER GRADIENTE ED HESSIANO SENZA UTILIZZO DI SYMPY
    
    Funzione di newton-raphson per calcolare il minimo di una funzione in più variabili

    Parametri
    ----------
    fun : 
        Nome della funzione che calcola il gradiente della funzione non lineare.
    Hess :  
        Nome della funzione che calcola la matrice Hessiana della funzione non lineare.
    x0 : array
        Vettore contenente l'approssimazione iniziale della soluzione.
    tolx : float
        Parametro di tolleranza per l'errore assoluto.
    tolf : float
        Parametro di tolleranza per l'errore relativo.
    nmax : int
        Numero massimo di iterazioni.

    Restituisce
    -------
    x : array
        Vettore soluzione del sistema (o equazione) non lineare.
    it : int
        Numero di iterazioni fatte per ottenere l'approssimazione desiderata.
    Xm : array
        Vettore contenente la norma del passo ad ogni iterazione.
    """

    matHess = Hess(x0)
    if np.linalg.det(matHess) == 0:
        print("La matrice Hessiana calcolata nell'iterato precedente non è a rango massimo")
        return None, None, None
    grad_fx0 = gradiente(x0)    
    s = -np.linalg.solve(matHess, gradiente(x0))
    # Aggiornamento della soluzione
    it = 1
    x1 = x0 + s
    grad_fx1 = gradiente(x1)
    Xm = [np.linalg.norm(s, 1)]
    
    while it <= nmax and np.linalg.norm(grad_fx1 , 1) >= tolf and np.linalg.norm(s, 1) >= tolx * np.linalg.norm(x1, 1):
        
        x0 = x1
        it += 1
        matHess = Hess(x0)
        grad_fx0 = grad_fx1
        
        if np.linalg.det(matHess) == 0:
            print("La matrice Hessiana calcolata nell'iterato precedente non è a rango massimo")
            return None, None, None
        

        # Risolvo il sistema lineare avente come matrice dei coefficienti la
        # matrice Hessiana e come termine il vettore gradiente calcolato nell'iterato precedente
        # in x0
        s = -np.linalg.solve(matHess, grad_fx0)
        
        # Aggiornamento della soluzione
        x1 = x0 + s

        #Calcolo del gradiente nel nuovo iterato
        grad_fx1  = gradiente(x1)
        print(np.linalg.norm(s, 1))
        Xm.append(np.linalg.norm(s, 1))

    return x1, it, Xm