from datetime import date
from anuncio import Display, Social, Video

class LargoExcedidoException(Exception):
    pass

class AttributeError(Exception):
    pass

class Campaña:
    def __init__(self, nombre:str,fecha_inicio:date,fecha_termino:date,anuncio):
        self.anuncios = []
        self.__nombre=nombre
        self.__fecha_inicio=fecha_inicio
        self.__fecha_termino=fecha_termino

        for info_anuncio in anuncio:
            tipo_anuncio = info_anuncio.pop('tipo')
            if tipo_anuncio == 'Display':
                anuncio = Display(**info_anuncio)
            elif tipo_anuncio == 'Social':
                anuncio = Social(**info_anuncio)
            elif tipo_anuncio == 'Video':
                anuncio = Video(**info_anuncio)
            else:
                raise ValueError(f"Tipo de anuncio desconocido: {tipo_anuncio}")
            self.anuncios.append(anuncio)
    

    @property
    def nombre(self):
        return self.__nombre

    @property
    def fecha_inicio(self):
        raise AttributeError("El atributo fecha_inicio es de solo escritura")
    
    @property
    def fecha_termino(self):
        raise AttributeError("El atributo fecha_termino es de solo escritura")

    @property
    def anuncio(self):
        return self.__anuncio

    @nombre.setter
    def nombre(self,nombre):
        if len(nombre) > 250:
            raise LargoExcedidoException ("El nombre de la campaña es demasiado largo")
        self.__nombre=nombre

    @fecha_inicio.setter
    def fecha_inicio(self,fecha_inicio):
        self.__fecha_inicio=fecha_inicio

    @fecha_termino.setter
    def fecha_termino(self,fecha_termino):
        self.__fecha_termino=fecha_termino



anuncios = [
    {'tipo': 'Display', 'ancho': 1, 'alto': 9, 'url_archivo': 'url_archivo', 'url_clic': 'url_clic', 'sub_tipo': 'tradicional'},
    {'tipo': 'Social', 'ancho': 6, 'alto': 3, 'url_archivo': 'url_archivo', 'url_clic': 'url_clic', 'sub_tipo': 'linkedin'},
    {'tipo': 'Video', 'ancho': 6, 'alto': 7, 'url_archivo': 'url_archivo', 'url_clic': 'url_clic', 'sub_tipo': 'outstream', 'duracion': -8}
]



campagna = Campaña("Campaña 1",date(2021,1,1),date(2021,6,1),anuncios)


try:
    campagna.nombre = "pañaj2gjgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzCampañaj2gjgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
except LargoExcedidoException as e:
    print(e)

try:
    print(campagna.fecha_inicio)
except AttributeError as e:
    print(e)  # Imprime: El atributo1 es de solo escritura

try:
    print(campagna.fecha_termino)
except AttributeError as e:
    print(e)  # Imprime: El atributo1 es de solo escritura