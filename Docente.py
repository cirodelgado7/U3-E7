from Personal import Personal


class Docente(Personal):

    __carrera = ''
    __cargo = ''
    __catedra = ''

    def __init__(self, **kwargs):
        self.__carrera = kwargs.pop("carrera")
        self.__catedra = kwargs.pop("catedra")
        self.__cargo = kwargs.pop("cargo")
        super().__init__(**kwargs)

    def __str__(self):
        cadena = '\n***** Docente *****'
        cadena += super().__str__()
        cadena += '\nCarrera: {}'.format(self.__carrera)
        cadena += '\nCatedra: {}'.format(self.__catedra)
        cadena += '\nCargo: {}'.format(self.__cargo)
        return cadena
        
    def getCarrera(self):
        return self.__carrera 

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

    def Sueldo(self):
        sueldo = self.getBasico()
        if self.__cargo == "simple":
            sueldo += sueldo * 0.1
        elif self.__cargo == "semiexclusivo":
            sueldo += sueldo * 0.2
        elif self.__cargo == "exclusivo":
            sueldo += sueldo * 0.5
        sueldo +=  (0.01 * self.getAntiguedad()) * self.getBasico()
        return sueldo

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                carrera=self.__carrera,
                cargo=self.__cargo,
                catedra=self.__catedra
            )
        )
        d.get("__atributos__").update(super().toJSON().get("__atributos__"))
        return d