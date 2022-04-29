class Ventana:

    def __init__(self,title="Por defecto",vsx=0,vsy=0,vix=1,viy=1):
        self.__title=title
        self.__vsx=vsx
        self.__vsy=vsy
        self.__vix=vix
        self.__viy=viy
    
    def mostrar(self):
        if self.__vsx<self.__vix and self.__vsx>=0 and self.__vix<=500 and self.__vsy<self.__viy and self.__vsy>=0 and self.__viy<=500:
            print()
            print(self.__title," ",self.__vsx," ",self.__vsy," ",self.__vix," ",self.__viy)
        else:
            print("Valores fuera de los límites")
    
    def getTitulo(self):
        return self.__title
    
    def alto(self):
        if self.__vsy<self.__viy and self.__vsy>=0 and self.__viy<=500:
            return self.__viy-self.__vsx
        else:
            print("Valores fuera de los límites")
    
    def ancho(self):
        if self.__vsx<self.__vix and self.__vsx>=0 and self.__vix<=500:
            return self.__vsx+self.__vix
        else:
            print("Valores fuera de los límites")
    
    def moverDerecha(self,desplazamiento=1):
        if self.__vsx + desplazamiento<=500 and self.__vix + desplazamiento<=500:
            self.__vsx+=desplazamiento
            self.__vix+=desplazamiento
        else:
            print("Valores fuera de los límites")
    
    def moverIzquierda(self,desplazamiento=1):
        if self.__vsx + desplazamiento>=0 and self.__vix + desplazamiento>=0:
            self.__vsx-=desplazamiento
            self.__vix-=desplazamiento
        else:
            print("Valores fuera de los límites")
    
    def bajar(self,desplazamiento=1):
        if self.__vsy + desplazamiento<=500 and self.__viy + desplazamiento<=500:
            self.__vsy-=desplazamiento
            self.__viy-=desplazamiento
        else:
            print("Valores fuera de los límites")
    
    def subir(self,desplazamiento=1):
        if self.__vsy + desplazamiento>=0 and self.__viy + desplazamiento>=0:
            self.__vsy+=desplazamiento
            self.__viy+=desplazamiento
        else:
            print("Valores fuera de los límites")

