import bin
import hex
import random_ip as ip
import print_dict as dic
import charge
import time

class Tcp:

  def __init__(self, cadena):
    self.__nombre = 'Modelo TCP/IP'
    self.__desc = 'Modelo que se dio a conocer como TCP/IP debido a sus dos protocolos primarios.'
    self.__arr_aplicacion = []
    self.__arr_transporte = []
    self.__arr_interred = []
    self.__arr_enlace = []
    self.__cadena = cadena
    self.__dic = {}
    self.__dir = 'desc'
    time.sleep(1.5)
    print('\n\t', self.nombre)
    print(self.desc, '\n')
    time.sleep(1.5)
    charge.charge_bar('Iniciando Modelo TCP/IP: ')

  @property
  def nombre(self): 
    return self.__nombre

  @nombre.setter 
  def nombre(self, nombre):
    self.__nombre = nombre

  @property
  def desc(self): 
    return self.__desc

  @desc.setter 
  def desc(self, desc):
    self.__desc = desc

  @property
  def arr_aplicacion(self): 
    return self.__arr_aplicacion

  @arr_aplicacion.setter 
  def arr_aplicacion(self, arr_aplicacion):
    self.__arr_aplicacion = arr_aplicacion

  @property
  def arr_transporte(self): 
    return self.__arr_transporte

  @arr_transporte.setter 
  def arr_transporte(self, arr_transporte):
    self.__arr_transporte = arr_transporte

  @property
  def arr_interred(self): 
    return self.__arr_interred

  @arr_interred.setter 
  def arr_interred(self, arr_interred):
    self.__arr_interred = arr_interred

  @property
  def arr_enlace(self): 
    return self.__arr_enlace

  @arr_enlace.setter 
  def arr_enlace(self, arr_enlace):
    self.__arr_enlace = arr_enlace

  @property
  def cadena(self): 
    return self.__cadena

  @cadena.setter 
  def cadena(self, cadena):
    self.__cadena = cadena
  
  @property
  def dic(self): 
    return self.__dic

  @dic.setter 
  def dic(self, dic):
    self.__dic = dic

  @property
  def dir(self): 
    return self.__dir

  @dir.setter 
  def dir(self, dir):
    self.__dir = dir

  def aplicacion(self):
    if(self.dir == 'desc'):
      time.sleep(1.5)
      print(f'{self.cadena}\n')
      time.sleep(1.5)
      print('\tCapa de Aplicación')
      print('Contiene todos los protocolos de alto nivel.')
      cadena_hex = hex.string_to_hex(self.cadena)
      self.arr_aplicacion = [cadena_hex, 'HTTP']
      self.dic['Aplicación'] = self.arr_aplicacion 
      dic.print_dict(self.dic, 'Aplicación')
      print()
    elif(self.dir == 'asc'):
      time.sleep(1.5)
      print()
      print('\tCapa de Aplicación')
      print('Contiene todos los protocolos de alto nivel.')
      dic.print_dict(self.dic, 'Aplicación')
      print()
      charge.charge_bar('Procesando los datos: ')
      print()
      time.sleep(1.5)
      print(self.cadena)
      print()
  
  def transporte(self):
    if(self.dir == 'desc'):
      time.sleep(1.5)
      print('\tCapa de Transporte')
      print('Está diseñada para que las entidades pares, en los nodos de origen y de destino, lleven a cabo una conversación.')
      self.arr_transporte = ['dict', {'user': 'pinguinodelanasa', 'token': 'C2SD@KJ320DIK2K@30'}]
      self.dic['Transporte'] = self.arr_aplicacion + self.arr_transporte
      dic.print_dict(self.dic, 'Transporte')
      print()
    elif(self.dir == 'asc'):
      time.sleep(1.5)
      print()
      print('\tCapa de Transporte')
      print('Está diseñada para que las entidades pares, en los nodos de origen y de destino, lleven a cabo una conversación.')
      dic.print_dict(self.dic, 'Transporte')
  
  def interred(self):
    if(self.dir == 'desc'):
      time.sleep(1.5)
      print('\tCapa de Interred')
      print('Define un formato de paquete y un protocolo oficial llamado IP.')
      self.arr_interred = [{'IP origen': ip.randomIP(), 'IP destino': ip.randomIP()}]
      self.dic['Interred'] = self.arr_aplicacion + self.arr_transporte + self.arr_interred 
      dic.print_dict(self.dic, 'Interred')
      print()
    elif(self.dir == 'asc'):
      time.sleep(1.5)
      print()
      print('\tCapa de Interred')
      print('Define un formato de paquete y un protocolo oficial llamado IP.')
      dic.print_dict(self.dic, 'Interred')
  
  def enlace(self):
    if(self.dir == 'desc'):
      time.sleep(1.5)
      print('\tCapa de Enlace')
      print('Describe qué enlaces se deben llevar a cabo para cumplir con las necesidades de esta capa.')
      cadena_bin = bin.string_to_bin(self.cadena)
      self.arr_enlace = ['Se han eliminado los errores', cadena_bin]
      self.dic['Enlace'] = self.arr_aplicacion + self.arr_transporte + self.arr_interred + self.arr_enlace
      dic.print_dict(self.dic, 'Enlace')
      print()
      time.sleep(1.5)
      print(''.join(cadena_bin), '\n')
      charge.charge_bar('Enviando los datos: ')
      print()
      self.dir = 'asc'
    elif(self.dir == 'asc'):
      time.sleep(1.5)
      charge.charge_bar('Recibiendo los datos: ')
      time.sleep(1.5)
      print()
      print('\tCapa de Enlace')
      print('Describe qué enlaces se deben llevar a cabo para cumplir con las necesidades de esta capa.')
      dic.print_dict(self.dic, 'Enlace')

def iniciar(cadena):
  print()
  m = Tcp(cadena)
  print()
  m.aplicacion()
  m.transporte()
  m.interred()
  m.enlace()
  m.enlace()
  m.interred()
  m.transporte()
  m.aplicacion()
