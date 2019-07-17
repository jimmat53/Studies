'''Double-ended queue'''

CAPACITY = 3

class EmptyDeQueue(Exception):
  """Exception to throw for empty dequeue."""


class DeQueue:
  def __init__(self):
    self.dequeue = []
  
  def isEmpty(self):
    if len(self.dequeue):
      return False
    else:
      return True

  def insertFront(self, ele):
    if len(self.dequeue) == CAPACITY:
      self.dequeue.pop()
    self.dequeue.insert(0, ele)
    

  def insertLast(self, ele):
    if len(self.dequeue) == CAPACITY:
      del self.dequeue[0]
    self.dequeue.append(ele)

  def deleteFront(self):
    if len(self.dequeue) == 0:
      raise EmptyDeQueue
    del self.dequeue[0]

  def deleteLast(self):
    if len(self.dequeue) == 0:
      raise EmptyDeQueue
    self.dequeue.pop()

  def __repr__(self):
    return 'Dequeue: ' + str(self.dequeue)


if __name__ == "__main__":
  dq = DeQueue()
  dq.insertFront(1)
  print dq

