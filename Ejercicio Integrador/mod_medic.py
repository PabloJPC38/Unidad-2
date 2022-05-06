class medicamento:

    def __init__(self,id_cama:int,id_medic:int,nbre:str,md:str,ppt:str,cant:int,precio:float):

        self.__id_cama=id_cama
        self.__id_medic=id_medic
        self.__nbre=nbre
        self.__md=md
        self.__ppt=ppt
        self.__cant=cant
        self.__precio=precio

    def Get_Id_cama(self):
        return self.__id_cama
    def Get_Id_medic(self):
        return self.__id_medic
    def Get_Nbre(self):
        return self.__nbre
    def Get_md(self):
        return self.__md
    def Get_PPT(self):
        return self.__ppt
    def Get_Cant(self):
        return self.__cant
    def Get_Precio(self):
        return self.__precio