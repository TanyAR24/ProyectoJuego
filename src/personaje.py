class Personaje:
    #funcion para inicializar un nuevo personaje
    def __init__(self, nombre, vida, fuerza, defensa,ataque_sorpresa):
        self.nombre=nombre
        self.vida=vida
        self.fuerza=fuerza
        self.defensa=defensa
        self.ataque_sorpresa=ataque_sorpresa
        self.muerto= False
    
    #funcion para realizar un ataque sobre otro personaje
    """si la fuerza del personaje que ataca es mayor o igual a 20 se aplica un ataque sorpresa
    si no lo es solo se reduce la defensa del enemigo"""
    def atacar(self, enemigo):
        daño=(self.fuerza)
        if (self.fuerza>= 20):
            daño+=self.ataque_sorpresa
            print(f"{self.nombre} ataca a {enemigo.nombre} el daño es de {daño}")
            enemigo.recibir_daño(daño)
            return daño
        else:
            enemigo.defensa-=self.fuerza
            enemigo.recibir_daño(daño)

    #funcion para verificar que el personaje recibe daño
    """el personaje recibe daño, primero se reduce la defensa, cuando ya no queda defensa se reduce la vida"""
    def recibir_daño(self,daño):
        if self.defensa>0:
            if self.defensa>=daño:
               self.defensa-=daño
               return print(f"{self.nombre} bloqueo el ataque, la defensa disminuyo a:{self.defensa}")
            else:
                daño_restante=daño-self.defensa
                self.defensa=0
                self.vida-=daño_restante
                return print(f"{self.nombre} perdio su defensa, recibio {daño_restante} de daño, la vida disminuyo a:{self.vida}")
        else:
            self.vida-=daño
            print(f"{self.nombre} no tiene defensas, recibio {daño} de daño y su vida disminuyo a {self.vida}")
        if self.vida<=0:
            self.muerto=True

    #muestra los datos de los personajes
    """muestra su nombre, vida y defensa actual al momento de llamarlo, luego se llama a la funcion estoy_vivo() para verificar si sigue vivo"""
    def mostrar_estado(self):
        print(f"Mi nombre es {self.nombre}, mi vida actual es {self.vida}, y mi defensa esta a {self.defensa}")
        return self.estoy_vivo()

    #verifica si el personaje sigue con vida
    """si la vida es mayor que cero el personaje esta vivo, de lo contrario esta muerto"""
    def estoy_vivo(self):
        if self.vida>0:
            print(f"Vida que me queda: {self.vida}")
            return True
        else:
            print(f"Mi vida esta en: {self.vida}")
            self.muerto=True
            print(f"*UN MINUTO DE SILENCIO POR* {self.nombre}")
            return False

    #define al personaje que muerio e imprime un mensaje de juego terminado
    """muestra un diseño de la muerte de un personaje y el nombre del personaje muerto"""
    def morir(self):
        self.muerto=True
        print("PERSONAJE MUERTO")
        print("    -------Juego Terminado-------")
        print("    --  0                      --")
        print("    --  |/                     --")
        print("    -- /|                /     --")
        print("    -- / \            -----o   --")
        print("    -- GANADOR         PERDEDOR--")
        print("    -----------------------------")
        print("    -----------Detalle-----------")
        return print(f"PERDEDOR----> {self.nombre}")
