from os import path
from csv import reader
from modulo1 import Viajero_Frecuente

if __name__=="__main__":

    def Leer_Archivo(path: str) -> list[Viajero_Frecuente]:
        with open(path, "r") as f:
            return list(map(lambda lista: Viajero_Frecuente(int(lista[0]),lista[1],lista[2],lista[3],float(lista[4])),reader(f,delimiter=",")))

    def Comparar(Lista):

        print()
        num=int(input("Ingrese un numero de pasajero:"))
        print()
        valor=float(input("Ingrese un valor a comparar:"))

        for l in Lista:
            if num == l:
                if l==valor:
                    print("Es igual")
                else:
                    print("No es igual")

    def Acumular_Millas(Lista):

        print()
        num=int(input("Ingrese numero de viajero frecuente:"))

        for l in Lista:
            if num == l:
                print()
                cant=float(input("Ingrese cantidad de millas a acumular:"))
                cant+=l
                print()
                print("Millas acumuladas:",l.Get_Millas())

    def Canjear_Millas(Lista):
        print()
        num=int(input("Ingrese numero de viajero frecuente:"))

        for l in Lista:
            if num == l:
                print()
                cant=float(input("Ingrese cantidad de millas a canjear:"))
                if l>=cant:

                    cant-=l
                    print()
                    print("Millas a canjear restantes:",l.Get_Millas())
                else:
                    print("Error en la operación")

    Lista=Leer_Archivo(path.dirname(__file__)+ "/viajero.csv")
    Comparar(Lista)
    Acumular_Millas(Lista)
    Canjear_Millas(Lista)
