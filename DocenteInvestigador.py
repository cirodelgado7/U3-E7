from Docente import Docente
from Investigador import Investigador


class DocenteInvestigador(Docente, Investigador):

    __categoriaIncentivo = ''
    __extra = 0.0

    def __init__(self, **kwargs):
        self.__categoriaIncentivo = kwargs.pop("categoriaIncentivo")
        self.__extra = float(kwargs.pop("extra"))
        super().__init__(**kwargs)

    def __str__(self):
        cadena = '\n***** Docente Investigador *****'
        cadena += super().__str__()
        cadena += '\nCategoria Incentivo: ' + self.__categoriaIncentivo
        cadena += '\nExtra: ' + str(self.__extra)
        return cadena

    def getCategoriaIncentivos(self):
        return self.__categoriaIncentivo

    def getExtra(self):
        return self.__extra

    def Sueldo(self):
        return  Docente.Sueldo(self) + self.__extra

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                extra=self.__extra,
                categoriaIncentivo=self.__categoriaIncentivo,
            )
        )
        d.get("__atributos__").update(super().toJSON().get("__atributos__"))
        return d