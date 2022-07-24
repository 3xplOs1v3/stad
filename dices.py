#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:51:04 2020

@author: sk
"""
from numpy.random import choice, random, normal, uniform, gamma, beta, exponential
import matplotlib.pyplot as plt, math

from matplotlib.pyplot import hist


# x1 + x2 + ... +xn = k
def CR(n,k):
    if n==1:
        return 1
    aux = [i for i in range(k+1)]
    return sum([CR(n-1,k-i) for i in aux])

# [[0,0,1],[0,1,0],[0,1,1]...[1,1,1]] P(mdimension, nelemento) n^m [(1/n),...,(m/n)]
def P(m,n):
    if m == 1:
        return [[i] for i in range(n)]
    return [ [i]+k for i in range(n) for k in P(m-1,n) ]

#DISCRETOS
def mapaa(x):
    res = []
    for xi in x:
        i = buscai(xi,res)
        if i==-1:
            res.append([xi,1])
        else:
            res[i][1]+=1
    return res
            
        
def buscai(xo, x):
    for i in range(len(x)):
        #if xo==x[i][0]:
        if xo==x[i][0]:
            return i
    return -1


n=100000

#x=[f(random()) for i in range(n)]




#suma de dados (uniformes discretas)
#dices = sorted([sum([choice([1,2,3,4,5,6]) for i in range(dados)]) for j in range(n)])

#uniforme
#dices = sorted([ random() for j in range(n)])

#suma uniformes continuas
dados=2
#dices = sorted([sum([random() for i in range(dados)]) for j in range(n)])

#resta de dos uniformes
#dices = sorted([ random()-random() for j in range(n)])

#producto de dos uniformes
#dices = sorted([ random()*random() for j in range(n)])

#division de dos uniformes
#dices = sorted([ random()/random() for j in range(n)])

#dices = sorted([ random()**(1/2) for j in range(n)])





#mapa = mapaa(dices)
#prob = [ [mapa[i][0] ,mapa[i][1]/len(dices) ] for i in range(len(mapa))]
#plt.plot([prob[i][0] for i in range(len(prob))], [prob[i][1] for i in range(len(prob))])

def max(x):
    max=x[0];
    for xi in x:
        if xi>max:
            max=xi
    return max

def min(x):
    min=x[0];
    for xi in x:
        if xi<min:
            min=xi
    return min

def fdistribucion(x):
    x=sorted(x)
    res=[]
    precision=100
    contador=0
    step=(max(x)-min(x))/precision
    level=step+min(x)
    for xi in x:
        if xi<=level:
            contador+=1
        else:
            res.append([level,contador])
            level+=step
            contador=0
    def normaliza(x):
        n=cuantos(x)
        for i in range(len(x)):
            x[i][1]=x[i][1]/n/step
        return x
    return normaliza(res)
  
    

    
def pinta(puntos):
    plt.plot( [ puntos[i][0] for i in range(len(puntos)) ],[puntos[i][1] for i in range(len(puntos))])
  
       
def cuantos(x):
    res=0
    for i in range(len(x)):
        res+=x[i][1]
    return res

n=100000
#dices=[erlang(2,1) for i in range(n)]
#dices=[uniform(0,1)+uniform(0,1) for i in range(n)]
#pinta(fdistribucion(dices))

def f1(x):
    return -1.4*x+1.7

def F1(x):
    return -0.7*x**2+1.7*x

def inverso():
    res=[]
    for i in range(n):
        u=uniform(0,1)
        if (0.7**2 -4*0.7*u)>=0:
            res.append((1.7+math.sqrt(0.7**2 -4*0.7*u))/(2*0.7))
    return res
    
#1.1
def unoa():
    X=[]
    for i in range(n):
        u = uniform(0,1)
        x=0
        while F1(x)<=u:
            x+=0.01
        X.append(x)
    return X

#1.2
def unob():
    X=[]
    for i in range(n):
        u1=uniform(0,1)
        u2=uniform(0,1)
        if u2<f1(u1)/1.7:
            X.append(u1)
    return X
"""
real=[f1(random()) for i in range(n)]
#pinta(fdistribucion(real))
pinta(fdistribucion(unoa()))
pinta(fdistribucion(unob()))
"""
"""
puntos=fdistribucion(unoa())
plt.plot( [ puntos[i][0] for i in range(len(puntos)) ],[puntos[i][1] for i in range(len(puntos))],label="inversion")
puntos=fdistribucion(unob())
plt.plot( [ puntos[i][0] for i in range(len(puntos)) ],[puntos[i][1] for i in range(len(puntos))],label="rechazo")
plt.legend()
"""

#2
def f2(x):
    return 20*x*(1-x)**3

def dos():
    X=[]
    for i in range(n):
        u1=uniform(0,1)
        u2=uniform(0,1)
        if u2<f2(u1)/f2(1/4):
            X.append(u1)
    return X
"""
real=[beta(2,4) for i in range(n)]
pinta(fdistribucion(real))
pinta(fdistribucion(dos()))
"""
"""
puntos=fdistribucion([beta(2,4) for i in range(n)])
plt.plot( [ puntos[i][0] for i in range(len(puntos)) ],[puntos[i][1] for i in range(len(puntos))],label="Beta(2,4)")
puntos=fdistribucion(dos())
plt.plot( [ puntos[i][0] for i in range(len(puntos)) ],[puntos[i][1] for i in range(len(puntos))],label="rechazo")
plt.legend()
"""
#3
n=10000
def tres():
    opcion1=[]
    opcion2=[]
    opcion3=[]
    for i in range(n):
        u1=uniform(0,1)
        v1=2*uniform(0,1)/math.exp(1)
        if v1<=-2*u1*math.log(u1):
            opcion1.append(v1/u1)
        u2=uniform(0,1)
        v2=uniform(0,1)/2
        if v2<=2*u2*(1-u2):
            opcion2.append(v2/u2)
        u3=uniform(0,((1+math.sqrt(2*math.exp(1)))/math.exp(1)))
        v3=2*uniform(0,1)/math.exp(1)
        if v3<2/math.exp(1) -(u3-1/math.exp(1))**2:
            if (v3/u3<10): #para que no dispare puntos
                opcion3.append(v3/u3)
    return [opcion1,opcion2,opcion3]

def ordenamayor(p):
    res = []
    for i in range(1,len(p)+1):
        mini = max(p)
        res.append(mini)
        p.remove(mini)
    return res

def normalizaa(x):
    #x=sorted(x)
    x=ordenamayor(x)
    res=[]
    maximo=max(x)
    for i in range(len(x)):
        res.append([i/(len(x)-1),x[i]/maximo])
    return sorted(res)

"""
opcion=tres()
opcion1=normalizaa(opcion[0])
opcion2=normalizaa(opcion[1])
opcion3=normalizaa(opcion[2])
plt.plot([opcion1[i][0] for i in range(len(opcion1))],[opcion1[i][1] for i in range(len(opcion1))],label='opcion1')
plt.plot([opcion2[i][0] for i in range(len(opcion2))],[opcion2[i][1] for i in range(len(opcion2))],label='opcion2')
plt.plot([opcion3[i][0] for i in range(len(opcion3))],[opcion3[i][1] for i in range(len(opcion3))],label='opcion3')


real=normalizaa([exponential(1) for i in range(n)])
plt.plot([real[i][0] for i in range(len(real))],[real[i][1] for i in range(len(real))],label='real')
plt.legend() 

"""
"""


dices = sorted([ beta(10,40) for j in range(n)])

pinta(fdistribucion(dices))

"""

X=tres()



puntos=fdistribucion([exponential(1) for i in range(n)])
plt.plot( [ puntos[i][0] for i in range(len(puntos)) ],[puntos[i][1] for i in range(len(puntos))],label="real")
puntos=fdistribucion(X[0])
#plt.plot( [ puntos[i][0] for i in range(len(puntos)) ],[puntos[i][1] for i in range(len(puntos))],label="opcion1")
puntos=fdistribucion(X[1])
#plt.plot( [ puntos[i][0] for i in range(len(puntos)) ],[puntos[i][1] for i in range(len(puntos))],label="opcion2")
puntos=fdistribucion(X[2])
#plt.plot( [ puntos[i][0] for i in range(len(puntos)) ],[puntos[i][1] for i in range(len(puntos))],label="opcion3")

plt.legend()
