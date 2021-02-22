import bin
import random_ip as ip
import print_dict as dic
import charge
import time

class Osi:

  def __init__(self, cadena):
    self.__nombre = 'Modelo OSI'
    self.__desc = 'Modelo de referencia para los protocolos de comunicación de las redes informáticas creado por ISO.'
    self.__arr_aplicacion = []
    self.__arr_presentacion = []
    self.__arr_sesion = []
    self.__arr_transporte = []
    self.__arr_red = []
    self.__arr_enlace = []
    self.__arr_fisica = []
    self.__cadena = cadena
    self.__dic = {}
    self.__dir = 'desc'
    time.sleep(1.5)
    print('\n\t', self.nombre)
    print(self.desc, '\n')
    time.sleep(1.5)
    charge.charge_bar('Iniciando Modelo OSI: ')

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
  def arr_presentacion(self): 
    return self.__arr_presentacion

  @arr_presentacion.setter 
  def arr_presentacion(self, arr_presentacion):
    self.__arr_presentacion = arr_presentacion

  @property
  def arr_sesion(self): 
    return self.__arr_sesion

  @arr_sesion.setter 
  def arr_sesion(self, arr_sesion):
    self.__arr_sesion = arr_sesion

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
  def arr_enlace(self): 
    return self.__arr_enlace

  @arr_enlace.setter 
  def arr_enlace(self, arr_enlace):
    self.__arr_enlace = arr_enlace

  @property
  def arr_fisica(self): 
    return self.__arr_fisica

  @arr_fisica.setter 
  def arr_fisica(self, arr_fisica):
    self.__arr_fisica = arr_fisica

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
      print('Contiene una variedad de protocolos que los usuarios utilizan con frecuencia.')
      self.arr_aplicacion = [self.cadena, 'HTTP']
      self.dic['Aplicación'] = self.arr_aplicacion 
      dic.print_dict(self.dic, 'Aplicación')
      print()
    elif(self.dir == 'asc'):
      time.sleep(1.5)
      print()
      print('\tCapa de Aplicación')
      print('Contiene una variedad de protocolos que los usuarios utilizan con frecuencia.')
      dic.print_dict(self.dic, 'Aplicación')
      print()
      charge.charge_bar('Procesando los datos: ')
      print()
      time.sleep(1.5)
      print(self.cadena)
      print()

  def presentacion(self):
    if(self.dir == 'desc'):
      time.sleep(1.5)
      print('\tCapa de Presentación')
      print('Se definen las estucturas de datos.')
      self.arr_presentacion = ['dict']
      self.dic['Presentación'] = self.arr_aplicacion + self.arr_presentacion
      dic.print_dict(self.dic, 'Presentación')
      print()
    elif(self.dir == 'asc'):
      time.sleep(1.5)
      print()
      print('\tCapa de Presentación')
      print('Se definen las estucturas de datos.')
      dic.print_dict(self.dic, 'Presentación')
  
  def sesion(self):
    if(self.dir == 'desc'):
      time.sleep(1.5)
      print('\tCapa de Sesión')
      print('Permite a los usuarios en distintas máquinas establecer sesiones entre ellos.')
      self.arr_sesion = [{'user': 'pinguinodelanasa', 'token': 'C2SD@KJ320DIK2K@30'}]
      self.dic['Sesión'] = self.arr_aplicacion + self.arr_presentacion + self.arr_sesion 
      dic.print_dict(self.dic, 'Sesión')
      print()
    elif(self.dir == 'asc'):
      time.sleep(1.5)
      print()
      print('\tCapa de Sesión')
      print('Permite a los usuarios en distintas máquinas establecer sesiones entre ellos.')
      dic.print_dict(self.dic, 'Sesión')
  
  def transporte(self):
    if(self.dir == 'desc'):
      time.sleep(1.5)
      print('\tCapa de Transporte')
      print('Su función es dividir los datos en unidades más pequeñas si es necesario.')
      self.arr_transporte = []
      self.dic['Transporte'] = self.arr_aplicacion + self.arr_presentacion + self.arr_sesion
      dic.print_dict(self.dic, 'Transporte')
      print()
    elif(self.dir == 'asc'):
      time.sleep(1.5)
      print()
      print('\tCapa de Transporte')
      print('Su función es dividir los datos en unidades más pequeñas si es necesario.')
      dic.print_dict(self.dic, 'Transporte')
  
  def red(self):
    if(self.dir == 'desc'):
      time.sleep(1.5)
      print('\tCapa de Red')
      print('Encamina los paquetes desde el origen hasta el destino.')
      self.arr_red = [{'IP origen': ip.randomIP(), 'IP destino': ip.randomIP()}]
      self.dic['Red'] = self.arr_aplicacion + self.arr_presentacion + self.arr_sesion + self.arr_red 
      dic.print_dict(self.dic, 'Red')
      print()
    elif(self.dir == 'asc'):
      time.sleep(1.5)
      print()
      print('\tCapa de Red')
      print('Encamina los paquetes desde el origen hasta el destino.')
      dic.print_dict(self.dic, 'Red')
  
  def enlace(self):
    if(self.dir == 'desc'):
      time.sleep(1.5)
      print('\tCapa de Enlace')
      print('Transforma un medio de transmisión puro en una linea que esté libre de errores de transmisión.')
      self.arr_enlace = ['Se han eliminado los errores']
      self.dic['Enlace'] = self.arr_aplicacion + self.arr_presentacion + self.arr_sesion + self.arr_red + self.arr_enlace
      dic.print_dict(self.dic, 'Enlace')
      print()
    elif(self.dir == 'asc'):
      time.sleep(1.5)
      print()
      print('\tCapa de Enlace')
      print('Transforma un medio de transmisión puro en una linea que esté libre de errores de transmisión.')
      dic.print_dict(self.dic, 'Enlace')
  
  def fisica(self):
    if(self.dir == 'desc'):
      time.sleep(1.5)
      print('\tCapa Física')
      print('Se relaciona con la transmisión de bits puros.')
      cadena_bin = bin.string_to_bin(self.cadena)
      self.arr_fisica = [cadena_bin]
      self.dic['Física'] = self.arr_aplicacion + self.arr_presentacion + self.arr_sesion + self.arr_red + self.arr_fisica 
      dic.print_dict(self.dic, 'Física')
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
      print('\tCapa Física')
      print('Se relaciona con la transmisión de bits puros.')
      dic.print_dict(self.dic, 'Física')

def iniciar(cadena):
  print()
  m = Osi(cadena)
  print()
  m.aplicacion()
  m.presentacion()
  m.sesion()
  m.transporte()
  m.red()
  m.enlace()
  m.fisica()
  m.fisica()
  m.enlace()
  m.red()
  m.transporte()
  m.sesion()
  m.presentacion()
  m.aplicacion()
