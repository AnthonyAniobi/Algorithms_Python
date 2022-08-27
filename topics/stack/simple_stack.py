class Stack:
    def __init__(self, limit=10) -> None:
        self.stk = []
        self.limit = limit
    
    def isEmpty(self):
        return len(self.stk)<=0
    
    def push(self, item):
        if len(self.stk) >= self.limit:
            print('Stack overflow')
        else:
            self.stk.append(item)
    
    def pop(self):
        if len(self.stk) <= 0:
            print('Stack underflow')
        else:
            return self.stk.pop()
    
    def peek(self):
        if len(self.stk) <= 0:
            print('Stack underflow')
        else:
            return self.stk[-1]
    
    def size(self):
        return len(self.stk)

    def __str__(self) -> str:
        return ','.join(self.stk)

if __name__ == '__main__':
    stack = Stack(10)
    stack.push('1')
    stack.push('2')
    stack.push('3')
    stack.push('4')
    stack.push('5')
    stack.push('6')
    stack.push('7')
    stack.push('8')

    print(stack.peek())
    stack.pop()
    print(stack.peek())
    stack.pop()
    print(stack)