from datetime import date
class Campaña:
    def __init__(self,nombre:str,fecha_inicio:date,fecha_termino:date):
        self.__nombre=nombre
        self.__fecha_inicio=fecha_inicio
        self.__fecha_termino=fecha_termino

    @property
    def nombre(self):
        return self.__nombre

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @fecha_inicio.setdefault()
    def fecha_inicio(self,fecha_inicio):
        self.__fecha_inicio=fecha_inicio

    @fecha_termino.setter
    def set_fecha_termino(self,fecha_termino):
        self.__fecha_termino=fecha_termino


    def __str__(self):
        return f"Nombre de la campaña: {self.nombre}"
