# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 01:30:31 2020

@author: Sofi
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


#Preliminares
Cal=np.array([[13, 14, 16, 12, 15,  0,  9, 10,  0,  0,  6,  0,  0,  0,  0,  0], 
              [14, 13, 15, 11, 16, 12, 10,  9,  0,  0,  0,  0,  0,  0,  0,  0],
              [15, 16, 14,  9, 13, 10, 12, 11,  0,  0,  0,  0,  0,  0,  0,  0],
              [16, 15, 13, 10, 14,  9, 11, 12,  0,  0,  0,  0,  0,  0,  0,  0],
              [ 0,  0,  0,  0,  0,  0,  0,  0,  3,  5,  1,  2,  4,  6,  7,  8],
              [ 0,  0,  0,  0,  0,  0,  0,  0,  5,  3,  2,  1,  6,  4,  8,  7],
              [ 0,  0,  0,  1,  0,  2,  3,  5,  0,  0,  0,  0,  9, 10, 11, 12],
              [ 0,  1,  5,  6,  0,  0,  0,  7,  0,  9, 12,  0, 14,  0,  0, 15],
              [ 7,  8,  4,  0,  6,  0,  0,  0, 16, 15, 13, 14,  0,  0,  0,  0],
              [ 8,  7,  6,  0,  4,  0,  0,  0, 15, 16, 14, 13,  0,  0,  0,  0],
              [ 0,  0,  2,  7,  1,  8,  0,  0, 12, 11,  0,  0, 16, 15,  0,  0],
              [ 0,  0,  0,  2,  0,  1,  5,  3,  0,  0,  0,  0, 10,  9, 12, 11],
              [ 0,  0,  0,  0,  0,  0,  0,  0,  1,  2,  5,  3,  7,  8,  4,  6],
              [ 0,  0,  0,  0,  0,  0,  0,  0,  2,  1,  3,  5,  8,  7,  6,  4],
              [12, 11, 10, 14,  9, 13, 16, 15,  0,  0,  0,  0,  0,  0,  0,  0],
              [11, 12,  9, 13, 10, 14, 15, 16,  0,  0,  0,  0,  0,  0,  0,  0],
              [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
              [ 0,  0,  0,  0,  0, 11,  0,  0,  7,  8,  0,  4,  1,  2,  5,  3],
              [ 0,  0,  0,  0,  0,  0,  0,  0,  8,  7,  4,  6,  2,  1,  3,  5],
              [ 0,  0,  0,  0,  0,  0,  0,  0,  4,  6,  8,  7,  5,  3,  1,  2],
              [ 0,  0,  0,  0,  0,  0,  0,  0,  6,  4,  7,  8,  3,  5,  2,  1],
              [ 9, 10, 12, 15, 11, 16, 13, 14,  0,  0,  0,  0,  0,  0,  0,  0],
              [10,  9, 11, 16, 12, 15, 14, 13,  0,  0,  0,  0,  0,  0,  0,  0],
              [ 4,  6,  7,  0,  8,  0,  0,  0, 13, 14, 15, 16,  0,  0,  0,  0],
              [ 3,  5,  0,  0,  0,  0,  6,  4,  0,  0,  9, 10,  0,  0, 13, 14],
              [ 0,  0,  0,  3,  0,  5,  1,  2,  0,  0,  0,  0, 11, 12, 10,  9],
              [ 2,  0,  0,  0,  3,  4,  8,  0, 10,  0,  0, 11,  0, 13, 16,  0],
              [ 0,  0,  1,  8,  2,  7,  0,  0, 11, 12,  0,  0, 15, 16,  0,  0],
              [ 6,  4,  8,  0,  7,  0,  0,  0, 14, 13, 16, 15,  0,  0,  0,  0],
              [ 5,  3,  0,  0,  0,  0,  4,  6,  0,  0, 10,  9,  0,  0, 14, 13],
              [ 0,  0,  0,  5,  0,  3,  2,  1,  0,  0,  0,  0, 12, 11,  9, 10]], int)

Dist=np.array([[   0, 114, 163, 211, 179, 274, 393, 442, 517, 582, 698, 817, 896, 899,1038,1086],
               [ 114,   0,  65, 113,  61, 177, 296, 344, 419, 484, 600, 719, 799, 801, 941, 989],
               [ 163,  65,   0,  51,  54, 106, 233, 281, 357, 421, 538, 657, 736, 739, 880, 961],
               [ 211, 113,  51,   0,  35,  68, 192, 238, 314, 389, 505, 624, 702, 706, 846, 893],
               [ 179,  61,  54,  35,   0, 103, 225, 273, 348, 413, 529, 648, 728, 730, 869, 918],
               [ 274, 177, 106,  68, 103,   0, 172, 221, 296, 361, 477, 596, 675, 678, 817, 865],
               [ 393, 296, 233, 192, 225, 172,   0,  73, 148, 213, 329, 448, 528, 530, 670, 718],
               [ 442, 344, 281, 238, 273, 221,  73,   0,  96, 161, 277, 396, 476, 478, 618, 666],
               [ 517, 419, 357, 314, 348, 296, 148,  96,   0,  76, 192, 311, 391, 393, 532, 581],
               [ 582, 484, 421, 389, 413, 361, 213, 161,  76,   0, 115, 234, 313, 316, 455, 503],
               [ 698, 600, 538, 505, 529, 477, 329, 277, 192, 115,   0, 127, 206, 209, 348, 396],
               [ 817, 719, 657, 624, 648, 596, 448, 396, 311, 234, 127,   0,  80,  82, 222, 270],
               [ 896, 799, 736, 702, 728, 675, 528, 476, 391, 313, 206,  80,   0,  72, 147, 195],
               [ 899, 801, 739, 706, 730, 678, 530, 478, 393, 316, 209,  82,  72,   0, 142, 190],
               [1038, 941, 880, 846, 869, 817, 670, 618, 532, 455, 348, 222, 147, 142,   0,  81],
               [1086, 989, 961, 893, 918, 865, 718, 666, 581, 503, 396, 270, 195, 190,  81,   0]], int)


#=============================================================================================================================================
#Pregunta 1

def distancia(equipo,jornada):
    if jornada==1:
        if Cal[0,equipo-1]==0:
            d=0
        else:
            d=Dist[equipo-1,Cal[0,equipo-1]-1]
    else:
        C=Cal[jornada-2:jornada,equipo-1:equipo]
        for i in range(2):
            if C[i,0]==0:
                C[i,0]=equipo
        d=Dist[C[0,0]-1,C[1,0]-1]
    return d


#=============================================================================================================================================
#Pregunta 2

Total=np.zeros((16,32),int)
for i in range(16):
    T=0
    for j in range(31):
        Total[i,j]=distancia(i+1,j+1)
        T+=Total[i,j]
    Total[i,31]=T


#=============================================================================================================================================
#Gráficos
    
#Distancias recorridas por cada equipo  
fig1=plt.figure(figsize=(10,6))
ax1=fig1.add_subplot(111)
X1=['PRI','ART','IND','MAY','IJU','MTZ','CFG','VCL','SSP','CAV','CMG','LTU','HOL','GRA','SCU','GTM']
Y1=Total[:,31:].reshape(16)
Figura=ax1.barh(X1,Y1,color='gray')
ax1.axis('tight')
plt.ylabel('Equipos',fontsize=13)
plt.xlabel('Kilómetros recorridos',fontsize=13)
plt.title('Kilómetros recorridos por equipo',fontsize=18)
band1 = ax1.axvspan (5000,5500)
band2 = ax1.axvspan (5500,6000)
band3 = ax1.axvspan (6000,6500)
band4 = ax1.axvspan (6500,7000)
band5 = ax1.axvspan (7000,8000)
band1.set_color('green')
band1.set_alpha (0.4)
band2.set_color('yellow')
band2.set_alpha (0.3)
band3.set_color('orange')
band3.set_alpha (0.4)
band4.set_color('red')
band4.set_alpha (0.4)
band5.set_color('red')
band5.set_alpha (0.5)
for i in range(16):
    plt.text(Y1[i],-0.2 + i,Y1[i])
fig1.savefig('grafico 1.jpg',format='jpg')


#=============================================================================================================================================
#Litros de combustible empleados por cada equipo 

fig2=plt.figure(figsize=(10,6))
ax2=fig2.add_subplot(111)
Y2=Y1/3.5
for i in range (16):
    Y2[i]=round(Y2[i],1)
Figura=ax2.barh(X1,Y2)
ax2.axis('tight')
plt.ylabel('Equipos',fontsize=13)
plt.xlabel('Litros de combustible Diesel',fontsize=13)
plt.title('Cantidad promedio de combustible requerida',fontsize=18)
for i in range(16):
    plt.text(Y2[i]-160,-0.2 + i,Y2[i],color='white')
fig2.savefig('grafico 2.jpg',format='jpg')


#=============================================================================================================================================
#Horas de descanso de cada equipo

DiasViajes=np.zeros((16))
for i in range(16):
    for j in range(31):
        if distancia(i+1,j+1)!=0:
            DiasViajes[i]+=1

HorasDescansoXdias=np.zeros((16))
for i in range(16):
    HorasDescansoXdias[i]=12-Total[i,31]/80/DiasViajes[i]


#Cantidad promedio de horas de descanso en un día de traslado por equipo
fig3=plt.figure(figsize=(10,6))
ax3=fig3.add_subplot(111)
Y3=HorasDescansoXdias
for i in range (16):
    Y3[i]=round(Y3[i],2)
colores1=[0]*16
for i in range(16):
    if Y3[i]<7.4:
        colores1[i]='red'
    elif Y3[i]<7.8:
        colores1[i]='orange'
    elif Y3[i]<8.2:
        colores1[i]='yellow'
    elif Y3[i]<8.6:
        colores1[i]='#00C800'
    else:
        colores1[i]='green' 
Figura=ax3.bar(X1,Y3,color=colores1)
ax3.axis('tight')
plt.xlabel('Equipos',fontsize=13)
plt.ylabel('Cantidad de horas',fontsize=13)
plt.title('Cantidad promedio de horas de descanso en un día de traslado',fontsize=18)
colores=['green','#00C800','yellow','orange','red']
texto=['Más de 8.6h', 'Entre 8.2h y 8.6h', 'Entre 7.8h y 8.2h', 'Entre 7.2h y 7.4h', 'Menos de 7.4h']
leyenda=[]
for i in range(5):
    leyenda.append(mpatches.Patch(color=colores[i],label=texto[i]))         
plt.legend(leyenda,handles=leyenda,loc='lower left')
for i in range(16):
    plt.text(i-0.3,Y3[i]+0.05,Y3[i])
fig3.savefig('grafico 3.jpg',format='jpg')


#Cantidad promedio de horas de descanso en un día de traslado por equipo II
fig31=plt.figure(figsize=(10,6))
ax31=fig31.add_subplot(111)
YY=(np.arange(-7.5,8,1)**2)*(-0.0218)+8.8054
Figura=(ax31.bar(X1,Y3,color=colores1),ax31.plot(X1,Y3,color='blue',alpha=1,marker='.'),ax31.plot(X1,YY,color='blue',alpha=0.6,linestyle='--'))
ax31.axis('tight')
plt.xlabel('Equipos',fontsize=13)
plt.ylabel('Cantidad de horas',fontsize=13)
plt.title('Cantidad promedio de horas de descanso en un día de traslado',fontsize=18)        
plt.legend(leyenda,handles=leyenda,loc='lower left')
for i in range(16):
    plt.text(i-0.3,Y3[i]+0.05,Y3[i])
fig31.savefig('grafico 31.jpg',format='jpg')


#Cantidad promedio de horas de descanso en un día de traslado por equipo III
fig32=plt.figure(figsize=(10,6))
ax32=fig32.add_subplot(111)
Figura=(ax32.plot(X1,Y3,color='#000099',alpha=1,marker='*'),ax32.plot(X1,YY,color='purple',alpha=0.8,linestyle='--'))
ax31.axis('tight')
plt.xlabel('Equipos',fontsize=13)
plt.ylabel('Cantidad de horas',fontsize=13)
plt.title('Cantidad promedio de horas de descanso en un día de traslado',fontsize=18)    
for i in range(16):
    plt.text(i-0.3,Y3[i]-0.08,Y3[i])
#fig32.savefig('grafico 32.jpg',format='jpg')


#=============================================================================================================================================    
#Distribución promedio del tiempo de un jugador en la 1ra etapa de la Serie Nacional 

fig4=plt.figure(figsize=(10,6))
ax4=fig4.add_subplot(111)
X4=['Horas de juego', 'Horas de viaje', 'Horas de acomodamiento','Horas de sueño', 'Horas de descanso (y entrenamiento)']
p1=round((Total[:,31:].sum())/80/16,2)
p2=4*round((DiasViajes.sum())/16,2)
Y4=[2.5*75,p1,p2,108*8,108*24-2.5*75-8*108-p1-p2]
colores2=['#0070D6','#0040C2','#000099','#000050','#00A9C9']
desfase=(0,0,0,0,0.05)
Figura=ax4.pie(Y4,labels=X4,colors=colores2,autopct='%0.1f%%',explode=desfase)
plt.title('Distribución promedio del tiempo de un jugador durante la serie',fontsize=18)
plt.axis('equal')
#fig4.savefig('grafico 4.jpg',format='jpg')


#=============================================================================================================================================
#Distribución promedio del tiempo de un jugador en un día de traslado

fig5=plt.figure(figsize=(10,6))
ax5=fig5.add_subplot(111)
X5=['Horas de viaje', 'Horas de acomodamiento','Horas de sueño', 'Horas de descanso (y entrenamiento)']
p1=round((Total[:,31:].sum())/80/16,2)
p2=4*round((DiasViajes.sum())/16,2)
Y5=[p1,p2,p2*2,p2*6-p2*2-p1-p2]
colores3=['#0040C2','#000099','#000050','#0090D6']
desfase=(0,0,0,0.05)
Figura=ax5.pie(Y5,labels=X5,colors=colores3,autopct='%0.1f%%',explode=desfase)
plt.title('Distribución promedio del tiempo de un jugador en un día de traslado',fontsize=18)
plt.axis('equal')
#fig5.savefig('grafico 5.jpg',format='jpg')