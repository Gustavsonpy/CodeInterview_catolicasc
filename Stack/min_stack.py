class MinStack(object):

    def __init__(self):
        # Armazena todos os valores inseridos
        self.stack = []

        # Armazena o menor valor valor até cada ponto
        self.min_stack = []

    def push(self, val):
        # Adiciona o valor na pilha principal
        self.stack.append(val)

        # Se a min_stack estiver vazia, o primeiro valor já é o mínimo
        if not self.min_stack:
          self.min_stack.append(val)
        else:
          # Caso contrário, compara:
          # - valor atual (val)
          # - último mínimo armazenado (topo da min_stack)
          # Guarda o menor dos dois
          self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        # Remove o topo da pilha
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        # Retorna o último elemento inserido no topo da pilha
        return self.stack[-1]

    def getMin(self):
      # Retorna o menor valor atual da pilha
      return self.min_stack[-1]

## TEST 01
print('Teste 01:')

# Criação da estrutura
minStack = MinStack()

# Inserção de valores
minStack.push(-2)
minStack.push(0)
minStack.push(-3)

# Retorna o menor valor atual da pilha
print(minStack.getMin())  # esperado: -3

# Remove o topo da pilha (-3)
minStack.pop()

# Agora o topo é 0
print(minStack.top())  # esperado: 0
# O mínimo voltou a ser -2
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