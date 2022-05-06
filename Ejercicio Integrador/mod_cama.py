class Cama:

    def __init__(self,id:int,hab:int,est:bool,NyA:str|None,diag:str|None,f_intern:str|None,f_alta:str|None):

        self.__id=id
        self.__hab=hab
        self.__est=est
        self.__NyA=NyA
        self.__diag=diag
        self.__f_intern=f_intern
        self.__f_alta=f_alta

    def Get_Id(self)->int:
        return self.__id
    def Get_Hab(self):
        return self.__hab
    def Get_Est(self):
        return self.__est
    def Get_NyA(self):
        if self.__NyA==None:
            return "No existe paciente"
        else:
            return self.__NyA
    def Get_Diag(self)->str:
        return self.__diag or "No existe paciente"
    def Get_F_Intern(self):
        return self.__f_intern or "No existe paciente"
    def Get_F_Alta(self):
        return self.__f_alta
    def Set_F_Alta(self,fecha):
        self.__f_alta=fecha
