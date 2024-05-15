import numpy as np

def plagr(xnodi,j):
    """
    Restituisce i coefficienti del j-esimo pol di
    Lagrange associato ai punti del vettore xnodi
    """
    xzeri=np.zeros_like(xnodi)
    n=xnodi.size
    if j==0:
       xzeri=xnodi[1:n]
    else:
       xzeri=np.append(xnodi[:j], xnodi[j+1:])
    
    num = np.linalg.poly(xzeri)
    den = np.polyval(num, xnodi[j])
    
    p=num/den
    
    return p

def InterpL(x, y, xx):
    """"
    %funzione che determina in un insieme di punti il valore del polinomio
    %interpolante ottenuto dalla formula di Lagrange.
    % DATI INPUT
    %  x  vettore con i nodi dell'interpolazione
    %  f  vettore con i valori dei nodi 
    %  xx vettore con i punti in cui si vuole calcolare il polinomio
    % DATI OUTPUT
    %  y vettore contenente i valori assunti dal polinomio interpolante
    %
    """
    n=x.size
    m=xx.size
    L=np.zeros((m,n))
    for j in range(n):
        p = plagr(x, j)
        L[:,j] = np.polyval(p, xx)

    return L@y