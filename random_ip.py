import random

def randomIP():
  return f'192.168.{random.randrange(255)}.{random.randrange(255)}'
