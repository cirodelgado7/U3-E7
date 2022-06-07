import abc


class Personal(abc.ABC):

    __cuil = ''
    __apellido = ''
    __nombre = ''
    __basico = 0.0
    __antiguedad = 0

    def __init__(self, cuil, apellido, nombre, basico, antiguedad):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__basico = float(basico)
        self.__antiguedad = int(antiguedad)

    def __str__(self):
        cadena = '\nCuil: {}'.format(self.__cuil)
        cadena += '\nApellido: {}'.format(self.__apellido)
        cadena += '\nNombre: {}'.format(self.__nombre)
        cadena += '\nSueldo Básico: ${}'.format(self.__basico)
        cadena += '\nAntiguedad: {}'.format(self.__antiguedad)
        return cadena

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getCuil(self):
        return self.__cuil

    def getBasico(self):
        return self.__basico

    def getAntiguedad(self):
        return self.__antiguedad

    def toJSON(self):
        return dict(
            __atributos__=dict(
                cuil=self.__cuil,
                apellido=self.__apellido,
                nombre=self.__nombre,
                basico=self.__basico,
                antiguedad=self.__antiguedad
            )
        )

    @abc.abstractmethod
    def Sueldo(self):
        pass