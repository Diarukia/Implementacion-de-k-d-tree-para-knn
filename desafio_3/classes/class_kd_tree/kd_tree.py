from classes.class_node.node import _node
import copy

dimensions = 13

class kd__tree:
    def __init__(self,df_app,genre_dict):
        self.df_app = df_app
        self.genre_dict = genre_dict
        self.root = None
        self.iteration = 0
    
    def run(self,fila):
        print("se buscaran los mas cercanos a esta aplicacion")
        print(self.fix_df(self.df_app.iloc[[fila]]) )
        print('insertando...')
        for i in range(len(self.df_app.index)):
            self.root = self.insertar(self.root,self.df_app.iloc[[i]])
        vecinos = self.knn(self.root,self.fix_df(self.df_app.iloc[[fila]]),10)
        return vecinos

    def insertar(self,root,df_row):
        return self.insertarRec(root,df_row,0)

    def insertarRec(self,root,df_row,depth):#df row, es el dato a guardar en el nodo, junto el numero del genero
        global dimensions
        if(root == None):
            root = _node.create_node_charge_data(df_row,self.genre_dict,depth)
            return root
        cd = depth % dimensions
        df_app_ = self.fix_df(copy.deepcopy(df_row))
        if(self.special_case(df_app_.iloc[0][cd])  < self.special_case(root.df_row.iloc[[0][0]][cd])):
            root.izq = self.insertarRec(root.izq,df_row,depth+1)
        else:
            root.der = self.insertarRec(root.der,df_row,depth+1)
        return root

    def fix_df(self, df_app):
        del df_app["track_name"]
        del df_app["currency"]
        del df_app["ver"]
        df_app = df_app.replace(df_app.iloc[0][9],self.genre_dict[df_app.iloc[0][9]])
        return df_app

    def special_case(self,df_value):
        if(type(df_value) == type('a')):
            return float(df_value[0])
        return df_value

    def knn(self,root,dato,n): #asumimos que dato es un par columna valor 
        global dimensions # dato es una fila del df
        dimension_ = None
        puntos_ordenados = list() # ordenados del mejor al peor
        pila = list()
        pila.insert(0,root)
        while(len(pila) > 0):
            self.iteration += 1
            nodo = pila.pop(0)
            dimension_ = nodo.depth % dimensions
            if((len(puntos_ordenados) < n)):
                puntos_ordenados.insert(0,nodo)
                self.ordenar(puntos_ordenados,dato.iloc[0][dimension_],dimension_)
            elif((self.euclidian_distance(dato.iloc[0][dimension_],nodo.df_row.iloc[[0][0]][dimension_]) < self.euclidian_distance(dato.iloc[0][dimension_],puntos_ordenados[0].df_row.iloc[[0][0]][dimension_]))):
                puntos_ordenados.pop(0)
                puntos_ordenados.insert(0,nodo)
                self.ordenar(puntos_ordenados,dato.iloc[0][dimension_],dimension_)
            if(dato.iloc[0][dimension_] < nodo.df_row.iloc[[0][0]][dimension_]):
                pila.insert(0,nodo.der)
                pila.insert(0,nodo.izq)
            else:
                pila.insert(0,nodo.der)
                pila.insert(0,nodo.izq)
            pila = self.quitar_null(pila,root)
        print('La cantidad de iteraciones son ',self.iteration )
        return puntos_ordenados

    def euclidian_distance(self,dato,list_value):
        dato = self.special_case(dato)
        list_value = self.special_case(list_value)
        return abs((dato)-(list_value))

    def ordenar(self,lista,dato,dimension_):
        n = len(lista)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if(self.euclidian_distance(dato,lista[j].df_row.iloc[[0][0]][dimension_]) < self.euclidian_distance(dato,lista[j+1].df_row.iloc[[0][0]][dimension_])):
                    lista[j] , lista[j+1] = lista[j+1] , lista[j]

    def quitar_null(self,pila,root):
        aux_pila = []
        for i in range(len(pila)):
            if(pila[i] != None ):
                aux_pila.append(pila[i])
        return aux_pila

    def mostrar_arbol(self,root):
        if(root == None):
            return
        self.mostrar_arbol(root.izq)
        print(root.df_row)
        self.mostrar_arbol(root.der)

    def imprimir_datos(self, lista):
        for i in lista:
            print(i.df_row)
        return
