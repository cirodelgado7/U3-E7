from Personal import Personal


class Investigador(Personal):

    __area = ''
    __tipoInvestigador = ''

    def __init__(self, **kwargs):
        self.__area = kwargs.pop("area")
        self.__tipoInvestigador = kwargs.pop("tipoInvestigador")
        super().__init__(**kwargs)

    def __str__(self):
        cadena = '\n***** Investigador *****'
        cadena += super().__str__()
        cadena += '\nArea: {}'.format(self.__area)
        cadena += '\nTipo de Investigador: {}'.format(self.__tipoInvestigador)
        return cadena

    def getArea(self):
        return self.__area

    def getTipoInvestigador(self):
        return self.__tipoInvestigador

    def Sueldo(self):
        return self.getBasico() + (0.01 * self.getAntiguedad())

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                area=self.__area,
                tipoInvestigador=self.__tipoInvestigador
            )
        )
        d.get("__atributos__").update(super().toJSON().get("__atributos__"))
        return d