import unittest
from src.personaje import Personaje

class TestPersonaje(unittest.TestCase):

    def setUp(self):
        """configuracion inicial para las pruebas"""
        self.p1 = Personaje("Jule la destructora", 43, 21, 50, 19)
        self.p2 = Personaje("Paco el mago", 10, 20, 35, 16)

    def test_atacar(self):
        print("\n===============================================")
        """verifica que el personaje ataque bien"""
        defensa_inicial = self.p2.defensa
        self.p1.atacar(self.p2)
        self.assertLessEqual(self.p2.defensa, defensa_inicial, "La defensa del enemigo no disminuyo correctamente")
        
    def test_recibir_daño(self):
        print("\n===============================================")
        """verifica que el personaje reciba bien el daño"""
        vida_inicial = self.p2.vida
        self.p2.recibir_daño(10)
        self.assertLessEqual(self.p2.vida, vida_inicial, "La vida del personaje no disminuyo correctamente")

    def test_mostrar_estado(self):
        print("\n===============================================")
        """verifica que el estado del personaje se muestre bien"""
        try:
            self.p1.mostrar_estado()
            self.p2.mostrar_estado()
        except Exception as e:
            self.fail(f"mostrar_estado() fallo con error: {e}")

    def test_estoy_vivo(self):
        print("\n===============================================")
        """verifica que el personaje detecte si sigue vivo o no"""
        self.assertTrue(self.p1.estoy_vivo(), "El personaje deberia estar vivo al inicio")
        self.p2.vida = 0
        self.assertFalse(self.p2.estoy_vivo(), "El personaje deberia estar muerto cuando la vida es 0")#para verificar el error solo cambiar a assertFalse

    def test_morir(self):
        print("\n===============================================")
        """confirma que uno de los dos personajes esta muerto"""
        self.p1.vida = 0
        self.p1.morir()
        self.assertTrue(self.p1.muerto, "El personaje no murio correctamente") #para verificar el error solo cambiar a assertFalse