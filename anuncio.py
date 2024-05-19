from abc import ABC, abstractmethod
class SubTipoInvalidoException(Exception):
    pass

class Anuncio(ABC):
    def __init__(self,ancho:int,alto:int,url_archivo:str,url_clic:str,sub_tipo:str):
        self.__ancho = ancho
        self.__alto = alto
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho

    @property
    def alto(self):
        return self.__alto

    @property
    def url_archivo(self):
        return self.__url_archivo

    @property
    def url_clic(self):
        return self.__url_clic

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @ancho.setter
    def ancho(self,ancho:int):
        self.__ancho = ancho if ancho > 0 else 1

    @alto.setter
    def alto(self,alto:int):
        self.__alto = alto if alto > 0 else 1

    @url_archivo.setter
    def url_archivo(self,url_archivo:str):
        self.__url_archivo = url_archivo

    @url_clic.setter
    def url_clic(self,url_clic:str):
        self.__url_clic = url_clic

    @sub_tipo.setter
    def sub_tipo(self, sub_tipo:str):
        if sub_tipo is not None and sub_tipo != "":
            if sub_tipo not in self.sub_tipos:
                raise SubTipoInvalidoException(f"El subtipo {sub_tipo} no es válido para el formato {self.formato}")
        self.__sub_tipo = sub_tipo

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensinar_anuncio(self):
        pass

    @staticmethod
    def mostrar_formatos(formato, sub_tipos):
        print(f"FORMATO: {formato}")
        print("==========")
        for sub_tipo in sub_tipos:
            print(f"- {sub_tipo}")


class Display(Anuncio):
    formato = "display"
    sub_tipos = ("tradicional","native")
    def __init__(self,ancho:int,alto:int,url_archivo:str,url_clic:str,sub_tipo:str):
        super().__init__(ancho,alto,url_archivo,url_clic,sub_tipo)
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")
        return

    def redimensinar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")
        return



display = Display(1, 1, "url_archivo", "url_clic", "tradicional")
try:
    display.sub_tipo = "invalido"
except SubTipoInvalidoException as e:
    print(e)


display.comprimir_anuncio()
display.redimensinar_anuncio()
Anuncio.mostrar_formatos(Display.formato, Display.sub_tipos)



class Social(Anuncio):
    formato = "social"
    sub_tipos = ("facebook","linkedin")
    def __init__(self,ancho:int,alto:int,url_archivo:str,url_clic:str,sub_tipo:str):
        super().__init__(ancho,alto,url_archivo,url_clic,sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE REDES SOCIALES NO IMPLEMENTADA AÚN")
        return

    def redimensinar_anuncio(self):
        print("REDIMENSIONAMIENTO DE REDES SOCIALES NO IMPLEMENTADA AÚN")
        return

social = Social(6, 3, "url_archivo", "url_clic", "linkedin")
try:
    display.sub_tipo = "invalido"
except SubTipoInvalidoException as e:
    print(e)
social.comprimir_anuncio()
social.redimensinar_anuncio()
Anuncio.mostrar_formatos(Social.formato, Social.sub_tipos)


class Video(Anuncio):
    formato = "video"
    sub_tipos = ("instream","outstream")
    def __init__(self,ancho:int,alto:int,url_archivo:str,url_clic:str,sub_tipo:str,duracion:int):
        super().__init__(ancho,alto,url_archivo,url_clic,sub_tipo)
        self.__duracion = duracion
        self.__alto = 1
        self.__ancho = 1
        

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")
        return

    def redimensinar_anuncio(self):
        print("REDIMENSIONAMIENTO DE VIDEO NO IMPLEMENTADA AÚN")
        return

video = Video(1, 1, "url_archivo", "url_clic", "instream",10)
try:
    display.sub_tipo = "invalido"
except SubTipoInvalidoException as e:
    print(e)
video.comprimir_anuncio()
video.redimensinar_anuncio()
Anuncio.mostrar_formatos(Video.formato, Video.sub_tipos)