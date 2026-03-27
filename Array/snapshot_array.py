from bisect import bisect_right

class SnapshotArray(object):

    def __init__(self, length):
        self.snap_id = 0
        self.data = [[(0, 0)] for _ in range(length)]
        
    # Adiciona uma nova versão
    def set(self, index, val):
        if self.data[index][-1][0] == self.snap_id:
            self.data[index][-1] = (self.snap_id, val)
        else:
            self.data[index].append((self.snap_id, val))
        
    # Incrementa um contador
    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1
        
    # Busca o valor correto via binary search
    def get(self, index, snap_id):
        arr = self.data[index]

        i = bisect_right(arr, (snap_id, float('inf'))) - 1

        return arr[i][1]

## TEST 01
snapshotArr = SnapshotArray(3)

snapshotArr.set(0, 5)
snap_id = snapshotArr.snap()

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

print('\nTeste 02:', snapshotArr.get(0, snap0))  # esperado: 5
print('Teste 02:', snapshotArr.get(1, snap0))  # esperado: 10

print('Teste 02:', snapshotArr.get(0, snap1))  # esperado: 6
print('Teste 02:', snapshotArr.get(1, snap1))  # esperado: 10

print('Teste 02:', snapshotArr.get(1, 2))      # esperado: 20 (snapshot atual implícito)