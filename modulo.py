from math import pow
class Hotel:

    def __init__(self,nombre:str,ubicacion:str,puntaje:int,precio:float):

        self.nombre=nombre
        self.ubicacion=ubicacion
        self.puntaje=puntaje
        self.precio=precio

    def __repr__(self):
        return '({}, {} , {} , {})'.format(self.nombre, self.ubicacion,self.puntaje,self.precio)
    
    def __getitem__(self,i):
        return self.nombre or self.precio or self.puntaje or self.ubicacion
    
    def calidad_precio(self):
        return float((pow(self.puntaje,2)*10)/self.precio)






