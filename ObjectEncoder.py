import json
from pathlib import Path
from Lista import Lista
from Docente import Docente
from Apoyo import PersonalApoyo
from Investigador import Investigador
from DocenteInvetigador import DocenteInvetigador

class ObjectEncoder(object):

    def writer(self, agentes, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(agentes, destino, indent=4)
        return True

    def reader(self, archivo):
        with Path(archivo).open("r", encoding="UTF-8") as fuente:
            aux = json.load(fuente)
        return aux

    def decodificarDiccionario(self, d):
        if "__class__" not in d:
            return d 
        else:
            class_name = d["__class__"]
            class_ = eval(class_name)
            if class_name == "Lista":
                nodos = d["Nodos"]
                Lista = class_()
                for i in range(len(nodos)):
                    dNodo = nodos[i]
                    class_name = dNodo.pop("__class__")
                    class_ = eval(class_name)
                    atributos = dNodo["__atributos__"]
                    unAgente = class_(**atributos)
                    Lista.agregarAgente(unAgente)
                return Lista