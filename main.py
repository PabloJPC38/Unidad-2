from modulo import Hotel
from operator import itemgetter,attrgetter
from functools import cmp_to_key

if __name__=="__main__":

    def comparar(a:Hotel,b:Hotel):
        if  a.calidad_precio()>b.calidad_precio():
            return 1
        elif a.calidad_precio()<b.calidad_precio():
            return -1
        else:
            return 0

    hotel=[Hotel("Hilton","Buenos Aires",80,100000),Hotel("Del Bono Park","San Juan",50,30000),Hotel("Ankara Suites","Salta",70,20000)]

    print()
    #************************EJEMPLO 1*************************************#
    print(sorted(hotel, key=lambda x:x.nombre))
    print()
    #************************EJEMPLO 2*************************************#
    print(sorted(hotel, key=lambda x: x.nombre, reverse=True))
    print()
    #************************EJEMPLO 3*************************************#
    print(sorted(hotel, key=itemgetter(0)))
    print()
    print(sorted(hotel, key=itemgetter(0),reverse=True))
    print()
    print(sorted(hotel, key=attrgetter('nombre')))
    print()
    print(sorted(hotel, key=attrgetter('nombre'),reverse=True))
    print()
    #************************EJEMPLO 4*************************************#
    print(sorted(hotel,key=cmp_to_key(comparar),reverse=True))
