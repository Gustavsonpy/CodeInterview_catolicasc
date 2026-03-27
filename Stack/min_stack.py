class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack:
          self.min_stack.append(val)
        else:
          self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
      return self.min_stack[-1]

## TEST 01
print('Teste 01:')
minStack = MinStack()

minStack.push(-2)
minStack.push(0)
minStack.push(-3)

print(minStack.getMin())  # esperado: -3

minStack.pop()

print(minStack.top())  # esperado: 0
print(minStack.getMin())  # esperado: -2

## TEST 02
# Valores decrescentes
print('Teste 02:')
minStack = MinStack()

minStack.push(5)
minStack.push(4)
minStack.push(3)
minStack.push(2)

print(minStack.getMin())  # esperado: 2

minStack.pop()
print(minStack.getMin())  # esperado: 3