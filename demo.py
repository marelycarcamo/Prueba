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
    nuevo_nombre = input("Ingrese un nuevo nombre para la campaña: ")
    campaña.nombre = nuevo_nombre
    print('nombre campaña: ',campaña.nombre)



    
    # Solicitar nuevo sub_tipo para el anuncio
    print('subtipos videos: ', Video.sub_tipos)
    nuevo_sub_tipo = input("Ingrese un nuevo sub_tipo para el anuncio: ").lower().strip()
	# Validar y asignar el nuevo sub_tipo si es válido
    # if nuevo_sub_tipo not in Video.sub_tipos:
    #     print(nuevo_sub_tipo)
    #     raise SubTipoInvalidoException(f"sub_tipo no válido")

    # if len(campaña.listado_anuncios) > 0 and isinstance(campaña.listado_anuncios[0], Video):
    campaña.listado_anuncios[0].sub_tipo = nuevo_sub_tipo
    # else:


    
    #     raise SubTipoInvalidoException("El anuncio no es de tipo Video.")

    print("Campaña actualizada:")
        # Visualizar los anuncios
    for anuncio in campaña.listado_anuncios:
        print(anuncio)


except (SubTipoInvalidoException, LargoExcedidoException) as e:
    logging.error(str(e))
    print(f"Se produjo un error: {e}.")



# try:
# 	campaña.nombre = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
# except LargoExcedidoException as e:
# 	print(e)

# try:
# 	print(campaña.fecha_inicio)
# except AttributeError as e:
# 	print(e)  # Imprime: El atributo1 es de solo escritura

# try:
# 	print(campaña.fecha_termino)
# except AttributeError as e:
	# print(e)  # Imprime: El atributo1 es de solo escritura

# try:
#     campaña.nombre = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzCampañaj2gjgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
# except LargoExcedidoException as e:
#     logging.error(str(e))
#     print(f"Se produjo un error: {e}.")

# try:
#     print(campaña.fecha_inicio)
# except AttributeError as e:
#     logging.error(str(e))
#     print(f"Se produjo un error: {e}.")

# try:
#     print(campaña.fecha_termino)
# except AttributeError as e:
#     logging.error(str(e))
#     print(f"Se produjo un error: {e}.")