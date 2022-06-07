from zope.interface import implementer
from Nodo import Nodo
from IAgente import IAgentes
from Docente import Docente
from DocenteInvestigador import DocenteInvestigador
from Investigador import Investigador
from Apoyo import PersonalApoyo
from Personal import Personal


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
                    if isinstance(aux.getDato(), DocenteInvestigador):
                        print("Tipo de Agente: Docente Investigador")
                    else:
                        print("Tipo de Agente: Personal de Apoyo")
        except IndexError:
            print("Posicion Invalida")

    def generarListaOrdenada(self):
        carrera = input("Ingrese Carrera: ")
        lista = []
        for nodo in self:
            if isinstance(nodo, DocenteInvestigador) and nodo.getCarrera() == carrera:
                lista.append(nodo)
        list.sort(lista, key=lambda DocenteInvestigador: DocenteInvestigador.getCarrera())
        for i in range(len(lista)):
            print(lista[i])

    def categoriaInvetigacion(self, area): #punto 5
        contDI = 0
        contI = 0
        aux = self.__comienzo
        while aux != None:
            if isinstance( aux.getDato(), DocenteInvestigador ):
                if aux.getDato().getArea() == area:
                    contDI += 1
            elif isinstance( aux.getDato(), Investigador ):
                if aux.getDato().getArea() == area:
                    contI += 1
            aux = aux.getSig()
        print('Cantidad de Docentes Investigadores: ', contDI)
        print('Cantidad de Investigadores: ', contI)

    def Sueldos(self):
        lista = []
        aux = self.__comienzo
        while aux != None:
            lista.append( aux.getDato() )
            aux = aux.getSig()
        list.sort( lista, key=lambda Personal: Personal.getApellido() )
        for agente in lista:
            importe = agente.Sueldo()
            
            if isinstance( agente, DocenteInvestigador ):
                print('DocenteInvestigador: ', agente.getApellido(), agente.getNombre(), importe)
            elif isinstance( agente, Docente ):
                print('Docente: ',agente.getApellido(), agente.getNombre(), importe)
            elif isinstance( agente, Investigador ):
                print('Investigador: ',agente.getApellido(), agente.getNombre(), importe)
            elif isinstance( agente, PersonalApoyo ):
                print('Personal Apoyo: ',agente.getApellido(), agente.getNombre(), importe)

    def listar (self, cat):
        aux = self.__comienzo
        importe = 0
        while aux != None:
            if isinstance(aux.getDato(), DocenteInvestigador):
                if aux.getDato().getCategoriaIncentivos() == cat:
                    importe += aux.getDato().getExtra()
                    print(aux.getDato().getApellido(), aux.getDato().getNombre(), aux.getDato().getExtra())
            aux = aux.getSig()
        print('Total de dinero que la Secretaría de Investigación debe solicitar al Ministerio: ',importe)
            
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
            unAgente = DocenteInvestigador(cuil=input('Cuil: '),
                                          apellido=input('Apellido: '),
                                          nombre=input('Nombre: '),
                                          basico=float(input('Sueldo Básico: ')),
                                          antiguedad=int(input('Antiguedad: ')),
                                          carrera=input('Carrera: '),
                                          cargo=input('Cargo: '),
                                          area=input('Area: '),
                                          tipoInvestigador=input('Tipo de Investigador: '),
                                          catedra=input('Catedra: '),
                                          categoriaIncentivo=input('Categoria Incentivo: '),
                                          extra=input('Extra: '))

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