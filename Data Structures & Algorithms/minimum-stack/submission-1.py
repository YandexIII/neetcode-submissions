class MinStack:

    def __init__(self):
        self.stack = []
        self.ordered_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        low = 0
        high = len(self.ordered_stack)

        while low < high:
            mid = (low + high) // 2
            if self.ordered_stack[mid] < val:
                low = mid + 1
            else:
                high = mid
        
        self.ordered_stack.insert(low, val)

        

    def pop(self) -> None:
        self.ordered_stack.remove(self.stack[-1])
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ordered_stack[0]
