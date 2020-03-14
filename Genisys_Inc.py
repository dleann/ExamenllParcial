# -*- coding: utf-8 -*-
# Programa: Genisys_Inc.py
# Objetivo: Clase que simula el comportamiento de servicio
# de estacionamiento.
# Autor: Dina Guerrero
# Fecha: 13/Marzo/2020

import sys
import platform
import datetime
from datetime import datetime,timedelta
from estacionamiento import Estacionamiento

class Genisys_Inc:
    """ 
    Se encarga de las funcionalidades del servicio de 
    estacionamiento. Toma datos, hace la tarifa y genera un 
    ticket.
    """

    def __init__ (self):
        """ Inicializa el servicio de estacionamiento. """
        self.estacionamiento = Estacionamiento()
        self.opciones= {
            "1":self.ingreso_auto,
            "2":self.salida_auto,
            "3":self.resumen_Ingreso,
            "4":self.resumen_salida,
            "5":self.ganancia,
            "6":self.salir}

    def menu(self):
        """ Despliega el menu principal """
        print("""
            Menu
            OPCIONES: 
                        1.Ingresar Vehiculo
                        2.Salida Vehiculo
                        3.Resumen Vehiculos Ingresados
                        4.Resumen Vehiculos Salida
                        5.Resumen Ganancia
                        6.Salir
                        """)


    def ingreso_auto(self):
        """ Ingreso de datos del auto """
        numero_placa = input("Ingrese Numero de placa del vehiculo: ")
        marca = input("Ingrese marca del vehiculo:")
        modelo = input("Ingrese modelo del vehiculo:")
        tipoVehiculo = input("Ingrese el tipo de Vehiculo: ")
        valorCincoHoras = datetime.now()
        estado = True
        self.estacionamiento.Guardar(numero_placa,marca,modelo,tipoVehiculo,valorCincoHoras,estado)
        print("Nuevo auto ingresado")
        self.press_enter()

    def salida_auto(self):
        """ Muestra ticket de salida """

    
    def resumen_Ingreso(self):
        """ Resumen de las horas """

    def conteo_autos(self):
        """ Cuenta y muestra el numero de mensajes """
        print("----Bandeja---- ")
        if self.estacionamiento.count() > 0:
            print("Tiene auto")
        else:
            print("No hay ningun ingreso")
        self.press_enter()    

    def resumen_salida(self, estacionamiento=None):
        """ Resumen de salida """
        if not estacionamiento:
            estacionamiento = self.estacionamiento.Guardar
        self.conteo_autos()
        for Estacionamiento in estacionamiento:
            print("""
                    Placa: {0}
                    Marca: {1}
                    Modelo: {2}
                    Tipo Vehiculo: {3}
                    Hora Ingreso: {4}
                    Estado: {5}

                  """.format(estacionamiento.numero_placa,estacionamiento.marca,estacionamiento.modelo,
                              estacionamiento.tipoVehiculo,estacionamiento.valorCincoHoras,estacionamiento.estado == True))
        self.press_enter()

    def ganancia(self):
        """ Ganancias del servicio de estacionamiento """
    
    def run(self):
        """Ejecuta el programa en un ciclo"""
        while True:
            self.menu()
            seleccion = input("Elija Una Opción: ")
            accion = self.opciones.get(seleccion)

            if accion:
                accion()
            else:
                print("Opcion invalida")


    def press_enter(self):
        """ Realiza una pausa y solicita presionar una tecla """
        input("\nPresiones enter para continuar")

    
    def salir(self):
        """ Cierra la aplicación """
        print("Gracias por ingresar")
        sys.exit(0)

if __name__ == "__main__":
    Menu = Genisys_Inc()
    Menu.run()




    

