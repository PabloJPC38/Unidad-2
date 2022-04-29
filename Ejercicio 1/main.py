from cgitb import text
from modulo1 import Email

def test():
    objeto_Prueba=Email('pablo','gmail','com','12345')
    print('Valores de prueba:{}'.format(objeto_Prueba.retornaEmail()))

if __name__== "__main__":

    test()
    nom=input("Ingrese nombre:")
    cuenta=input("Ingrese cuenta:")
    ident=input("Ingrese identificador:")
    dominio=input("Ingrese dominio:")
    tip=input("Ingrese tipo de dominio:")
    password=input("Ingrese contraseña:")
    print()

    objeto=Email(ident,dominio,tip,password)

    print("Estimado "+nom+" te enviaremos tus mensajes a la dirección "+objeto.retornaEmail())

    print()
    print("Se requiere cambiar contraseña...")
    c=input("Ingrese contraseña actual:")
    if c==objeto.psw:
        n=input("Ingrese nueva contraseña:")
        objeto.psw=n
        print()
        print("Nueva contraseña:"+ objeto.psw)
    else: print("Contraseña invalida")

    print()
    direccion=input("Por favor, ingrese la direccion de correo: ")
    objeto2=Email.crearCuenta(direccion)
    print(objeto2.retornaEmail()+" creada!!")

    with open("Cuentas.txt", "r", encoding="utf8") as arch:
        l=arch.readline()
        lista=l.split(",")
        lista_objetos=list(map(lambda x: Email.crearCuenta(x), lista))
        cont=0
        identic=input("Ingrese un identificador de cuenta: ")
        for cuenta in lista_objetos:
            if identic==cuenta.getID():
                cont=cont+1
        if cont>=1:
            print("Se encuentra repetido")
