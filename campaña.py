from datetime import date
from anuncio import Display, Social, Video

class LargoExcedidoException(Exception):
    pass

class AttributeError(Exception):
    pass

class Campaña:
    def __init__(self, nombre:str,fecha_inicio:date,fecha_termino:date,listado_anuncios:list):
        self.__listado_anuncios = []
        self.__nombre=nombre
        self.__fecha_inicio=fecha_inicio
        self.__fecha_termino=fecha_termino
        self.__crear_anuncios(anuncios)
    


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
    def listado_anuncios(self):
        return self.__listado_anuncios

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


    @listado_anuncios.setter
    def listado_anuncios(self,listado_anuncios):
        self.__listado_anuncios=listado_anuncios


    def __crear_anuncios(self, anuncios:list):
        for datos_anuncio in anuncios:
            tipo = datos_anuncio['tipo']
            ancho = datos_anuncio['ancho']
            alto = datos_anuncio['alto']
            url_archivo = datos_anuncio['url_archivo']
            url_clic = datos_anuncio['url_clic']
            sub_tipo = datos_anuncio['sub_tipo']
            
            if tipo == "Display":
                anuncio = Display(ancho, alto, url_archivo, url_clic, sub_tipo)
            elif tipo == "Social":
                anuncio = Social(ancho, alto, url_archivo, url_clic, sub_tipo)
            elif tipo == "Video":
                duracion = datos_anuncio.get('duracion', 0)  # Por defecto 0 si no se proporciona duración
                anuncio = Video(ancho, alto, url_archivo, url_clic, sub_tipo, duracion)
            else:
                raise ValueError(f"Tipo de anuncio desconocido: {tipo}")
            
            self.listado_anuncios.append(anuncio)

        
    def __count_anuncios(self):
        counts = {"Display": 0, "Social": 0, "Video": 0}
        for anuncio in self.__listado_anuncios:
            if isinstance(anuncio, Display):
                counts["Display"] += 1
            elif isinstance(anuncio, Social):
                counts["Social"] += 1
            elif isinstance(anuncio, Video):
                counts["Video"] += 1
        return counts

    def __str__(self):
        counts = self.__count_anuncios()
        return (f"Nombre de la campaña: {self.__nombre}\n"
                f"Anuncios: {counts['Video']} Video, {counts['Display']} Display, {counts['Social']} Social")


# Ejemplo de uso
anuncios = [
    {'tipo': 'Display', 'ancho': 1, 'alto': 9, 'url_archivo': 'url_archivo1', 'url_clic': 'url_clic1', 'sub_tipo': 'tradicional'},
    {'tipo': 'Display', 'ancho': 1, 'alto': 8, 'url_archivo': 'url_archivo2', 'url_clic': 'url_clic2', 'sub_tipo': 'native'},
    {'tipo': 'Social', 'ancho': 6, 'alto': 3, 'url_archivo': 'url_archivo3', 'url_clic': 'url_clic3', 'sub_tipo': 'linkedin'},
    {'tipo': 'Video', 'ancho': 6, 'alto': 7, 'url_archivo': 'url_archivo4', 'url_clic': 'url_clic4', 'sub_tipo': 'outstream', 'duracion': 12},
]

campaña = Campaña("Campaña 1", date(2021, 1, 1), date(2021, 6, 1), Campaña.listado_anuncios)

print(campaña)



try:
    campaña.nombre = "pañaj2gjgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzCampañaj2gjgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
except LargoExcedidoException as e:
    print(e)

try:
    print(campaña.fecha_inicio)
except AttributeError as e:
    print(e)  # Imprime: El atributo1 es de solo escritura

try:
    print(campaña.fecha_termino)
except AttributeError as e:
    print(e)  # Imprime: El atributo1 es de solo escritura