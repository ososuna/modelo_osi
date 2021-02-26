import os
os.system('pip install progress')
import sys
import modelo_osi as osi
import modelo_tcp_ip as tcp
import modelo_simplificado as sim

def menu():
  
  while(True):
    print("\nBienvenid@ a la simulación de los modelos OSI, TCP/IP y simplificado")
    print("\nSelecciona el modelo de capas a utilizar")
    print("1 - Modelo OSI")
    print("2 - Modelo TCP/IP")
    print("3 - Modelo Simplificado")
    print("4 - Salir")
    opcion = int(input('Ingresa una opción: '))

    if( 0 < opcion < 4):
      cadena = input('Ingresa una cadena: ')
      if(opcion == 1):
        osi.iniciar(cadena)
      elif(opcion == 2):
        tcp.iniciar(cadena)
      elif(opcion == 3):
        sim.iniciar(cadena)
    else:
      print('\n¡Hasta pronto!\n')
      sys.exit()

