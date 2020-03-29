import unittest
from Maquina import *


class TestMaquina(unittest.TestCase):
    """"Testes """
    def test_calcular_notas(self):
        """Testar o numero de notas devolvida pela Maquina"""
        # validas2=[" 1,00", "R$ 2,00","R$ 5,00","R$ 10,00","R$ 20,00","R$ 50,00"]        
        #qtd_notas=[20,10,30,40,10,10]
        troco=90
        a=[0,0,0,0,2,1] 
        v=calcular_notas(troco)
        self.assertEqual(a,v)
        
    def test_calcular_notas2(self):
        troco=30
        b=[0,0,0,1,1,0]
        v2=calcular_notas(troco)        
        self.assertEqual(b,v2)


    def test_troco_valido(self):
        qtd=[1,2,3,4,5,1]
        qtd_dispo=[100,50,40,30,10,5]
        self.assertTrue(troco_valido(qtd,qtd_dispo))

    def test_troco_valido2(self):
        qtd=[1,0,3,4,5,0]
        qtd_dispo=[100,50,40,30,10,5]
        self.assertTrue(troco_valido(qtd,qtd_dispo))

    def test_troco_valido3(self):
        qtd=[1,10,3,4,5,0]
        qtd_dispo=[0,0,40,30,10,5]
        self.assertFalse(troco_valido(qtd,qtd_dispo))

unittest.main()

