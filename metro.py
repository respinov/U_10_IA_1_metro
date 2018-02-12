#/usr/bin/env python
# -*- coding: utf-8 -*-
# Vuelos con busqueda en amplitud

from arbol import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):

    solucionado = False
    nodos_visitados = [] 
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        nodo=nodos_frontera[0]
        # Extraer todo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        
        if nodo.get_datos() == solucion:
          # solución encontrada   
          solucionado = True
          return nodo       #nodos_visitados  
        else:
          #Expandir nodos hijo   (ciudades con conexion)
          dato_nodo = nodo.get_datos()
          lista_hijos = []
          for un_hijo in conexiones[dato_nodo]:
             hijo = Nodo(un_hijo)
             lista_hijos.append(hijo)
             if not hijo.en_lista(nodos_visitados)\
             and not hijo.en_lista(nodos_frontera):
                 nodos_frontera.append(hijo)
          nodo.set_hijos(lista_hijos)    
         
    
if __name__=="__main__": 
    conexiones = {
    #Linea 2
    'Taxquena':{'GAnaya'},
    'GAnaya':{'Taxquena','Ermita'},
    'Ermita':{'GAnaya','Portales','Mexicaltzingo','ECentral'},
    'Portales':{'Ermita','Nativitas'}, 
    'Nativitas':{'Portales','VCortes'},
    'VCortes':{'Nativitas','Xola'},
    'Xola':{'VCortes','Viaducto'},
    'Viaducto':{'Xola','Chabacano'},
    'Chabacano':{'Viaducto','SAbad','Jamaica','LCardenas'},
    'SAbad':{'Chabacano','PSuarez'},
    'PSuarez':{'SAbad','Zocalo'},
    'Zocalo':{'PSuarez','Allende'},
    'Allende':{'Zocalo','BArtes'},
    'BArtes':{'Allende','Hidalgo'},
    'Hidalgo':{'BArtes','Revolucion'},
    'Revolucion':{'Hidalgo','SCosme'},
    'SCosme':{'Revolucion','Normal'},
    'Normal':{'SCosme','CMilitar'},
    'CMilitar':{'Normal','Popotla'},
    'Popotla':{'CMilitar','Cuitlahuac'},
    'Cuitlahuac':{'Popotla', 'Tacuba'},
    'Tacuba':{'Cuitlahuac', 'Panteones'},
    'Panteones':{'Tacuba','CCaminos'},
    'CCaminos':{'Panteones'},
    #Fin linea 2
    
    'Mexicaltzingo':{'Ermita','ECentral'},
    'ECentral':{'Ermita','Venados'},
    'Venados':{'Zapata','ECentral'},
    'Zapata':{'Coyoacan','DNorte'},
    'DNorte':{'Zapata'},
    'Coyoacan':{'Zapata'},
        
    #Linea 9
    'Pantitlan':{'Puebla'},
    'Puebla':{'Pantitlan', 'CDeportiva'},
    'CDeportiva':{'Velodromo','Puebla'},
    'Velodromo':{'Mixiuhca','CDeportiva'},
    'Mixiuhca':{'Velodromo', 'Jamaica'},
    'Jamaica':{'Mixiuhca','Chabacano','SAnita','FServando'},
    'LCardenas':{'Chabacano','CMedico'},
    'CMedico':{'LCardenas','Chilpancingo'},
    'Chilpancingo':{'CMedico', 'Patriotismo'},
    'Patriotismo':{'Chilpancingo','Tacubaya'},
    'Tacubaya':{'Patriotismo'},
    #Fin Linea 9
    
    #Linea 4
    'SAnita':{'Jamaica'},
    'FServando':{'Jamaica','Candelaria'},
    'Candelaria':{'FServando', 'Morelos'},
    'Morelos':{'Candelaria','CNorte'},
    'CNorte':{'Morelos', 'Consulado'},
    'Consulado':{'CNorte','Bondojito'},
    'Bondojito':{'Consulado', 'Talisman'},
    'Talisman':{'Bondojito', 'MCarrera'},
    'MCarrera':{'Talisman'},
    #Fin Linea 4
#    '':{},
#    '':{},
    
    
    
    }
     
    estado_inicial = 'Taxquena'
    solucion = 'MCarrera'
    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)
    # mostrar resultado
    resultado =[]
    nodo = nodo_solucion
    while nodo.get_padre() != None:
      resultado.append(nodo.get_datos())
      nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print (resultado)
