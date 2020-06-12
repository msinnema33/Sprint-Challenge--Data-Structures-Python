# a circular buffer of defined size
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # define capacity
        self.current = 0  # current_node
        self.storage = [None] * capacity # ^ holds a space in list based on its capacity

    def append(self, item):
        self.storage[self.current] = item  # set item passed in to storage's current node
        self.current += 1  # increase current by one
        # if the capacity is full
        if self.current >= self.capacity:
           self.current = 0   # reset current to 0

    def get(self):
        # return all elements in storage that aren't None
        return [x for x in self.storage if x != None]