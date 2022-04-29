
"""Listas bidimensionales
Se necesita desarrollar una aplicación que procese la información de las variables meteorológicas temperatura, humedad y presión atmosférica. 
El registro de estas variables se hace cada una hora durante todos los días del mes. Esto se guarda en un archivo de texto separado con coma que contiene los siguientes datos: número de día, hora, valor de la variable temperatura, valor de la variable humedad y valor de la variable presión atmosférica. Se genera un archivo por cada mes.
Defina la clase “Registro” que posea como atributos los valores de las tres variables meteorológicas que se registran.
Implemente un programa que:
1. Defina una lista bidimensional en la que se almacene el registro de las variables meteorológicas (instancia de la clase Registro) para cada día del mes, por cada hora.
2. Almacene en la lista bidimensional los datos registrados en el archivo.
3. Presente un menú de opciones permita realizar las siguientes tareas:
3.1. Mostrar para cada variable el día y hora de menor y mayor valor.
3.2. Indicar la temperatura promedio mensual por cada hora.
3.3. Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato.
Hora	Temperatura	Humedad	Presión
0	        xx	      xx	  xx
1	        xx	      xx	  xx
…	        …	      …	       …
…	        …	      …        …
22	        xx	      xx	  xx
23	        xx	      xx	  xx
"""
from os import path
import csv
from modulo1 import Registro

if __name__=="__main__":

    def Mostrar_Dia_Y_Hora(L):

        ma1,me1,ma2,me2,ma3,me3=0.0,99999.0,0.0,99999.0,0.0,99999.0
        pdt=pht=pdt2=pht2=pdh=phh=pdh2=phh2=pdp=php=pdp2=php2=0
        
        for i in range(len(L)):
            for j in range(len(L[i])):

                t,h,p=L[i][j].Temp(),L[i][j].Humed(),L[i][j].Press()
                

                if t>ma1:
                    ma1=t
                    pdt=i
                    pht=j
                if t<me1:
                    me1=t
                    pdt2=i
                    pht2=j
                if h>ma2:
                    ma2=h
                    pdh=i
                    phh=j
                if h<me2:
                    me2=h
                    pdh2=i
                    phh2=j
                if p>ma3:
                    ma3=p
                    pdp=i
                    php=j
                if p<me3:
                    me3=p
                    pdp2=i
                    php2=j

        print("Temperatura: Mayor valor, día:",pdt+1," hora:",pht+1)
        print("Temperatura: Menor valor, día:",pdt2+1," hora:",pht2+1)
        print()
        print("Humedad: Mayor valor, día:",pdh+1," hora:",phh+1)
        print("Humedad: Menor valor, día:",pdh2+1," hora:",phh2+1)
        print()
        print("Presión Atmosférica: Mayor valor, día:",pdp+1," hora:",php+1)
        print("Presión Atmosférica: Menor valor, día:",pdp2+1," hora:",php2+1)
        print()

    def Temperatura_Promedio(L):
        for j in range(24):
            prom=0
            for i in range(30):
                prom+=L[i][j].Temp() #L[0][0]
            print("Hora:",j,"---Promedio mensual:{:.2f}".format(prom/30))
    def Listar_Dia(L):

        dia=int(input("Ingrese día a listar:"))
        dia-=1
        print("Hora     Temperatura     Humedad     Presión")

        for j in range(len(L[dia])):

            print(j,"       ",L[dia][j].Temp(),"        ",L[dia][j].Humed(),"       ",L[dia][j].Press())

    def Menu(Lista):
        op=None

        while(op!='0'):

            print("Menu de opciones:")
            print()
            print("1:Mostrar para cada variable el día y hora de menor y mayor valor")
            print("2:Mostrar temperatura promedio mensual por cada hora")
            print("3:Listar valores de las tres variables para cada hora del día a ingresar")
            print("0:Para salir")
            print()
            op=input("Ingresar opción:")

            if op=='1':
                Mostrar_Dia_Y_Hora(Lista)
            if op=='2':
                Temperatura_Promedio(Lista)
            if op=='3':
                Listar_Dia(Lista)

    Lista=[]

    for i in range(30):
        Lista.append([0]*24)

    with open(path.dirname(__file__)+ "/mes.csv","r") as f:
        reader=csv.reader(f,delimiter=',')
        for linea in reader:
            dia= int(linea[0])
            hora= int(linea[1])
            temperatura=linea[2]
            humedad=float(linea[3])
            presion=float(linea[4])
            Lista[dia-1][hora-1]=Registro(temperatura,humedad,presion)

    Menu(Lista)

