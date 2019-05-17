class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # Adds an element to the end of a buffer.
    # If the buffer is full, overwrite the oldest data
    if len(self.storage) == self.capacity:
      self.storage[self.current] = item
      self.current = (self.current + 1) % self.capacity
    # If the buffer is not full, append the item and then check if the
    # buffer has been filled
    else:
      self.storage.append(item)
      if len(self.storage) == self.capacity:
        self.current = 0

  def get(self):
    if len(self.storage) == self.capacity:
      return self.storage[self.current:]+self.storage[:self.current]
    else:
      return self.storage