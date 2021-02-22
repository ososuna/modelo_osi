import bin
import random_ip as ip
import print_dict as dic
import charge
import time

class Sim:

  def __init__(self, cadena):
    self.__nombre = 'Modelo Simplificado'
    self.__desc = 'Modelo simplificado de tres capas basando en OSI y TCP/IP.'
    self.__arr_aplicacion = []
    self.__arr_transporte = []
    self.__arr_red = []
    self.__cadena = cadena
    self.__dic = {}
    self.__dir = 'desc'
    time.sleep(1.5)
    print('\n\t', self.nombre)
    print(self.desc, '\n')
    time.sleep(1.5)
    charge.charge_bar('Iniciando Modelo Simplificado: ')

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
  def arr_red(self): 
    return self.__arr_red

  @arr_red.setter 
  def arr_red(self, arr_red):
    self.__arr_red = arr_red

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
      print('\tCapa de Aplicación')
      print('Contiene todos los protocolos de alto nivel.')
      self.arr_aplicacion = [self.cadena, 'HTTP']
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
  
  def red(self):
    if(self.dir == 'desc'):
      time.sleep(1.5)
      print('\tCapa de Red')
      print('Define un formato de paquete y un protocolo oficial llamado IP.')
      cadena_bin = bin.string_to_bin(self.cadena)
      self.arr_red = [{'IP origen': ip.randomIP(), 'IP destino': ip.randomIP()}, 'Se han eliminado los errores', cadena_bin]
      self.dic['Red'] = self.arr_aplicacion + self.arr_transporte + self.arr_red 
      dic.print_dict(self.dic, 'Red')
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
      print('\tCapa de Red')
      print('Define un formato de paquete y un protocolo oficial llamado IP.')
      dic.print_dict(self.dic, 'Red')
    
def iniciar(cadena):
  print()
  m = Sim(cadena)
  print()
  m.aplicacion()
  m.transporte()
  m.red()
  m.red()
  m.transporte()
  m.aplicacion()