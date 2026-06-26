class MinStack:

    def __init__(self):

        self.minstack = []
        

    def push(self, val: int) -> None:

        return self.minstack.append(val)
        

    def pop(self) -> None:

        return self.minstack.pop()
        

    def top(self) -> int:

        return self.minstack[-1]

    def getMin(self) -> int:

        return min(self.minstack)
        
