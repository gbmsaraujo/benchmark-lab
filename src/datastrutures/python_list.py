from typing import Any, List


from typing import Any, List, Optional

from src.interfaces.generic_list import IGenericList

class PythonList(IGenericList):
    def __init__(self):
        self.data: List[Any] = []

    def insert(self, index: int, value: Any) -> None:
        if 0 <= index <= len(self.data):
            self.data.insert(index, value)
        else:
            raise IndexError("Index out of bounds")

    def remove(self, index: int) -> None:
        if 0 <= index < len(self.data):
            self.data.pop(index)
        else:
            raise IndexError("Index out of bounds")

    def search(self, value: Any) -> int:
        for i, item in enumerate(self.data):
            if item == value:
                return i
        return -1

    def get(self, index: int) -> Optional[Any]:
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            return None

    def set(self, index: int, value: Any) -> None:
        if 0 <= index < len(self.data):
            self.data[index] = value
        else:
            raise IndexError("Index out of bounds")

    def append(self, value: Any) -> None:
        self.data.append(value)

    def prepend(self, value: Any) -> None:
        self.data.insert(0, value)

    def __len__(self) -> int:
        return len(self.data)
