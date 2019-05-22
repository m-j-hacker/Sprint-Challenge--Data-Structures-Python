# New strategy: I need to create a flag that permanently marks
# The ring buffer as full when it fills up, this will simplify
# the logic that is required

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  class __Full:
    def append(self, item):
      # Adds an element to the end of the buffer.
      # If the buffer is full, overwrite the oldest data
      self.storage[self.current] = item
      self.current = (self.current + 1) % self.capacity
    def get(self):
      # The list should be returned in the right order, from oldest to newest
      return self.storage
      

  def append(self, item):
    
    self.storage[self.current] = item
    # If the buffer is not full, append the item and then check if the
    # buffer has been filled
    if self.current == self.capacity - 1:
      self.current = 0
      self.__class__ = self.__Full
    else:
      self.current = (self.current + 1) % self.capacity

  def get(self):
    array = []
    for i in range(len(self.storage)):
      if self.storage[i] is None:
        continue
      else:
        array.append(self.storage[i])

    return array
    # array_to_print = []
    # for i in self.storage:
    #   if self.storage[i] != None:
    #     array_to_print[i] = self.storage[i]
    # # if len(self.storage) == self.capacity:
    # #   return self.storage[self.current:]+self.storage[:self.current]
    
    #   return array_to_print
    # else:
    # print_array = []
    # for i in range(0, self.capacity - 1):
    #   if self.storage[i]:
    #     print_array[i] = self.storage[i]
    # return print_array