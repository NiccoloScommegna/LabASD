from enum import Enum


class DataType(Enum):
    HEAP = "Heap"
    LINKED_LIST = "Lista Concatenata"
    ORDERED_LINKED_LIST = "Lista Concatenata Ordinata"


class ArrayType(Enum):
    RANDOM = "Random"
    ASCENDING = "Crescente"
    DESCENDING = "Decrescente"


class ArraySize(Enum):
    SMALL = 100
    MEDIUM = 1000
    LARGE = 10000
