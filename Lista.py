from zope.interface import implementer
from Nodo import Nodo
from IAgente import IAgentes
from Docente import Docente
from DocenteInvetigador import DocenteInvetigador
from Investigador import Investigador
from Apoyo import PersonalApoyo


@implementer(IAgentes)
class Lista(object):

    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self

    def __len__(self):
        return self.__tope

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSig()
            return dato

    def insertarAgente(self, agente):
        nuevoNodo = Nodo(agente)
        indice = int(input('Ingrese la posición en la que lo desea ubicar: '))
        aux = self.__comienzo
        if aux is None:
            self.__comienzo = nuevoNodo
            self.__actual = nuevoNodo
            self.__tope += 1
        else:
            i = 0
            ant = aux
            aux = aux.getSig()
            while aux is not None and i < indice:
                ant = aux
                aux = aux.getSig()
                i += 1
            if i < indice:
                ant.setSig(nuevoNodo)
                self.__tope += 1
                del aux

    def agregarAgente(self, agente):
        nuevoNodo = Nodo(agente)
        aux = self.__comienzo
        if aux is None:
            self.__comienzo = nuevoNodo
            self.__actual = nuevoNodo
            self.__tope += 1
        else:
            ant = aux
            aux = aux.getSig()
            while aux is not None:
                ant = aux
                aux = aux.getSig()
            if aux is None:
                ant.setSig(nuevoNodo)
                self.__tope += 1
                del aux

    def mostrarTipoAgente(self):
        try:
            indice = int(input("Indice de la lista: "))
            aux = self.__comienzo
            i = 0
            while i < indice and aux is not None:
                aux = aux.getSig()
                i += 1
            if aux is None:
                raise IndexError
            else:
                if isinstance(aux.getDato(), Investigador):
                    print("Tipo de Agente: Investigador")
                else:
                    if isinstance(aux.getDato(), DocenteInvetigador):
                        print("Tipo de Agente: Docente Investigador")
                    else:
                        print("Tipo de Agente: Personal de Apoyo")
        except IndexError:
            print("Posicion Invalida")

    def generarListaOrdenada(self):
        carrera = input("Ingrese Carrera: ")
        aux = self.__comienzo
        cota = None
        k = None
        while k is not aux:
            k = self.__comienzo
            p = self.__comienzo
            while aux.getSig() is not cota:
                if isinstance(aux, DocenteInvetigador) and p.getDato().getCarrera() == carrera:
                    aux = p.getSig().getDato()
                    p.setSig(p.getDato()).getDato()
                    p.setDato(aux)
                    k = p
                p.setSig(p)
            cota = k.getSig()
        while aux is not None:
            print("\n - {}".format(aux))

    def agentesinvestigacion(self):
        investigadores = 0
        docentesInvetigadores = 0
        for nodo in self:
            if isinstance(nodo, DocenteInvetigador):
                docentesInvetigadores += 1
            elif isinstance(nodo, Investigador):
                investigadores += 1
        return investigadores, docentesInvetigadores

    def catinvetigacion(self, categoria):
        categoria = categoria.upper()
        aux = []
        for nodo in self:
            if isinstance(nodo, DocenteInvetigador) and nodo.getCategoriaIncentivos() == categoria:
                aux.append(nodo)
        return aux

    def Sueldos(self):
        lista = []
        bandera = True
        for agente in self:
            i = 0
            if bandera:
                lista.append(agente)
                bandera = False
            else:
                while i < len(lista) and lista[i].getApellido() < agente.getApellido():
                    i += 1
                lista.insert(i, agente)
        return lista

    def toJSON(self):
        return dict(
            __class__=self.__class__.__name__,
            Lista=[Lista.toJSON() for Lista in self]
        )

    def registrarAgente(self):
        op = int(input('1. Docente - 2. Investigador - 3. Docente Investigador - 4. Personal de Apoyo: '))
        if op == 1:
            unAgente = Docente(cuil=input('Cuil: '),
                               apellido=input('Apellido: '),
                               nombre=input('Nombre: '),
                               basico=float(input('Sueldo Básico: ')),
                               antiguedad=int(input('Antiguedad: ')),
                               carrera=input('Carrera: '),
                               cargo=input('Cargo: '),
                               catedra=input('Catedra: '))
            return unAgente
        elif op == 2:
            unAgente = Investigador(cuil=input('Cuil: '),
                                    apellido=input('Apellido: '),
                                    nombre=input('Nombre: '),
                                    basico=float(input('Sueldo Básico: ')),
                                    antiguedad=int(input('Antiguedad: ')),
                                    area=input('Area: '),
                                    tipoInvestigador=input('Tipo de Investigador: '))
            return unAgente
        elif op == 3:
            unAgente = DocenteInvetigador(cuil=input('Cuil: '),
                                          apellido=input('Apellido: '),
                                          nombre=input('Nombre: '),
                                          basico=float(input('Sueldo Básico: ')),
                                          antiguedad=int(input('Antiguedad: ')),
                                          area=input('Area: '),
                                          tipoInvestigador=input('Tipo de Investigador: '))
            return unAgente
        elif op == 4:
            unAgente = PersonalApoyo(cuil=input('Cuil: '),
                                     apellido=input('Apellido: '),
                                     nombre=input('Nombre: '),
                                     basico=float(input('Sueldo Básico: ')),
                                     antiguedad=int(input('Antiguedad: ')),
                                     categoria=input('Categoria Incentivo: '))
            return unAgente
        else:
            print('La opción ingresada no es válida')