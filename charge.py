import time
import random
from progress.bar import ChargingBar

def charge_bar(text):
  bar = ChargingBar(text, max=100)
  for num in range(100):
      time.sleep(random.uniform(0, 0.03))
      bar.next()
  bar.finish()