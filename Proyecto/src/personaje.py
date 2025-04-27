class Personaje:

    #creacion de personaje
    def __init__(self, nombre, vida, escudo, fuerza, ataque_sorpresa, modo_test):
        self.nombre=nombre
        self.vida=max(0,vida)
        self.escudo=max(0,escudo)
        self.fuerza=max(0,fuerza)
        self.ataque_sorpresa=max(0,ataque_sorpresa)
        self.muerto=False
        self.modo_test=modo_test #Este parametro sirve para indicar si estoy en modo test, sirve para evitar mostrar los printf por pantalla
        self.__experiencia=0
        self.__nivel=0

    #metodo para que los personajes ataquen
    def atacar(self,enemigo):
        if(enemigo.vida>=70):
            return self.ataque_de_sorpresa(enemigo)
        else:
            return self.ataque_normal(enemigo)
        
    #metodo para un ataque sorpresa
    def ataque_de_sorpresa(self, enemigo):
        danio=(self.ataque_sorpresa)
        if not self.modo_test:#esto sirve para que no se muestren los print en la terminal
            print(f"El personaje {self.nombre} utilizo su ataque sorpresa contra {enemigo.nombre} y este recibio {danio} de daño \n")
        enemigo.recibir_danio(danio)
        self.experiencia_ataque_sorpresa()
        return danio

    #metodo para un ataque normal
    def ataque_normal(self, enemigo):
        danio=self.fuerza
        if not self.modo_test:
            print(f"El personaje {self.nombre} uso un ataque normal contra {enemigo.nombre} y este recibio {danio} de daño \n")
        enemigo.recibir_danio(danio)
        self.experiencia_ataque_fuerza()
        return danio

    #metodo para que los personajes reciban daño
    def recibir_danio(self, danio):
        if(self.escudo>0):
            if(self.escudo>=danio):
                self.escudo-=danio
                if not self.modo_test:
                    print(f"Soy {self.nombre} y he recibido {danio} de daño a mi defensa, mi defensa disminuyo a {self.escudo}\n")
                return self.escudo
            else:
                destruccion_escudo=(danio-self.escudo)
                self.escudo=0
                self.vida-=destruccion_escudo
                if not self.modo_test:
                    print(f"Soy {self.nombre} y perdi mi escudo porque recibi {danio}, mi vida disminuyo a {self.vida}\n")
                return self.vida
        else:
            self.vida-=danio
            if(self.vida<=0):
                self.vida=0
                if not self.modo_test:
                    print(f"Soy {self.nombre} y he recibido {danio} de daño en mi vida, mi vida quedo a {self.vida}\n")
                return self.estoy_vivo()
            else:
                if not self.modo_test:
                    print(f"Soy {self.nombre} y he recibido {danio} de daño en mi vida, mi vida quedo a {self.vida}\n")
                return self.vida

    #metodo para ver en que estado sigue la vida y el escudo de los personajes 
    def mostrar_estado(self):
        return (f"Soy {self.nombre},mi vida es {self.vida}, mi escudo esta a {self.escudo}, mi fuerza es de {self.fuerza}, y mi ataque sorpresa tiene una potencia de {self.ataque_sorpresa}\n")

    #metodo para verificar si el personaje continua con vida
    def estoy_vivo(self):
        if(self.vida<=0):
            self.muerto=True
            return self.morir()
        else:
            self.muerto=False
            return self.mostrar_estado()

    #metodo para mostrar en diseño que personaje perdio
    def morir(self):
        self.muerto=True
        if not self.modo_test:
            print("=========================================\n")
            print("PERSONAJE MUERTO")
            print("    -------Juego Terminado-------")
            print("    --  0                      --")
            print("    --  |/                     --")
            print("    -- /|                /     --")
            print("    -- / \\            -----o   --")
            print("    -- GANADOR         PERDEDOR--")
            print("    -----------------------------")
            print("    -----------Detalle-----------")
            print(f"PERDEDOR----> {self.nombre}")
            print("=========================================\n")

    #metodo para que los personajes sumen experencia dependiendo del ataque
    #metodo experiencia por ataque_sorpresa
    def experiencia_ataque_sorpresa(self):
        self.__experiencia+=self.ataque_sorpresa
        self.nivel_personaje()
        if not self.modo_test:
            print(f"Soy {self.nombre} y mi experiencia aumento a {self.__experiencia} por cada daño de ataque sorpresa")
        return self.__experiencia
    
    #metodo experiencia por ataque de fuerza
    def experiencia_ataque_fuerza(self):
        self.__experiencia+=self.fuerza
        self.nivel_personaje()
        if not self.modo_test:
            print(f"Soy {self.nombre} y mi experiencia aumento a {self.__experiencia} por cada daño de fuerza")
        return self.__experiencia
    #get para mostrar los valores
    def get_experiencia(self):
        return self.__experiencia
    
    #metodo para aumentar el nivel de los personajes
    def nivel_personaje(self):
        while self.__experiencia>=30:
            self.__nivel+=1
            self.__experiencia-=30
            if not self.modo_test:
                print(f"Soy {self.nombre} y mi nivel aumento a {self.__nivel} por cada 30 de experiencia")
    #get para mostrar los valores
    def get_nivel(self):
        return self.__nivel
