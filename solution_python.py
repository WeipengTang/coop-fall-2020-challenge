class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0        
        self.histroy = []
        self.currentIndex = -1

    def add(self, num: int):
        self.value += num
        self.histroy.append(num)
        self.update_index(1)

    def subtract(self, num: int):
        self.value -= num
        self.histroy.append(-1*num)
        self.update_index(1)

    def undo(self):
        if self.currentIndex > -1:
            self.value -= self.histroy[self.currentIndex]
            self.update_index(-1)

    def redo(self):
        if self.currentIndex < (len(self.histroy) - 1):
            self.value += self.histroy[self.currentIndex + 1]
            self.update_index(1)

    def bulk_undo(self, steps: int):
        start_index = self.currentIndex - steps
        while self.currentIndex != start_index and self.currentIndex > -1:
            self.undo()

    def bulk_redo(self, steps: int):
        end_index = self.currentIndex + steps
        while self.currentIndex != end_index and self.currentIndex < len(self.histroy):
            self.redo()

    def update_index(self, steps: int):
        self.currentIndex += steps


# if __name__ == "__main__":
    
#     obj = EventSourcer()
#     obj.add(5)
#     obj.add(5)
#     obj.add(5)
#     obj.add(5)
#     obj.subtract(5)
#     obj.bulk_undo(5)
#     obj.bulk_redo(5)


#     print(obj.value)

    
