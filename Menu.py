class Menu:

    __switcher = None

    def __init__(self):
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4,
            5: self.opcion5,
            6: self.opcion6,
            7: self.opcion7,
            8: self.salir}

    def mostrarMenu(self, lista):
        salir = False
        while not salir:
            print("\n********** Agentes Universitarios ****************")
            print("******************* Menu *************************"
                  "\n1. Insertar Agentes a la Colección"
                  "\n2. Agregar Agentes a la colección"
                  "\n3. Mostrar tipo de agente"
                  "\n4. Generar listado de Docentes Investigadores"
                  "\n5. Mostrar Investigadores"
                  "\n6. Generar un listado con datos de agentes"
                  "\n7. Mostrar importe extra y total"
                  "\n8. Salir")
            op = int(input('Ingrese una opcion: '))
            if op in range(1, 9) and type(op) is not str:
                self.opcion(op, lista)
                salir = op == 8
            else:
                print('La opción ingresada no es valida. Ingrese una opción válida')

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, lista):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func( lista )

    def opcion1(self, lista):
        print('\n1. Insertar Agentes a la Colección')
        unAgente = lista.registrarAgente()
        lista.insertarAgente( unAgente )

    def opcion2(self, lista):
        print('\n2. Agregar Agentes a la Colección')
        unAgente = lista.registrarAgente()
        lista.agregarAgente( unAgente )

    def opcion3(self, lista):
        print('\n3. Mostrar tipo de agente')
        lista.mostrarTipoAgente()

    def opcion4(self, lista):
        print('\n4. Generar listado de Docentes Investigadores')
        lista.generarListaOrdenada()

    def opcion5(self, lista):
        print('\n5. Mostrar Investigadores')
        area = input('Ingrese el area de investigacion: ')
        lista.categoriaInvetigacion( area )

    def opcion6(self, lista):
        print('\n6. Generar un listado con datos de agentes')
        lista.Sueldos()

    def opcion7(self, lista):
        print('\n7. Mostrar importe extra y total')
        cat = input('Ingrese una categoria (I, II, III, IV o V): ')
        lista.listar( cat )

    def salir(self, lista):
        print('Salir')