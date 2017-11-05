# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:10:18 2017

@author: Angeles
"""

finished=[]
discovered=[]

nodos=[]
cantidad = raw_input()
cantidad=cantidad.split()
#three back forwad croos
#tree
try:
    c1=int(cantidad[0])
    ct=int(cantidad[3])
    if  int(cantidad[3])  == 0 and  int(cantidad[1])>0 :
        ct= int(cantidad[2]) 
    elif  int(cantidad[3]) >0:
        ct =  int(cantidad[3]) 
        
    if int(cantidad[0])==0:
        nodos.append(1)
        
    elif int(cantidad[1])>int(cantidad[0]): # se hace por separado si el 3 edges es mayor o menor
        
        
        if int(cantidad[1])>int(cantidad[0]):
            c1=int(cantidad[1])
        for i in range(c1 + ct):
            nodos.append([]) # se crean los nodos
        for i in range(int(cantidad[0])-int(cantidad[3])):
            nodos[i].append(i+1) # se conectan secuencialmennte
        
        for i in range (len(nodos)-int(cantidad[3])-int(cantidad[1]),len(nodos)-int(cantidad[3])): # se hacen los back
            
            if i-1 < 0:
                nodos[-int(cantidad[3])-1].append(0)
            else:
                nodos[i].append(i-1)
      
        # lo conecto con los otros para que se finalicen antes de volver a buscarlos por el stack del 1        
        for i in range (int(cantidad[2])): # forward
             nodos[i].append(len(nodos)-i -ct-1)              

        for i in range (len(nodos)-int(cantidad[3]),len(nodos)):# reservo un nodo especial para los cross
            nodos[0].append(i)
            nodos[i].append(i-1)
            
 
    
    elif int(cantidad[0])>=int(cantidad[1]): # cuando tree edges es mayor que los back
        if  int(cantidad[3])  == 0 and  int(cantidad[1])>0 :
            ct= 1
        
        for i in range(ct+c1):
        	 nodos.append([])
        
         
        for i in range (1,int(cantidad[0])+1): # se conectan todos al principal
            nodos[0].append(i)
        
          
        
        for i in range(len(nodos[0])-int(cantidad[1])-1,len(nodos[0])-1): # s conectan los back al principal
            nodos[nodos[0][i]].append(0)
        
        
        for i in range(1,int(cantidad[2])+1): # los forweard salen del segundo
            nodos[1].append(nodos[0][i])
            
        for i in range(len(nodos[0])-int(cantidad[3]),len(nodos[0])): # los cross salen de las conecciones primarias 
            nodos[nodos[0][i]].append(i)
    
    print len(nodos)
    for i in nodos:
        # se imprime la cantidad de nodos conectados
        print len(i),
        for k in i:
            print k, # luego los conectados
        print "\n"
except :
    print 'No se puede hacer el grafo'
  