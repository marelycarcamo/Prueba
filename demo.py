import logging
# Configurar el registro de errores
logging.basicConfig(filename='error.log', level=logging.ERROR)
from datetime import date
from campaña import LargoExcedidoException, Campaña, Video
from anuncio import SubTipoInvalidoException

# Inicializar la lista de anuncios
listado_anuncios = []

# Crear la campaña
campaña = Campaña("Campaña Inicial", date(2021, 1, 1), date(2021, 6, 1),listado_anuncios)

# Crear una instancia de Campaña con un anuncio de tipo Video
anuncios = [
    {'tipo': 'Video', 'ancho': 1920, 'alto': 1080, 'url_archivo': 'video.mp4', 'url_clic': 'https://example.com', 'sub_tipo': 'outstream', 'duracion': 30},
]

# Llamar al método __crear_anuncios en la instancia de Campaña
listado_anuncios=campaña._crear_anuncios(anuncios)

print(campaña)

    # Visualizar los anuncios
for anuncio in campaña.listado_anuncios:
	print(anuncio)

try:
    # Solicitar nuevo nombre de la campaña
    nuevo_nombre = input("\nIngrese un nuevo nombre para la campaña: ")
    campaña.nombre = nuevo_nombre
    print(f'--- El nombre de la campaña se actualizó correctamente."{nuevo_nombre}" ---')
	
        # Solicitar nuevo sub_tipo para el anuncio
    nuevo_sub_tipo = input("\nIngrese un nuevo sub_tipo para el anuncio: ").lower().strip()
    campaña.listado_anuncios[0].sub_tipo = nuevo_sub_tipo
    print(f'--- El tipo de anuncio, se actualizó correctamente "{campaña.listado_anuncios[0].sub_tipo}" ---')

except (SubTipoInvalidoException, LargoExcedidoException) as e:
    logging.error(str(e))
    print(f"Se produjo un error: {e}.")

