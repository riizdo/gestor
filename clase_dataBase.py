

class DataBase():
    __completa = {}
    __listas = []
    
    def __init__(self):
        self.cargaDatos()
        
        
    def cargaDatos(self):
        try:
            f = open('lista_tablas.txt', 'r')
            datos = f.read()
            f.close()
            for data in datos.split('\n'):
                self.__listas.append(data)
        except:
            pass
        
        for indice in self.__listas:
            f = open(self.__listas[indice] + '.txt', 'r')
            datos = f.read()
            f.close()
            
            numero = 0
            lista = []
            for fila in datos.split('\n'):
                valores = {}
                if numero == 0:
                    for dato in fila.split('||'):
                        lista.append(dato)
                else:
                    num = 0
                    for dato in fila.split('||'):
                        valores[lista[num]] = dato
                        num += 1
            numero += 1
            
    
    
    def nuevaTabla(self, tabla):
        if tabla in self.__listas:
            pass
        else:
            self.__listas.append(tabla)
            self.__completa[tabla] = []
        
        
    def añadir(self, tabla, *valor):
        pass
    
    
    def mostrar(self):
        print(self.__completa)
    
    
if __name__ == '__main__':
    dataBase = DataBase()