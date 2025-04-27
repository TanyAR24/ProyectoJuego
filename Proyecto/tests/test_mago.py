import unittest
from src.mago import Mago

class TestMago(unittest.TestCase):
    def setUp(self):
        self.mago=Mago("prissma", 100,100,32,42,modo_test=True)
    
    #testeo de los metodos ATAQUES
    #ataque sorpresa disminuye el escudo
    def test_ataque_de_sorpresa_afecta_el_escudo(self):
        atacante=Mago("Paco", 100, 100,21,16,modo_test=True)
        enemigo=Mago("Jule", 100,100,25,10,modo_test=True)
        mana=atacante.mana
        danio=mana + atacante.ataque_sorpresa
        atacante.ataque_de_sorpresa(enemigo)
        self.assertEqual(danio,31)
        self.assertEqual(enemigo.escudo, 69)

    #ataque sorpresa disminuye la vida
    def test_ataque_de_sorpresa_afecta_la_vida(self):
        atacante=Mago("Paco", 100, 100,21,16,modo_test=True)
        enemigo=Mago("Jule", 50,0,25,10,modo_test=True)
        mana=atacante.mana
        danio=mana + atacante.ataque_sorpresa
        atacante.ataque_de_sorpresa(enemigo)
        self.assertEqual(danio,31)
        self.assertEqual(enemigo.vida, 19)

    #ataque normal disminuye el escudo
    def test_ataque_normal_afecta_el_escudo(self):
        atacante=Mago("Paco", 100, 100,21,16,modo_test=True)
        enemigo=Mago("Jule", 100,100,25,10,modo_test=True)
        mana=atacante.mana
        danio=mana + atacante.fuerza
        atacante.ataque_normal(enemigo)
        self.assertEqual(danio,36)
        self.assertEqual(enemigo.escudo, 64)

    #ataque normal disminuye la vida
    def test_ataque_normal_afecta_la_vida(self):
        atacante=Mago("Paco", 100, 100,21,16,modo_test=True)
        enemigo=Mago("Jule", 50,0,25,10,modo_test=True)
        mana=atacante.mana
        danio=mana + atacante.fuerza
        atacante.ataque_normal(enemigo)
        self.assertEqual(danio,36)
        self.assertEqual(enemigo.vida, 14)
