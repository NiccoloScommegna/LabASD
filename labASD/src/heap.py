import math
import numpy as np
from priority_queue_interface import PriorityQueueInterface


class Heap(PriorityQueueInterface):

    size: int = 0

    def __init__(self):
        self.data = np.array([], dtype=int or float)

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def left_child(self, i: int) -> int:
        return i * 2 + 1

    def right_child(self, i: int) -> int:
        return i * 2 + 2

    def max_heapify(self, i: int) -> None:
        left = self.left_child(i)
        right = self.right_child(i)
        size = len(self.data)
        if left < size and self.data[left] > self.data[i]:
            largest = left
        else:
            largest = i
        if right < size and self.data[right] > self.data[largest]:
            largest = right
        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.max_heapify(largest)

    def insert(self, item: int) -> None:
        # Ottieni l'indice dell'ultimo elemento nell'heap e aggiunge il nuovo elemento in coda all'array
        index = self.size
        self.data = np.append(self.data, item)
        self.size += 1

        # Eseguo il passo di "heapify-up" per ripristinare la proprietà dell'heap massimo
        # Si ripristina la proprietà dell'heap massimo con un approccio bottom-up, solo se l'elemento inserito è maggiore del genitore
        while (index != 0) and item > self.data[self.parent(index)]:
            # Scambia il valore del genitore con il valore del figlio
            self.data[index], self.data[self.parent(index)] = self.data[self.parent(index)], self.data[index]
            # Aggiorna l'indice al livello superiore
            index = self.parent(index)

    def extract_max(self) -> int | None:
        # Se l'heap è vuoto, restituisce None
        if self.size == 0:
            print("Heap vuoto")
            return None

        # Salva il massimo (radice) prima di rimuoverlo dall'heap
        max_value = self.data[0]

        # Sostituisci la radice con l'ultimo elemento e rimuovi l'ultimo elemento usando
        self.data[0] = self.data[self.size - 1]
        self.data = np.delete(self.data, self.size - 1)
        self.size -= 1

        # Eseguo il passo di "heapify-down" per mantenere la proprietà dell'heap massimo
        self.max_heapify(0)

        # Restituisco il valore massimo precedentemente salvato
        return max_value

    def print_heap(self) -> None:
        print(self.data)

    def display_tree(self) -> None:
        n = len(self.data)
        if n == 0:
            print("Heap vuoto")
            return

        height = int(math.log2(n)) + 1
        max_width = 2 ** height - 1

        for i in range(height):
            nodes_in_level = 2 ** i
            spacing = max_width // (nodes_in_level + 1)
            for j in range(nodes_in_level):
                index = 2 ** i - 1 + j
                if index < n:
                    print(f"{self.data[index]:>{spacing}}", end=" ")
            print()  # Vai alla prossima riga
