from enum import Enum


class DataType(Enum):
    HEAP = "Heap"
    LINKED_LIST = "Linked List"
    ORDERED_LINKED_LIST = "Ordered Linked List"


class ArrayType(Enum):
    RANDOM = "Random"
    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class ArraySize(Enum):
    SMALL = 100
    MEDIUM = 1000
    LARGE = 10000
