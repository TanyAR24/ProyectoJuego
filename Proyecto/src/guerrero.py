from personaje import Personaje
class Guerrero(Personaje):
    #creacion del personaje Guerrero que hereda los atributos y metodos de la clase Personaje
    def __init__(self, nombre, vida, escudo, fuerza, ataque_sorpresa, modo_test):
        """Podria definir un valor especifico para todos los guerreros creados. Por ejemplo
        fuerza=50--> ese atributo no pasaria como parametro de la clase base, pero si cuando se inicializa los atributos heredados"""
        super().__init__(nombre, vida, escudo, fuerza, ataque_sorpresa, modo_test)
        self.resistencia=max(0,100) #atributo nuevo, con un valor para todos los guerreros

    #redefinicion del metodo atacar amoldandose al guerrero
    def atacar(self, enemigo):
        if(enemigo.vida>=70):
            if not self.modo_test:#esto sirve para que no se muestren los print en la terminal
                print(f"El guerrero {self.nombre} ataca con su espada que lanza fuego")
            return self.ataque_de_sorpresa(enemigo)
        else:
            if not self.modo_test:#esto sirve para que no se muestren los print en la terminal
                print(f"El guerrero {self.nombre} ataca con su espada normal")
            return self.ataque_normal(enemigo)
        
    #redefinicion del metodo atacar amoldandose al guerrero
    def ataque_de_sorpresa(self, enemigo):
        if(self.resistencia>=20):
            self.resistencia -= 20
            if not self.modo_test:#esto sirve para que no se muestren los print en la terminal
                print(f"Bajo 20 de mi resistencia por el golpe, mi resistencia de 100 bajo a: {self.resistencia}")
            return super().ataque_de_sorpresa(enemigo)#se agrega super() poor que el resto del codigo no cambia, solo agrego un atributo que no lo modifica 
        else:
            self.resistencia=0
            if not self.modo_test:#esto sirve para que no se muestren los print en la terminal
                print(f"mi resistencia se acabo, esta en {self.resistencia}")
    
    #redefinicion del metodo atacar amoldandose al guerrero
    def ataque_normal(self, enemigo):
        if(self.resistencia>=10):
            self.resistencia -= 10
            if not self.modo_test:#esto sirve para que no se muestren los print en la terminal
                print(f"Bajo 10 de mi resistencia por el golpe mi resistencia de 100 bajo a: {self.resistencia}")
            return super().ataque_normal(enemigo)
        else:
            self.resistencia=0
            if not self.modo_test:#esto sirve para que no se muestren los print en la terminal
                print(f"mi resistencia se acabo, esta en {self.resistencia}")
    