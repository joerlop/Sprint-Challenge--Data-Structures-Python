class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        # if ring is full, replace oldest slot
        if self.current == self.capacity:
            self.storage[0] = item
            self.current = 1
        # else, add item to current slot
        else:
            self.storage[self.current] = item
            self.current += 1

    def get(self):
        items = []
        for item in self.storage:
            if item:
                items.append(item)

        return items

