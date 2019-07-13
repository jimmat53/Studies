"""A Queue with a capacity limit."""

CAPACITY = 3


class EmptyQueue(Exception):
    """Exception to throw for empty queue."""


class Queue:
    def __init__(self):
        self.capacity = CAPACITY
        self.queue = []

    def isEmpty(self):
        if len(self.queue):
          return False
        else:
          return True

    def enqueue(self, ele):
      if len(self.queue) < self.capacity:
        self.queue.append(ele)
      else:
        del self.queue[0]
        self.queue.append(ele)

    def dequeue(self):
      if self.isEmpty():
        raise EmptyQueue
      else:
		ele = self.queue.pop()
		return ele

if __name__ == "__main__":
  q = Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  q.enqueue(4)
  print q.queue
