from os import path
from csv import reader
from modulo1 import Viajero_Frecuente

if __name__=="__main__":

    def Leer_Archivo(path: str) -> list[Viajero_Frecuente]:
        with open(path, "r") as f:
            return list(map(lambda lista: Viajero_Frecuente(int(lista[0]),lista[1],lista[2],lista[3],float(lista[4])),reader(f,delimiter=",")))

    def Viajero_Mayor_Cantidad(Lista):
        mayor=Lista[0]

        for l in Lista:
            if l>mayor:
                mayor=l
        print()
        print("Tiene mayor cantidad de millas el viajero ",mayor.Get_Num())

    def Acumular_Millas(Lista):

        print()
        num=int(input("Ingrese numero de viajero frecuente:"))

        for l in Lista:
            if num == l:
                print()
                cant=float(input("Ingrese cantidad de millas a acumular:"))
                l+=cant
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

                    l-=cant
                    print()
                    print("Millas a canjear restantes:",l.Get_Millas())
                else:
                    print("Error en la operación")

    Lista=Leer_Archivo(path.dirname(__file__)+ "/viajero.txt")
    Viajero_Mayor_Cantidad(Lista)
    Acumular_Millas(Lista)
    Canjear_Millas(Lista)