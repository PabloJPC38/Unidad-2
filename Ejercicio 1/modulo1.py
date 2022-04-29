class Email:
    def __init__(self,id,dom,tipo,psw=None):
        self.id=id
        self.dom=dom
        self.tipo=tipo
        self.psw=psw
    def retornaEmail(self):
        return(self.id+"@"+self.dom+"."+self.tipo)
    def getDominio(self):
        return(self.dom)
    def getID(self):
        return(self.id)
    @staticmethod
    def crearCuenta(direc):
        var = direc.split("@")
        var1 = var[1].split(".")
        return Email(var[0], var1[0], var1[1])
