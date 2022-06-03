# Importar librería Queue
from queue import Queue


class Grafo:
    """
    Clase de representación de un Grafo
    ...
    Atributos
    ----------
    num_Nodos : int
        Número de nodos del grafo
    dirigido : boolean
        Tipo de grafo dirigido o no dirigido

    Métodos
    -------
    Métodos Definidos

    __init__(numNodos, dirigido=True):
        Constructor de la clase Grafo, con todos sus atributos

    agregar_Arista(nodo1, nodo2, peso=1):
        Añade una arista a los nodos y agrega peso

    imprimir_ListaAdj():
        Impresión del gráfo

    busqueda_por_Profundidad(nodo_Inicio):
        Primera búsqueda por amplitud o anchura
    """
    # Constructor
    def __init__(self, num_Nodos, dirigido=True):
        """
        Método constructor de la clase Grafo, donde inicializa sus parámetros

        Parámetros
            ----------
            num_Nodos : int
                Número de nodos del grafo
            dirigido : boolean
                Tipo de grafo dirigido o no dirigido
        """
        # Define el número de nodos
        self.m_num_Nodos = num_Nodos
        # Define el rango del número de nodos
        self.m_Nodos = range(self.m_num_Nodos)

        # Tipo de grafo dirigido o no dirigido
        self.m_dirigido = dirigido

        # Representación de la lista de adyacencia
        # Para la implementación de la lista de adyacencia se usa un diccionario
        self.m_lista_adyacencia = {node: set() for node in self.m_Nodos}

    # Añande una arista al grafo
    def agregar_Arista(self, nodo1, nodo2, peso=1):
        '''
        Agrega una arista a los nodos del grafo, además añade el peso de cada 
        arista.

        Parámetros
        ----------
        nodo1 : int
            Entrada de dato tipo entero para el nodo1 
        nodo2 : int
            Entrada de dato tipo entero para el nodo2 
        peso : int
            Entrada de dato tipo entero para el 
        '''

        #En la lista de adyacencia toma el nodo 1 y agrega el nodo 2 y su peso.
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))

        # Agrega una arista a otro nodo cuando el grafo no sea dirigido
        if not self.m_dirigido:
            # Se agrega al nodo 2, el nodo 1 y su peso
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))

    # Imprime de manera representativa el grafo creado
    def imprimir_ListaAdj(self):
        # Realiza un recorrido con un for sobre la lista de adyacencia
        for llave in self.m_lista_adyacencia.keys():
            # Imprime cada nodo que se encuentra en la lista de adyacencia
            print("Nodo", llave, ": ", self.m_lista_adyacencia[llave])

    # Método búsqueda por profundidad 
    def busqueda_por_profundidad(self, inicio, objetivo, ruta = [], visitado = set()):
        '''
        En este método realiza la búsqueda por profundidad donde recorre todos los nodos de manera
        ordenada pero no uniforme

        Parámetros
        ----------
        inicio: int 
            Nodo de inicio para realizar el recorrido
        objetivo: int
            Nodo al que quiere llegar, a tráves del recorrido
        ruta: lista
            Recorrido de la ruta que realiza para llegar el nodo
        visitados: set()
            Inica la lista de nodos que ya han sido recorridos o visitados
        '''
                #Identifica el nodo de  inicio a la ruta
        ruta.append(inicio)
        #Agregar como nodo visitado
        visitado.add(inicio)
        #Si el nodo que esta de inicio es igual al objetivo planteado entonces retorna la ruta 
        if inicio == objetivo:
            return ruta
        #Para esto de desarrolla un ciclo for donde agrega el nodo vecino y el peso a la lista
        #de adyacencia el nodo de inicio
        for (nodoVecino, peso) in self.m_lista_adyacencia[inicio]:
            #En caso de no ser el nodo visitado, debe de recorres el método d búsqueda
            if nodoVecino not in visitado:
                resultado = self.busqueda_por_profundidad(nodoVecino, objetivo, ruta, visitado)
                if resultado is not None:
                    return resultado       
        ruta.pop()
        return None