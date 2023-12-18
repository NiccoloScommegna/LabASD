from node import Node
from priority_queue_interface import PriorityQueueInterface


class LinkedList(PriorityQueueInterface):

    size: int = 0

    def __init__(self):
        self.head = None

    def print_list(self) -> None:
        current = self.head
        index = 0
        while current != None:
            print(f"{index}: {current.get_data()}")
            current = current.get_next()
            index += 1

    def insert(self, item: int) -> None:
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        self.size += 1

    def extract_max(self) -> int | None:
        if self.head is None:
            print("Linked list vuota")
            return None

        # Inizializzo le variabili
        previous = self.head
        max_node = self.head
        previous_max_node = None
        current = previous.get_next()

        # Trova l'elemento massimo nella linked list
        while current is not None:
            if current.get_data() > max_node.get_data():
                max_node = current
                previous_max_node = previous
            previous = current
            current = current.get_next()

        # Rimuovi l'elemento massimo dalla linked list
        max_data = max_node.get_data()
        self.size -= 1

        if previous_max_node is None:
            # Se l'elemento massimo è il primo nella lista
            self.head = max_node.get_next()
        else:
            # Altrimenti, se l'elemento massimo è in mezzo o alla fine della lista
            previous_max_node.set_next(max_node.get_next())

        return max_data
