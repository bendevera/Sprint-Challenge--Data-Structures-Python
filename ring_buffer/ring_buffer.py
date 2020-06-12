class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.old_index = 0
        self.storage = []

    def append(self, item):
        if self.size == self.capacity:
            self.storage[self.old_index] = item
            if self.old_index == self.capacity - 1:
                self.old_index = 0
            else:
                self.old_index += 1
        else:
            self.size += 1
            self.storage.append(item)

    def get(self):
        return self.storage