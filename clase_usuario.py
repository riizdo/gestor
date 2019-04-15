


class Usuario():
    __lista_completa = []
    __lista_atributos = ['nombre', 'contraseña', 'departamento', 'inicio', 'tipo']
    
    
    def __init__(self):
        self.__nombre = 'invitado'
        self.__contraseña = ''
        self.__departamento = ''
        self.__inicio = ''
        self.__tipo = ''
        self.cargaDatos()


    def cargaDatos(self):
        f = open('Data/usuarios.txt', 'r')
        datos = f.read()
        for linea in datos.split('\n'):
            numero = 0
            lista = {}
            for dato in linea.split('||'):
                lista[self.__lista_atributos[numero]] = dato
                numero += 1
            self.__lista_completa.append(lista)
        f.close()
        
        
    def guardaDatos(self):
        lista = {}
        lista[self.__lista_atributos[0]] = self.__nombre
        lista[self.__lista_atributos[1]] = self.__contraseña
        lista[self.__lista_atributos[2]] = self.__departamento
        lista[self.__lista_atributos[3]] = self.__inicio
        lista[self.__lista_atributos[4]] = self.__tipo
        
        self.__lista_completa.append(lista)
        
        datos = None
        try:
            f = open('Data/usuarios.txt', 'r')
            datos = f.read()
            f.close()
        except:
            pass
        
        f = open('Data/usuarios.txt', 'w')
        newData = (self.__nombre + '||' + self.__contraseña + '||' + self.__departamento + '||' + self.__inicio + '||' + self.__tipo)
        if datos == None:
            f.write(newData)
        else:
            f.write(datos + '\n' + newData)
        f.close()
        
        
    def mostrarUsuarios(self):
        print(self.__lista_completa)
        
        
    def nombre(self, nombre = None):
        if nombre == None:
            return self.__nombre
        else:
            self.__nombre = nombre
            return None
            
            
    def contraseña(self, contraseña = None):
        if contraseña == None:
            return self.__contraseña
        else:
            self.__contraseña = contraseña
            return None
            
            
    def departamento(self, departamento = None):
        if departamento == None:
            return self.__departamento
        else:
            self.__departamento = departamento
            return None
            
            
    def inicio(self, inicio = None):
        if inicio == None:
            return self.__inicio
        else:
            self.__inicio = inicio
            return None
        
            
    def tipo(self, tipo = None):
        if tipo == None:
            return self.__tipo
        else:
            self.__tipo = tipo
            return None
        
        
class Tecnico(Usuario):
    __historial = []
    
    def __init__(self):
        Usuario.__init__(self)
        
        

    
            
if __name__ == '__main__':
    usuario = Tecnico()