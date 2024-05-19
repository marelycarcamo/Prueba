from anuncio import Anuncio
class Display(Anuncio):
    formato = "display"
    sub_tipos = ("tradicional","native")
    def _init__(self,ancho:int,alto:int,url_archivo:str,url_clic:str,sub_tipo:str,formato,sub_tipos):
        super().init(ancho,alto,url_archivo,url_clic,sub_tipo)

def comprimir_anuncio(self):
	print("COMPRESIÓN DE DISPLAY NO IMPLEMENTADA AÚN")
	return



display = Display(1, 1, "url_archivo", "url_clic", "tradicional")
display.comprimir_anuncio()



    