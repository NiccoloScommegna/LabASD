from linked_list import LinkedList, Node


class OrderedLinkedList(LinkedList):

    size: int = 0

    def insert(self, item):
        # Inserisci l'elemento in modo ordinato (decrescente) nella lista
        current = self.head
        previous = None

        while current is not None and current.get_data() > item:
            previous = current
            current = current.get_next()

        new_node = Node(item)
        if previous is None:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            new_node.set_next(current)
            previous.set_next(new_node)

        self.size += 1

    def extract_max(self):
        # Estrai l'elemento massimo dalla testa della lista ordinata
        if self.head is None:
            print("Linked list vuota")
            return None

        max_value = self.head.get_data()
        self.head = self.head.get_next()
        self.size -= 1
        return max_value
