from __future__ import annotations


class Conjunto:

    __conjunto:list[int]=[]

    def __init__(self,conjunto:list[int]=[]):

        self.__conjunto=conjunto

    def __str__(self)->str:

        return str(self.__conjunto)

    def __add__(self,otro:Conjunto) -> Conjunto:

        result:list[int]=[]

        for x in self.__conjunto:
            result.append(x)
        for x in otro.__conjunto:
            if x not in result:
                result.append(x)

        return Conjunto(result)

    def __sub__(self,otro:Conjunto) -> Conjunto:

        result:list[int]=[]

        for x in self.__conjunto:
            if x not in otro.__conjunto:
                result.append(x)

        return Conjunto(result)

    def __eq__(self,otro:Conjunto)->bool:

        if len(self.__conjunto) != len(otro.__conjunto):  # type: ignore
            return False

        for elemento in self.__conjunto:
            if elemento not in otro.__conjunto:  # type: ignore
                return False

        return True
