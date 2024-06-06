# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:50:05 2020

@author: Sofi
"""
import numpy as np
import copy
import random

# Pregunta 1 + Preliminares
Cal=np.array([[(4,3),(5,4),(2,5),(4,0),(4,2), (3,4),(4,5),(5,2),(0,4),(2,4), (4,3),(5,4),(2,5),(4,0),(4,2)],
              [(5,0),(3,1),(1,4),(1,5),(5,3), (0,5),(1,3),(4,1),(5,1),(3,5), (5,0),(3,1),(1,4),(1,5),(5,3)],
              [(1,2),(0,2),(3,0),(3,2),(0,1), (2,1),(2,0),(0,3),(2,3),(1,0), (1,2),(0,2),(3,0),(3,2),(0,1)]],int)
Cal9=np.array([[  0,  5,  2, -3, -4, -1,  0,-10, -7,  8,  9,  6,  0, 15, 12,-13,-14,-11],
               [ -5,  0,  1, -2,  3,  4, 10,  0, -6,  7, -8, -9,-15,  0, 11,-12, 13, 14],
               [ -2, -1,  0, -4, -5,  3,  7,  6,  0,  9, 10, -8,-12,-11,  0,-14,-15, 13],
               [  3,  2,  4,  0, -1, -5, -8, -7, -9,  0,  6, 10, 13, 12, 14,  0,-11,-15],
               [  4, -3,  5,  1,  0, -2, -9,  8,-10, -6,  0,  7, 14,-13, 15, 11,  0,-12],
               [  1, -4, -3,  5,  2,  0, -6,  9,  8,-10, -7,  0, 11,-14,-13, 15, 12,  0]],int)
DistProv=np.array([[  0, 328, 658, 222, 860, 797],
            [328,   0, 330, 125, 533, 469],
            [658, 330,   0, 465, 256, 212],
            [222, 125, 465,   0, 657, 594],
            [860, 533, 256, 657,   0,  98],
            [797, 469, 212, 594,  98,   0]],int)
Subseries=np.array([(0,1),(0,2),(3,0),(4,0),(5,0),(1,2),(3,1),(1,4),(1,5),(3,2),(4,2),(2,5),(4,3),(5,4),(5,3)],int)


# =============================================================================
# Pregunta 2

# Función que convierte un calendario de la forma 5 a la forma 9, dados el calendario, la cantidad de equipos y las rondas
def C5aC9(c,cant,R):
    C9=np.zeros((cant,R*cant),int)
    C=np.zeros((cant//2,R*(cant-1),2),int)
    CC=np.zeros((cant//2,R*(cant-1),2),int)
    for i in range(0,cant//2):
        for j in range(0,R*(cant-1)):
            C[i][j][1]=c[i][j][1]+(j//(cant-1))*cant
            C[i][j][0]=c[i][j][0]
            CC[i][j][0]=c[i][j][0]+(j//(cant-1))*cant
            CC[i][j][1]=c[i][j][1]
    for i in range(0,cant//2):
        for j in range(0,R*(cant-1)):
            C9[C[i][j][0],C[i][j][1]]=j+1
            C9[CC[i][j][1],CC[i][j][0]]=-(j+1)
    return C9

# Función que convierte un calendario de la forma 9 a la forma 5, dados el calendario, la cantidad de equipos y las rondas
def C9aC5(c,cant,R):
    C5=np.zeros((cant//2,R*(cant-1),2),int)
    for i in range(0,cant):
        for j in range(0,R*cant):
            if c[i][j]>0:
                n=0
                while C5[n][c[i][j]-1][0]+C5[n][c[i][j]-1][1]>0:
                    if n==cant//2-1:
                        break
                    else:
                        n+=1
                C5[n][c[i][j]-1][0]=i
                C5[n][c[i][j]-1][1]=j%cant
    return C5


# =============================================================================
# Pregunta 3
    
# Función que, dados un calendario de la forma 9, una cantidad de equipos, un número de rondas y una matriz de distancias, 
# devuelve la lista de distancias que recorre cada equipo y la distancia total recorrida 
def distC9(c,cant,R,distancias):
    Dist9=[0]*cant
    for equipo in range(0,cant):
        l=[equipo]*(R*(cant-1)+1)
        for i in range(-1,-(R*(cant-1)+1),-1):
            for j in range(((abs(i+1))//(cant-1))*cant,((abs(i+1))//(cant-1))*cant+cant):
                if i==c[equipo][j]:
                    l[abs(i)]=int(j%cant)
                    break
        for j in range(0,R*(cant-1)):
            Dist9[equipo]+=distancias[l[j],l[j+1]]
    return [Dist9,(np.array(Dist9)).sum()]

# Función análoga para un calendario de la forma 5
def distC5(c,cant,R,distancias):
    return distC9(C5aC9(c,cant,R),cant,R,distancias)


# =============================================================================
# Pregunta 4
    
# Restricción 0
# Función que verifica que un equipo no juegue el mismo día con dos equipos distintos, dados un calendario de la forma 9, 
# la cantidad de equipos y la cantidad de rondas
def verifbasicC9(c,cant,R):
    for equipo in range(0,cant):
        C=c[equipo:equipo+1,:]
        for dia in range(1,R*(cant-1)+1):
            if len(C[abs(C)==dia])+len(C[abs(C)==-dia])!=1:
                return [False,equipo,dia]
    return True

# Función análoga para un calendario de la forma 5
def verifbasicC5(c,cant,R):
    return verifbasicC9(C5aC9(c,cant,R),cant,R)
    
# -----------------------------------------------------------------------------
# Restricción 1
# Función que verifica que se cumpla la restricción TTP-k del torneo RR-r, dados un calendario de la forma 5, la cantidad
# de equipos, la cantidad de rondas y el parámetro k
def verif1C5(c,cant,R,k):
    for equipo in range(0,cant):
        dia=0
        while dia<R*(cant-1)-k:
            lugar=1
            for s in range(0,cant//2):
                if c[s][dia][0]==equipo:
                    lugar=0
                    break
            for n in range(1,k+2):
                t=0
                if n==k+1:
                    return False
                else:
                    for s in range(0,cant//2):
                        if c[s][dia+n][lugar]!=equipo:
                            t+=1
                    if t==cant//2:
                        dia+=n
                        break               
    return True

# Función análoga para un calendario de la forma 9
def verif1C9(c,cant,R,k):
    return verif1C5(C9aC5(c,cant,R),cant,R,k)

# -----------------------------------------------------------------------------
# Restricción 2 (Solo se verificarán para 3 rondas)
# 2.1
# Función que verifica que cada par de equipos juegue exactamente una vez en cada ronda y que se alternen en cuanto a 
# L y V, dados un calendario de la forma 9 y la cantidad de equipos
def verif21C9(c,cant):
    for equipo1 in range(0,cant):
        for equipo2 in range (equipo1+1,cant):
            if c[equipo1][equipo2]*c[equipo1][equipo2+cant]>=0:
                return [False,equipo1,equipo2] 
            if c[equipo1][equipo2+cant]*c[equipo1][equipo2+2*cant]>=0:
                return [False,equipo1,equipo2+2*cant]
    return True            

# Función análoga para un calendario de la forma 5
def verif21C5(c,cant):
    return verif21C9(C5aC9(c,cant,3),cant)


# 2.2
# Función que verifica que no haya subseries de ida y vuelta, dados un calendario de la forma 9 y la cantidad de equipos
def verif22C9(c,cant):
    for equipo1 in range(0,cant):
        for equipo2 in range (equipo1+1,cant):
            if abs(c[equipo1][equipo2+cant])-abs(c[equipo1][equipo2])==1:
                return False           
            if abs(c[equipo1][equipo2+2*cant])-abs(c[equipo1][equipo2+cant])==1:
                return False
    return True

# Función análoga para un calendario de la forma 5
def verif22C5(c,cant):  
    return verif22C9(C5aC9(c,cant,3),cant)

# -----------------------------------------------------------------------------
# Funciones que verifican que se cumplan todas las restricciones anteriores para un TTP-k, RR-3
# Función para calendarios de la forma 5
def verifC5(c,cant,k):
    return verif1C5(c,cant,3,k) and verif21C5(c,cant) and verif22C5(c,cant) and verifbasicC5(c,cant,3)

# Función para calendarios de la forma 9
def verifC9(c,cant,k):
    return verif1C9(c,cant,3,k) and verif21C9(c,cant) and verif22C9(c,cant) and verifbasicC9(c,cant,3)


# =============================================================================
# Problema 5:
 

# =============================================================================
# Problema 6:

# Funciones auxiliares 
# Función que dada una lista de subseries, transforma la lista dada en una matriz de la forma 9 que no ofrece información
# sobre los días en que se realiza cada subserie, sino solo la información de L/V a partir de los elementos 0,1,-1
def Mascara(S):
    Calen=np.zeros((6,6),int)
    for i in range(6):
        for j in range(i):
            a=(S[:,0:1]==i)
            b=(S[:,1:]==j)
            c=(a*b==1)
            if c.any():
                Calen[i][j]=1
                Calen[j][i]=-1
            else:
                Calen[i][j]=-1
                Calen[j][i]=1
    return Calen

# Función que dada una lista, devuelve la lista de todas las listas que son desordenaciones de la dada
def ListasPosibles(l):
    ListPos=[]
    if len(l)==1:
        ListPos.append(l)
    else:
        for i in range(len(l)):
            lcopy=copy.deepcopy(l)
            del lcopy[i]
            L=ListasPosibles(lcopy)
            for j in range(len(L)):
                L[j].append(l[i])
            ListPos+=L
    return ListPos

# Función que dados un número y una lista ordenada de números, devuelve la posición que debería ocupar el número si se 
# insertara en la lista, utilizando el método de búsqueda binaria
def Ubicar(x,lista,ini,fin):
    if len(lista[ini:fin])==1:
        if x>=lista[ini]:
            return fin
        else:
            return ini
    else:
        if x>=lista[(ini+fin)//2]:
            return Ubicar(x,lista,(ini+fin)//2,fin)
        else:
            return Ubicar(x,lista,ini,(ini+fin)//2)


# -----------------------------------------------------------------------------
# Función que devuelve un calendario que cumple con las restricciones y además cumple que las rondas 1,2,3 solo varían en
# cuanto a la alternancia L/V
def Calendario(S):
    k=0
    Calen=Mascara(S)
    L0=ListasPosibles(list(range(1,6)))
    L1=[[]]
    for i in range(1,6):
        listica=list(range(1,6))
        listica.remove(i)
        L1.append(ListasPosibles(listica))
    for i in range(len(L0)):
        Lista0=np.array(L0[i],int)   
        for j in range(len(L1[Lista0[0]])):
            C=np.zeros((6,6),int)
            C[0:1,1:]=Lista0
            Lista1=np.array(L1[Lista0[0]][j])
            Bool=Lista1-Lista0[1:]
            if len(Bool[Bool==0])==0:
                C[1:2,2:]=Lista1
                for dia in range(1,6):
                    listica2=[2,3,4,5]
                    if dia!=Lista0[0]:
                        listica2.remove(L0[i].index(dia)+1)
                        listica2.remove(L1[Lista0[0]][j].index(dia)+2)
                        if C[listica2[0]][listica2[1]]!=0:
                            C[0][1]=0
                            break
                        else:
                            C[listica2[0]][listica2[1]]=dia
                if C[0][1]!=0:
                    C+=C.T
                    C=np.where(C==0,Lista0[0],C)
                    D=np.concatenate((C*Calen,(C+5)*Calen*(-1),(C+10)*Calen),axis=1)
                    if verif1C9(D,6,3,3):
                        return D
    return False

# =============================================================================
# Adicional - Optimización del calendario
    
# Función que recorre todos los posibles calendarios y devuelve el calendario en que la distancia total recorrida sea mínima
# Es demasiado costosa
def Optimo(S):
    Calen=Mascara(S)
    L0=ListasPosibles(list(range(1,6)))
    L1=[[]]
    ListCal=[]
    CalOp=copy.deepcopy(Calendario(S))
    Optimus=distC9(CalOp,6,3,DistProv)[1]
    for i in range(1,6):
        listica=list(range(1,6))
        listica.remove(i)
        L1.append(ListasPosibles(listica))
    for i in range(len(L0)):
        Lista0=np.array(L0[i],int)   
        for j in range(len(L1[Lista0[0]])):
            C=np.zeros((6,6),int)
            C[0:1,1:]=Lista0
            Lista1=np.array(L1[Lista0[0]][j])
            Bool=Lista1-Lista0[1:]
            if len(Bool[Bool==0])==0:
                C[1:2,2:]=Lista1
                for dia in range(1,6):
                    listica2=[2,3,4,5]
                    if dia!=Lista0[0]:
                        listica2.remove(L0[i].index(dia)+1)
                        listica2.remove(L1[Lista0[0]][j].index(dia)+2)
                        if C[listica2[0]][listica2[1]]!=0:
                            C[0][1]=0
                            break
                        else:
                            C[listica2[0]][listica2[1]]=dia
                if C[0][1]!=0:
                    C+=C.T
                    C=np.where(C==0,Lista0[0],C)
                    ListCal.append(C)
    for i in range(len(ListCal)):
        for j in range(len(ListCal)):
            for k in range(len(ListCal)): 
                D=np.concatenate((ListCal[i]*Calen,(ListCal[i]+5)*(-1)*Calen,(ListCal[i]+10)*Calen),axis=1)
                if verif1C9(D,6,3,3) and verif22C9(D,6) and distC9(D,6,3,DistProv)[1]<Optimus:
                    CalOp=D
                    Optimus=distC9(D,6,3,DistProv)[1]
    return Optimus,CalOp

# -----------------------------------------------------------------------------
# Función que recorre todos los posibles calendarios que cumplen que las rondas 1,2 y 3 solo difieren en la alternancia
# L/V y devuelve el que minimiza la distancia total recorrida - es instantánea
def OptimoYparejo(S):
    Calen=Mascara(S)
    L0=ListasPosibles(list(range(1,6)))
    L1=[[]]
    CalOp=copy.deepcopy(Calendario(S))
    Optimus=distC9(CalOp,6,3,DistProv)[1]
    for i in range(1,6):
        listica=list(range(1,6))
        listica.remove(i)
        L1.append(ListasPosibles(listica))
    for i in range(len(L0)):
        Lista0=np.array(L0[i],int)   
        for j in range(len(L1[Lista0[0]])):
            C=np.zeros((6,6),int)
            C[0:1,1:]=Lista0
            Lista1=np.array(L1[Lista0[0]][j])
            Bool=Lista1-Lista0[1:]
            if len(Bool[Bool==0])==0:
                C[1:2,2:]=Lista1
                for dia in range(1,6):
                    listica2=[2,3,4,5]
                    if dia!=Lista0[0]:
                        listica2.remove(L0[i].index(dia)+1)
                        listica2.remove(L1[Lista0[0]][j].index(dia)+2)
                        if C[listica2[0]][listica2[1]]!=0:
                            C[0][1]=0
                            break
                        else:
                            C[listica2[0]][listica2[1]]=dia
                if C[0][1]!=0:
                    C+=C.T
                    C=np.where(C==0,Lista0[0],C) 
                    D=np.concatenate((C*Calen,(C+5)*(-1)*Calen,(C+10)*Calen),axis=1)
                    if verif1C9(D,6,3,3) and distC9(D,6,3,DistProv)[1]<Optimus:
                        CalOp=D
                        Optimus=distC9(D,6,3,DistProv)[1]
    return distC9(CalOp,6,3,DistProv),CalOp

# -----------------------------------------------------------------------------
# Función que devuelve una lista de todos los posibles calendarios de la ronda 1 ordenados por la distancia recorrida 
def ListOrdR_1(S):
    Calen=Mascara(S)
    ListaOrd=[]
    ListaDist=[]
    L0=ListasPosibles(list(range(1,6)))
    L1=[[]]
    for i in range(1,6):
        listica=list(range(1,6))
        listica.remove(i)
        L1.append(ListasPosibles(listica))
    for i in range(len(L0)):
        Lista0=np.array(L0[i],int)   
        for j in range(len(L1[Lista0[0]])):
            C=np.zeros((6,6),int)
            C[0:1,1:]=Lista0
            Lista1=np.array(L1[Lista0[0]][j])
            Bool=Lista1-Lista0[1:]
            if len(Bool[Bool==0])==0:
                C[1:2,2:]=Lista1
                for dia in range(1,6):
                    listica2=[2,3,4,5]
                    if dia!=Lista0[0]:
                        listica2.remove(L0[i].index(dia)+1)
                        listica2.remove(L1[Lista0[0]][j].index(dia)+2)
                        if C[listica2[0]][listica2[1]]!=0:
                            C[0][1]=0
                            break
                        else:
                            C[listica2[0]][listica2[1]]=dia
                if C[0][1]!=0:
                    C+=C.T
                    C=np.where(C==0,Lista0[0],C)
                    C*=Calen
                if verif1C9(C,6,1,3):
                    distancia=distC9(C,6,1,DistProv)[1]
                    if len(ListaOrd)==0:
                        ListaOrd.append(C)
                        ListaDist.append(distancia)
                    else:
                        indice=Ubicar(distancia,ListaDist,0,len(ListaDist))
                        if indice==len(ListaDist):
                            ListaOrd.append(C)
                            ListaDist.append(distancia)
                        else: 
                            ListaOrd.append(0)
                            ListaDist.append(0)
                            ListaDist[indice+1:]=ListaDist[indice:len(ListaDist)-1]
                            ListaOrd[indice+1:]=ListaOrd[indice:len(ListaDist)-1]
                            ListaOrd[indice]=C
                            ListaDist[indice]=distancia
    return ListaOrd

# Función que devuelve una lista de todos los posibles calendarios de la ronda 2 ordenados por la distancia recorrida 
def ListOrdR_2(S):
    Calen=Mascara(S)*(-1)
    ListaOrd=[]
    ListaDist=[]
    L0=ListasPosibles(list(range(1,6)))
    L1=[[]]
    for i in range(1,6):
        listica=list(range(1,6))
        listica.remove(i)
        L1.append(ListasPosibles(listica))
    for i in range(len(L0)):
        Lista0=np.array(L0[i],int)   
        for j in range(len(L1[Lista0[0]])):
            C=np.zeros((6,6),int)
            C[0:1,1:]=Lista0
            Lista1=np.array(L1[Lista0[0]][j])
            Bool=Lista1-Lista0[1:]
            if len(Bool[Bool==0])==0:
                C[1:2,2:]=Lista1
                for dia in range(1,6):
                    listica2=[2,3,4,5]
                    if dia!=Lista0[0]:
                        listica2.remove(L0[i].index(dia)+1)
                        listica2.remove(L1[Lista0[0]][j].index(dia)+2)
                        if C[listica2[0]][listica2[1]]!=0:
                            C[0][1]=0
                            break
                        else:
                            C[listica2[0]][listica2[1]]=dia
                if C[0][1]!=0:
                    C+=C.T
                    C=np.where(C==0,Lista0[0],C)
                    C*=Calen
                if verif1C9(C,6,1,3):
                    distancia=distC9(C,6,1,DistProv)[1]
                    if len(ListaOrd)==0:
                        ListaOrd.append(C)
                        ListaDist.append(distancia)
                    else:
                        indice=Ubicar(distancia,ListaDist,0,len(ListaDist))
                        if indice==len(ListaDist):
                            ListaOrd.append(C)
                            ListaDist.append(distancia)
                        else:
                            ListaOrd.append(0)
                            ListaDist.append(0)
                            ListaDist[indice+1:]=ListaDist[indice:len(ListaDist)-1]
                            ListaOrd[indice+1:]=ListaOrd[indice:len(ListaDist)-1]
                            ListaOrd[indice]=C
                            ListaDist[indice]=distancia
    return ListaOrd

# Función que devuelve una lista de todos los calendarios de las rondas 1 y 2, ordenados por la distancia recorrida
def ListOrdR_12(S):
    Calen=Mascara(S)
    L1=ListOrdR_1(S)
    L2=ListOrdR_2(S)
    ListaOrd=[]
    ListaDist=[]
    for i in range(len(L1)):
        for j in range(len(L2)):
            C=np.concatenate((L1[i],L2[j]-5*Calen),axis=1)
            distancia=distC9(C,6,2,DistProv)[1]
            if len(ListaOrd)==0:
                ListaOrd.append(C)
                ListaDist.append(distancia)
            else:
                indice=Ubicar(distancia,ListaDist,0,len(ListaDist))
                if indice==len(ListaDist):
                    ListaOrd.append(C)
                    ListaDist.append(distancia)
                else:
                    ListaOrd.append(0)
                    ListaDist.append(0)
                    ListaDist[indice+1:]=ListaDist[indice:len(ListaDist)-1]
                    ListaOrd[indice+1:]=ListaOrd[indice:len(ListaDist)-1]
                    ListaOrd[indice]=C
                    ListaDist[indice]=distancia
    return ListaOrd

# Función que genera un calendario con la lista de los calendarios simples
def Caltimus1(S,m1,m2,m3):
    Calen=Mascara(S)
    L1=ListOrdR_1(S)
    L2=ListOrdR_2(S)
    CalOp=OptimoYparejo(S)[1]
    DistOp=distC9(CalOp,6,3,DistProv)
    for i in range(m1):
        for j in range(m2):
            for k in range(m3):
                Caltimus=np.concatenate((L1[i],L2[j]-5*Calen,L1[k]+10*Calen),axis=1)
                Distimus=distC9(Caltimus,6,3,DistProv)
                if verif1C9(Caltimus,6,3,3) and verif22C9(Caltimus,6) and Distimus[1]<DistOp[1]:
                    DistOp=Distimus
                    CalOp=Caltimus
    return DistOp,CalOp

# Función que genera un calendario con la lista de calendarios dobles y con la de los simples
def Caltimus2(S,m1,m2):
    Calen=Mascara(S)
    L1=ListOrdR_12(S)
    L2=ListOrdR_1(S)
    CalOp=OptimoYparejo(S)[1]
    DistOp=distC9(CalOp,6,3,DistProv)
    for i in range(m1):
        for j in range(m2):
            Caltimus=np.concatenate((L1[i],L2[j]+10*Calen),axis=1)
            if verif22C9(Caltimus,6) and verif1C9(Caltimus,6,3,3): 
                Distimus=distC9(Caltimus,6,3,DistProv)
                if Distimus[1]<DistOp[1]:
                    DistOp=Distimus
                    CalOp=Caltimus
    return DistOp,CalOp

print(ListasPosibles([1,2,3,4]))