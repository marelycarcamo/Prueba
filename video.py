from anuncio import Anuncio
class Video(Anuncio):
    formato = "video"
    sub_tipos = ("instream","outstream")

    def __init__(self,ancho:int,alto:int,url_archivo:str,url_clic:str,sub_tipo:str):
		super().__init__(self,ancho:1,alto:1,duracion:int):
			self.__ancho = ancho
			self.__alto = alto
			self.__duracion = duracion
			self.formato = "video"
			self.sub_tipos = ("instream","outstream")

    def get_ancho(self):
        return self.__ancho

    def get_alto(self):
        return self.__alto

    def get_duracion(self):
        return self.__duracion


def comprimir_anuncio(self):
	print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")
	return


