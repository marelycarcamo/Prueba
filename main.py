from display import Display
from video import Video


def main():
    
    
    
    # display = Display(12,5,'url_archivo','url_clic','tradicional')
    video = Video(3,6,'url_archivo','url_clic','tradicional')
    video.comprimir_anuncio()
    
    # display.set_ancho()
    # print(display.get_ancho())
    return


if __name__ == "__main__":
    main()