from personaje import Personaje
class Mago(Personaje):
    #creacion del personaje Mago que hereda los atributos y metodos de la clase Personaje
    def __init__(self, nombre, vida, escudo, fuerza, ataque_sorpresa, modo_test):
        super().__init__(nombre, vida, escudo, fuerza, ataque_sorpresa, modo_test)
        self.mana=max(0,15)#un poder que suma en ataque

    #redefinicion del metodo atacar amoldandose al mago
    def atacar(self, enemigo):
        if(enemigo.vida>=70):
            if not self.modo_test:#esto sirve para que no se muestren los print en la terminal
                print(f"El mago {self.nombre} ataca con su posima toxica")
            return self.ataque_de_sorpresa(enemigo)
        else:
            if not self.modo_test:#esto sirve para que no se muestren los print en la terminal
                print(f"El mago {self.nombre} ataca con sus poderes magicos")
            return self.ataque_normal(enemigo)

    
    #redefinicion del metodo atacaque_de_sorpresa amoldandose al mago
    def ataque_de_sorpresa(self, enemigo):
        danio=self.ataque_sorpresa + self.mana
        enemigo.recibir_danio(danio)
        self.experiencia_ataque_sorpresa()
        return danio
        """return super().ataque_de_sorpresa(enemigo)--> aca no va super() porque cambia el calculo del daño"""
    
    #redefinicion del metodo atacaque_normal amoldandose al mago
    def ataque_normal(self, enemigo):
        danio=self.fuerza + self.mana
        enemigo.recibir_danio(danio)
        self.experiencia_ataque_fuerza()
        return danio