import numpy as np

class Memory:
  def __init__(self,maxn):
    self.maxn = maxn
    self.data = np.zeros(self.maxn)
    self.i = 0
  
  def clear(self):
    self.data = np.zeros(self.maxn)
  
  def add(self,num):
    assert type(num) == float, "Wrong data type, please use float format"
    if self.i + 1 > self.maxn:
      self.clear()
      self.i = 0
    self.data[self.i] = num
    self.i += 1