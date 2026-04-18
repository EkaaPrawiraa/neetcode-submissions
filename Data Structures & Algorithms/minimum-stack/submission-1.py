class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.mins = val
        else:
            self.stack.append(val - self.mins)
            if val < self.mins:
                self.mins = val
        
    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.mins = self.mins - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.mins
        else:
            return self.mins
        
    def getMin(self) -> int:
        return self.mins
        
