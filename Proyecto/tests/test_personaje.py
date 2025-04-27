import unittest
from src.personaje import Personaje

class TestPersonaje(unittest.TestCase):
    def setUp(self):
       """Creacion de personaje para pruebas"""
       self.p1=Personaje("Paco",100,100,21,16, modo_test=True)
       self.p2=Personaje("Pepo",89,100,25,10,modo_test=True)

    #TESTS METODO ATACAR
    #si vida del enemigo es >=70
    def test_atacar_usando_ataque_sorpresa(self):
        atacante=Personaje("Paco", 100, 100, 21, 16,modo_test=True)
        enemigo=Personaje("Jule", 70,40,25,10,modo_test=True)
        danio=atacante.atacar(enemigo)
        self.assertEqual(danio,16)#verifica que sea daño de ataque sorpresa
    #si vida del enemigo es <70
    def test_atacar_usando_ataque_normal(self):
        atacante=Personaje("Paco", 100, 100,21,16,modo_test=True)
        enemigo=Personaje("Jule", 43,0,25,10,modo_test=True)
        danio=atacante.atacar(enemigo)
        self.assertEqual(danio,21)#verifica que sea daño normal

    #TEST METODO ATAQUE_SORPRESA
    def test_ataque_de_sorpresa(self):
        atacante=Personaje("Paco", 100, 0, 21, 16,modo_test=True)
        enemigo=Personaje("Jule", 70,0,25,10,modo_test=True)
        atacante.ataque_de_sorpresa(enemigo)#enemigo debio recibir 16 de ataque sorpresa y se le debio resta en vida
        self.assertEqual(enemigo.vida,54)

    #TEST METODO ATAQUE_NORMAL
    def test_ataque_normal(self):
        atacante=Personaje("Paco", 100, 0,21,16,modo_test=True)
        enemigo=Personaje("Jule", 43,0,25,10,modo_test=True)
        atacante.ataque_normal(enemigo)
        self.assertEqual(enemigo.vida, 22)
    
    #TESTS VALOR NEGATIVO
    #test vida negativa
    def test_vida_negativa(self):
        personaje=Personaje("Paco", -10, 0,21,16,modo_test=True)
        personaje.recibir_danio(10)
        self.assertEqual(personaje.vida,0)

    #test escudo negativo
    def test_escudo_negativo(self):
        personaje=Personaje("Paco", 100, -20,21,16,modo_test=True)
        personaje.recibir_danio(20)
        self.assertEqual(personaje.escudo,0)

    #TESTS DEL METODO RECIBIR_DANIO
    #test si hay escudo
    def test_recibir_danio_escudo_mayor_al_danio(self):
        personaje=Personaje("Jule", 43,30,25,0,modo_test=True)
        personaje.recibir_danio(21)
        self.assertEqual(personaje.vida,43)
        self.assertEqual(personaje.escudo,9)

    #test si el escudo es menor al daño
    def test_recibir_danio_escudo_menor_al_danio(self):
        personaje=Personaje("Jule", 43,10,25,0,modo_test=True)
        personaje.recibir_danio(21)
        self.assertEqual(personaje.vida,32)
        self.assertEqual(personaje.escudo,0)

    #test si no hay escudo
    def test_recibir_danio_sin_escudo(self):
        personaje=Personaje("Jule", 43,0,25,0,modo_test=True)
        personaje.recibir_danio(21)
        self.assertEqual(personaje.vida,22)
        self.assertEqual(personaje.escudo,0)

    #test si no hay escudo y la vida es menor al daño
    def test_recibir_danio_sin_escudo_y_vida_menor_al_danio(self):
        personaje=Personaje("Jule", 12,0,25,0,modo_test=True)
        personaje.recibir_danio(21)
        self.assertEqual(personaje.vida, 0)
        self.assertEqual(personaje.escudo,0)
        self.assertTrue(personaje.muerto)

    #TEST METODO MOSTRAR_ESTADO
    def test_mostrar_estado(self):
        personaje=Personaje("Paco", 100, 0,21,0,modo_test=True)
        estado=personaje.mostrar_estado()
        self.assertIn("Soy Paco", estado)
        self.assertIn("mi vida es 100", estado)
        self.assertIn("mi escudo esta a 0",estado)
        self.assertIn("mi fuerza es de 21", estado)
        self.assertIn("mi ataque sorpresa tiene una potencia de 0", estado)

    #TEST METODO ESTOY_VIVO
    #si vida <=0 esta muerto
    def test_estoy_vivo_vida_menor_igual_a_cero(self):
        personaje=Personaje("Jule", 0,0,25,0,modo_test=True)
        personaje.estoy_vivo()
        self.assertTrue(personaje.muerto)
        
    #si vida es >0 esta vivo
    def test_estoy_vivo_vida_mayor_a_cero(self):
        personaje=Personaje("Jule", 12,0,25,0,modo_test=True)
        personaje.estoy_vivo()
        self.assertFalse(personaje.muerto)

    #TEST METODO MORIR
    def test_morir(self):
        personaje=Personaje("Jule", 0,0,25,0,modo_test=True)
        personaje.morir()
        self.assertTrue(personaje.muerto)

    #TEST METODO EXPERIENCIA
    def test_experiencia_ataque_sorpresa(self):
        atacante=Personaje("Paco", 100, 100, 21, 16,modo_test=True)
        enemigo=Personaje("Jule", 70,40,25,10,modo_test=True)
        atacante.ataque_de_sorpresa(enemigo)#+16 de experiencia
        atacante.ataque_de_sorpresa(enemigo)#+16 de experiencia
        #hasta aca hay 31 de experiencia--> nivel 1, experiencia restante 2
        self.assertEqual(atacante.get_nivel(),1)
        self.assertEqual(atacante.get_experiencia(),2)

    def test_experiencia_ataque_fuerza(self):
        atacante=Personaje("Paco", 14, 100, 21, 16,modo_test=True)
        enemigo=Personaje("Jule", 70,40,25,10,modo_test=True)
        atacante.ataque_normal(enemigo)#+21 de experiencia
        atacante.ataque_normal(enemigo)#21 de experiencia
        atacante.ataque_normal(enemigo)#+21 de experiencia
        #hasta aca hay 63 de experiencia--> nivel 2, experiencia restante 3
        self.assertEqual(atacante.get_nivel(),2)
        self.assertEqual(atacante.get_experiencia(), 3)

    #TEST METODO NIVEL
    def test_nivel_personaje(self):
        personaje=Personaje("Jule", 30,0,25,30,modo_test=True)
        personaje._Personaje__experiencia=35#accediendo al atributo privado, esta bien si es en test(permite modificar los atributos sin acceder directamente a ellos)
        personaje.nivel_personaje()#deberia subir el nivel a 1
        self.assertEqual(personaje.get_nivel(),1)
        self.assertEqual(personaje.get_experiencia(),5)
