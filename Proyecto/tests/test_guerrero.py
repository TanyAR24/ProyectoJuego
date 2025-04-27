import unittest
from src.guerrero import Guerrero

class TestGuerrero(unittest.TestCase):
    def setUp(self):
        self.guerrero=Guerrero("Pascal", 100,100,32,42,modo_test=True)
    
    #testeo de los metodos ATAQUES para verificar que la resistencia sea correcta
    def test_ataque_de_sorpresa(self):
        atacante=Guerrero("Paco", 100, 100,21,16,modo_test=True)
        enemigo=Guerrero("pedritoh", 100,100,32,42,modo_test=True)
        atacante.ataque_de_sorpresa(enemigo)
        self.assertEqual(atacante.resistencia, 80)

    def test_ataque_normal(self):
        atacante=Guerrero("Paco", 100, 100,21,16,modo_test=True)
        enemigo=Guerrero("pedritoh", 100,100,32,42,modo_test=True)
        atacante.ataque_normal(enemigo)
        self.assertEqual(atacante.resistencia, 90)
    
    #test para verificar que resistencia no sea negativa
    def test_ataque_de_sorpresa_resistencia(self):
        atacante=Guerrero("Paco", 100, 100,21,16,modo_test=True)
        enemigo=Guerrero("pedritoh", 100,100,32,42,modo_test=True)
        for _ in range(6):
            """For para repetir seis veces lo que este dentro"""
            atacante.ataque_de_sorpresa(enemigo)
        self.assertEqual(atacante.resistencia, 0)

    def test_ataque_normal_resistencia(self):
        atacante=Guerrero("Paco", 100, 100,21,16,modo_test=True)
        enemigo=Guerrero("pedritoh", 100,100,32,42,modo_test=True)
        for _ in range(11):
            atacante.ataque_normal(enemigo)
        self.assertEqual(atacante.resistencia, 0)