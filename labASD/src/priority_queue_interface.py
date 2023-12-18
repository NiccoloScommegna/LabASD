from abc import ABC, abstractmethod


class PriorityQueueInterface(ABC):

    size: int

    @abstractmethod
    def insert(self, item: int) -> None:
        pass

    @abstractmethod
    def extract_max(self) -> int | None:
        pass
