#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:26:45 2020

@author: sk
"""

from numpy.random import choice, random, normal, uniform, gamma, beta, exponential
import matplotlib.pyplot as plt, math

import numpy as np

def limpia(x):
    #res = [0]
    res=[]
    for i in range(len(x)):
        if (x[i]!=0):
            res.append(x[i])
    return res


Hfun = []
Hfull = []

for vueltas in range(1,1000):

    
    Fin = 100000
    N = 1000
    
    funcionandoCI = 10
    reservaCI = 4
    operarios = 4
    
    maquinasFuncionando = funcionandoCI
    maquinasReserva = reservaCI
    maquinasRotas = 0
    
    
    T = N
    n=0
    t=0
    trompe = N
    tarregla = N
    Nrotas = 0
    Narregladas = 0
    rotas = [0 for i in range(Fin)]
    arregladas = [0 for i in range(Fin)]
    arreglo = [0 for i in range(Fin)]
    
    def rompe(n):
        if n==0: n=1
        return normal(1.8,0.2)/n
    def arregla(n,t,T):
        tasa = 0.55 + (1.65-0.55)*t/T
        if n==0: n=1
        if n>operarios: n=operarios
        return exponential(tasa)/n
        
      
    funcionando = 0
    
    def romper(tsuc):
        
        global maquinasRotas
        global maquinasReserva
        global maquinasFuncionando
        
        if (maquinasFuncionando>0):
            if (maquinasRotas<funcionandoCI+reservaCI-1):
                maquinasRotas+=1
            if (maquinasReserva>0):
                maquinasReserva-=1
            else:
                if (maquinasFuncionando>0): maquinasFuncionando-=1
            
            global T
            global t
            t = tsuc
            global n
            n+=1
            global Nrotas
            Nrotas+=1
            rotas[Nrotas]=t
            X = rompe(maquinasFuncionando)
            if (t+X<T):
                global trompe
                trompe = t + X
            if (maquinasRotas>0 and maquinasRotas<reservaCI):
                
                Y = arregla(maquinasRotas,t,T)
                global tarregla
                tarregla = t + Y
                global Serv
                if(n==1): arreglo.append(Y)
    
    
    def arreglar(tsuc):
        global maquinasRotas
        global maquinasReserva
        global maquinasFuncionando
        
        if (maquinasRotas>0):
            global T
            
            if (maquinasRotas>0):
                if (maquinasFuncionando>funcionandoCI-1):
                    maquinasReserva+=1
                else:
                    maquinasFuncionando+=1
                maquinasRotas-=1
                
            global t
            t = tsuc
            global n
            n-=1
            global Narregladas
            Narregladas += 1
            global S
            arregladas[Narregladas]=t
            if (maquinasRotas>0):
                
                Y = arregla(maquinasRotas,t,T)
                global tarregla
                tarregla = t + Y
                arreglo.append(Y)
            
            
    
    
    romper(rompe(maquinasFuncionando))
    veces=0
    fun = 0 
    ful = 0
    Maquinas=[]
    while(trompe<Fin or tarregla<Fin):
        Maquinas.append(maquinasFuncionando)
        if (maquinasFuncionando>funcionandoCI-1): fun+=1
        if (maquinasRotas>operarios-1): ful+=1
        veces+=1
        if (trompe<tarregla):
            #print("ROMPO. funcionando: ", maquinasFuncionando, ". rotas: ",maquinasRotas, ". reserva: ",maquinasReserva)
            tsuc = trompe
            trompe = Fin
            romper(tsuc)
        
        if (tarregla<trompe):
            #print("ARRRRREGLO. funcionando: ", maquinasFuncionando, ". rotas: ",maquinasRotas, ". reserva: ",maquinasReserva)
            tsuc=tarregla
            tarregla= Fin
            arreglar(tsuc)
            
    rotas=limpia(rotas)
    arregladas=limpia(arregladas)
    arreglo=limpia(arreglo) 
    
    
    
    #print()
    #print("proporcion tiempo sistema funcionando: ",fun/veces)
    #print()
    #print("proporcion los ", operarios, " trabajando a la vez: ",ful/veces)
    
    #tiempo.append([reservaCI,fun/veces])
    #ocupados.append([reservaCI,ful/veces])
    
    a1 = 0
    a2 = 0
    mini=[]
    mini.append(len(rotas))
    mini.append(len(arregladas))
    mini.append(len(arreglo))
    for i in range(min(mini)):
        a1 += arregladas[i]-rotas[i]
        a2 += arregladas[i]-rotas[i]-arreglo[i]    
            
    #A1.append([operarios,a1/len(rotas)])
    #A2.append([operarios,a2/len(rotas)])
    Hfun.append(fun/veces)
    Hfull.append(ful/veces)
        
    
def pinta(puntos):
    plt.plot( [ puntos[i][0] for i in range(len(puntos)) ],[puntos[i][1] for i in range(len(puntos))])

print("PARA TIEMPO DEL SISTEMA FUNCIONANDO")
print("media: ",np.mean(Hfun))
print("desviacion: ",np.std(Hfun))
print("PARA TIEMPO DE OPRERARIOS TRABAJANDO A LA VEZ")
print("media: ",np.mean(Hfull))
print("desviacion: ",np.std(Hfull))


plt.hist(Hfun, bins=30)
plt.xlabel('media: '+str("%.4f" % np.mean(Hfun))+'  desviacion: '+str("%.4f" % np.std(Hfun)))
#plt.xlabel('media: ',np.mean(Hfun),' desviacion: ',np.std(Hfun))

plt.hist(Hfull, bins=30)
plt.xlabel('media: '+str("%.4f" % np.mean(Hfull))+'  desviacion: '+str("%.4f" % np.std(Hfull)))

#plt.hist(Hfull, bins=10)

"""
puntos=A1
plt.xlabel('OPERARIOS')
plt.ylabel('PROPORCION')
plt.plot( [ puntos[i][0] for i in range(len(puntos)) ],[puntos[i][1] for i in range(len(puntos))],label="tiempo medio sistema")
puntos=A2
plt.plot( [ puntos[i][0] for i in range(len(puntos)) ],[puntos[i][1] for i in range(len(puntos))],label="tiempo medio cola")

plt.legend()
"""