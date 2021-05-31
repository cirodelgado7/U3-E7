from Personal import Personal


class PersonalApoyo(Personal):

    __categoria = int

    def __init__(self, cuil, apellido, nombre, basico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, basico, antiguedad)
        self.__categoria = int(categoria)

    def __str__(self):
        cadena = '\n***** Personal de Apoyo *****'
        cadena += super().__str__()
        cadena += '\nCategoria: {}'.format(self.__categoria)
        return cadena

    def getCategoria(self):
        return self.__categoria

    def Sueldo(self):
        sueldo = self.getBasico()
        if self.__categoria <= 10:
            sueldo *= 0.1
        elif self.__categoria <= 20:
            sueldo *= 0.2
        else:
            sueldo *= 0.3
        sueldo += self.getBasico() * self.getAntiguedad() * 0.1
        return sueldo

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                categoria=self.__categoria
            )
        )
        d.get("__atributos__").update(super().toJSON().get("__atributos__"))
        return d