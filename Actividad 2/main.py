from os import path
from csv import reader
from modulo1 import Viajero_Frecuente

if __name__=="__main__":

    def Leer_Archivo(path: str) -> list[Viajero_Frecuente]:
        with open(path, "r") as f:
            return list(map(lambda lista: Viajero_Frecuente(int(lista[0]),lista[1],lista[2],lista[3],float(lista[4])),reader(f,delimiter=",")))

    def Menu(lista: list[Viajero_Frecuente]):
        n=int(input("Ingrese numero de viajero frecuente:"))
        op=None
        for x in lista:

            if n==x.numero_viajero():

                while(op!='0'):

                    if op=='a':
                        total=x.cantidadTotaldeMillas()
                        print("Total de millas para el viajero de número ",n,":",total)
                    elif op=='b':
                        cm=float(input("Ingrese cantidad de millas:"))
                        cant=x.acumularMillas(cm)
                        print("Millas acumuladas por el viajero de número ",n,":",cant)
                    elif op=='c':
                        cc=float(input("Ingrese cantidad de millas a canjear:"))
                        resto=x.canjearMillas(cc)
                        print("Total de millas para el viajero de número ",n,":",resto)
                    print()
                    print("Opciones:")
                    print()
                    print("a-Consultar cantidad de millas:")
                    print("b-Acumular millas:")
                    print("c-Canjear millas:")
                    print("0_Salir:")
                    print()
                    op=input("Elegir opción:")

    Lista=Leer_Archivo(path.dirname(__file__)+ "/viajero.txt")
    Menu(Lista)
    #print(Lista)