from models.Juego import Juego 

class JuegoBomba(Juego):
    
    def __init__(self) -> None:
        super().__init__()


    def fabricJuego(self):
        return JuegoBomba()