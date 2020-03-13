#-*- coding: utf-8 -*-

from autos import Autos

class Estacionamiento:
    def __init__(self):
        """ Inicializa un estacionamiento Vacío """
        self.autos = list()
    
    def Guardar(self,numplaca="",marca="",modelo="",tipo="",hora_ingreso="",estado=""):
        """ Agrega un nuevo elmento al estacionamiento """
        self.autos.append(Autos(numplaca,marca,modelo,tipo,hora_ingreso,estado))
