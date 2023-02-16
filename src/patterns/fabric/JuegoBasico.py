from models.Juego import Juego 

class JuegoBasico(Juego):
    
    def __init__(self) -> None:
        super().__init__()

    def fabricJuego(self):
        return JuegoBasico()
