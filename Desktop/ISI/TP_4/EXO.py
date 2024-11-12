import numpy as np
def afficher(p):
 n=len(p)
 for i in range (n-1,-1,-1):
        if(i==0):
            print(f"{p[i]}")
        else:
            print(f" {p[i]}*X^{i} + ",end=" ")
t=[2,4,6,2]
n=afficher(t)

def get_valeur(p,x):
    n=len(p)
    val=0
    for i in range (n-1,-1,-1):
     val+=p[i]*(x**i)
    return val
print(get_valeur(t,1))
def deriver(p):
    n=len(p)
    d=np.zeros(len(p))
    for i in range (n-1,-1,-1):
        d[i]=p[i]*i

    return d


b=deriver(t)
print(b)
afficher(b)