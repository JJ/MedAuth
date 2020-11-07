from .testUsuarioCliente import TestUsuarioCliente
from typing import List
import datetime


class TestPoliza:
    def __init__(self, usuario: TestUsuarioCliente, id_poliza: str, periodo_carencia: datetime, tipo: str, 
    			copagos: float, mensualidad: str, servicios_excluidos: List[str], modulos_extra: List[str]):
        self.__titular = usuario
        self.__id_poliza = id_poliza
        self.__periodo_carencia = periodo_carencia
        self.__tipo = tipo
        self.__copagos = copagos
        self.__mensualidad = mensualidad
        self.__servicios_excluidos = servicios_excluidos[:]
        self.__modulos_extra = modulos_extra[:]

    def get_titular(self):
    	return self.__titular
    
    def get_id_poliza(self):
    	return self.__id_poliza
    
    def set_id_poliza(self, id_poliza):
    	self.__id_poliza = id_poliza

    def get_periodo_carencia(self):
    	return self.__periodo_carencia
    
    def set_periodo_carencia(self, periodo_carencia):
    	self.__periodo_carencia == periodo_carencia

    def get_tipo(self):
    	return self.__tipo

    def set_tipo(self, tipo):
    	self.__tipo = tipo

    def get_copagos(self):
    	return self.__copagos

    def set_copagos(self, copagos):
    	self.__copagos = copagos

    def get_mensualidad(self):
    	return self.__mensualidad

    def set_mensualidad(self, mensualidad):
    	self.__mensualidad = mensualidad

    def get_servicios_excluidos(self):
    	return self.__servicios_excluidos

    def set_servicios_excluidos(self, servicios_excluidos):
    	self.__servicios_excluidos = servicios_excluidos[:]
    
    def get_modulos_extra(self):
    	return self.__modulos_extra

    def set_modulos_extra(self, modulos_extra):
    	self.__modulos_extra = modulos_extra[:]
    
    def __eq__(self, otra):
    	assert self.__titular == otra.get_titular()
    	assert self.__id_poliza == otra.get_id_poliza()
    	assert self.__periodo_carencia == otra.get_periodo_carencia()
    	assert self.__tipo == otra.get_tipo()
    	assert self.__copagos == otra.get_copagos()
    	assert self.__mensualidad == otra.get_mensualidad()
    	assert self.__servicios_excluidos == otra.get_servicios_excluidos()
    	assert self.__modulos_extra == otra.get_modulos_extra()
    	
    	return (self.__titular == otra.get_titular()) and (self.__id_poliza == otra.get_id_poliza()) and (self.__periodo_carencia == otra.get_periodo_carencia()) and (self.__tipo == otra.get_tipo()) and (self.__copagos == otra.get_copagos()) and (self.__mensualidad == otra.get_mensualidad()) and (self.__servicios_excluidos == otra.get_servicios_excluidos() and (self.__modulos_extra == otra.get_modulos_extra()))

def test_compare_poliza():
	u = TestUsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678", "12345678")
	u2 = TestUsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678", "12345678")
	fecha = datetime.datetime(2020, 5, 17)
	fecha2 = datetime.datetime(2020, 5, 18)
	
	t1 = TestPoliza(u, "12345678", fecha, "Total", 35.99, 103.0, ["TAC", "Apendicitis"], ["Dental"])
	t2 = TestPoliza(u2, "12345678", fecha, "Total", 35.99, 103.0, ["TAC", "Apendicitis"], ["Dental"])
	t3 = TestPoliza(u2, "12345678", fecha2, "Básico", 35.99, 103.0, ["TAC", "Apendicitis"], ["Dental"])
	assert t1 == t1 # Pasa test
	assert t1 == t2 # Pasa test
	assert t2 == t3 # No pasa test
