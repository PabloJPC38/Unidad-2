from os import path
from csv import reader
from modulo1 import PlanAhorro

if __name__=="__main__":

    def Leer_Archivo(path:str)-> list[PlanAhorro]:

        with open(path,"r") as f:
            return list(map(lambda lista:PlanAhorro(lista[0],lista[1],lista[2],float(lista[3])),reader(f,delimiter=";")))

    def Actualizar_Valor(Lista):

        for l in Lista:
            print()
            l.Mostrar()
            v=input("Ingrese valor actualizado:")
            l.Actualizar(v)
            l.Mostrar_Valores_Actualizados()
            print()

    def Mostrar_Datos(Lista):
        v=float(input("Ingrese valor:"))
        print()
        for l in Lista:

            if l.Get_Valor()<v:
                l.Mostrar()

    def Monto_A_Pagar(Lista):

        for l in Lista:
            print()
            #print(l.Valor_Cuota())
            print("Monto a pagar por el vehiculo ",l.Get_Modelo(),":",(l.Valor_Cuota()*l.Cantidad_De_Cuotas()))

    def Modificar_Cuotas(Lista):
        print()
        print("Cantidad actual de cuotas:",PlanAhorro.Get_Cuotas_Licitar())
        print()
        c=int(input("Ingrese nueva cantidad de cuotas:"))
        PlanAhorro.Modificar_Cantidad_Cuotas(c)
        print()
        print("Cantidad actual de cuotas (modificado):",PlanAhorro.Get_Cuotas_Licitar())

    def Menu(Lista):

        op=None
        while op!="0":

            print()
            print("1: Actualizar valor de vehículo:")
            print("2: Mostrar vehículos inferiores a un valor")
            print("3: Monto para licitar un vehículo:")
            print("4: Modificar cantidad de cuotas")
            print("0: Salir")
            print()
            op=input("Ingresar opción:")
            print()

            if op=="1":
                Actualizar_Valor(Lista)
            if op=="2":
                Mostrar_Datos(Lista)
            if op=="3":
                Monto_A_Pagar(Lista)
            if op=="4":
                Modificar_Cuotas(Lista)

    Lista=Leer_Archivo(path.dirname(__file__)+"/planes.csv")
    print()
    Menu(Lista)


