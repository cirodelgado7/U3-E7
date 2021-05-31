from zope.interface import Interface

class IAgentes(Interface):

    def insertarAgente(elemento, indice):
        pass

    def agregarAgente(elemento):
        pass

    def mostrarAgente(indice):
        pass
