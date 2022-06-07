class Nodo(object):

    __dato = None
    __sig = None

    def __init__(self, Dato):
        self.__dato = Dato
        self.__sig = None

    def setSig(self, siguiente):
        self.__sig = siguiente

    def getSig(self):
        return self.__sig   

    def getDato(self):
        return self.__dato
