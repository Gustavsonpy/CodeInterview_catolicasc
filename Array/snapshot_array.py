# Função para busca binária
from bisect import bisect_right

class SnapshotArray(object):

    def __init__(self, length):
        # Quantidade de snaps feitos
        self.snap_id = 0

        # Para cada índice, temos uma lista de tuplas (snap_id, valor)
        # Inicializamos todos com (0, 0), pois o array começa com zeros
        self.data = [[(0, 0)] for _ in range(length)]
        
    # Adiciona uma nova versão de valor em um índice
    def set(self, index, val):

        # Verifica se último valor registrado foi no snapshot atual
        if self.data[index][-1][0] == self.snap_id:

            # Atualiza o valor (evita duplicações)
            self.data[index][-1] = (self.snap_id, val)
        else:

            # Adiciona uma nova versão com o snap atual
            self.data[index].append((self.snap_id, val))
        
    # Incrementa um contador de snaps e retorna o ID do snap criado
    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1
        
    # Retorna o valor de um índice em snapshot específico
    def get(self, index, snap_id):
        arr = self.data[index]

        # Busca o valor correto via 'busca binária'
        i = bisect_right(arr, (snap_id, float('inf'))) - 1

        # Retorna a segunda posição da tupla
        return arr[i][1]

## TEST 01
# Array de tamanho 3: [0, 0, 0]
snapshotArr = SnapshotArray(3)

# Define index 0 como 5 (snap_id = 0)
snapshotArr.set(0, 5)
snap_id = snapshotArr.snap()

# Altera o index para 6 (snap_id = 1)
snapshotArr.set(0, 6)

resultado = snapshotArr.get(0, snap_id)

print('Teste 01:', resultado)  # esperado: 5

## TEST 02
snapshotArr = SnapshotArray(3)

snapshotArr.set(0, 5)
snapshotArr.set(1, 10)

snap0 = snapshotArr.snap()  # snapshot 0

snapshotArr.set(0, 6)

snap1 = snapshotArr.snap()  # snapshot 1

snapshotArr.set(1, 20)

# Consulta no estado mais antigo
print('\nTeste 02:', snapshotArr.get(0, snap0))  # esperado: 5
print('Teste 02:', snapshotArr.get(1, snap0))  # esperado: 10

# Consulta no estado intermediário
print('Teste 02:', snapshotArr.get(0, snap1))  # esperado: 6
print('Teste 02:', snapshotArr.get(1, snap1))  # esperado: 10

# Consulta no estado mais recente
print('Teste 02:', snapshotArr.get(1, 2))      # esperado: 20 (snapshot atual implícito)