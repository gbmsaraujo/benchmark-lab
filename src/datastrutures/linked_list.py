from typing import Any, Optional

from src.interfaces.generic_list import IGenericList


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional[Node] = None


class LinkedList(IGenericList):
    def __init__(self, value: Any = None):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.length = 0

        if value is not None:
            new_node = Node(value)
            self.head = self.tail = new_node
            self.length = 1

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value: Any) -> None:
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self) -> Optional[Any]:
        if self.length == 0:
            return None
        if self.length == 1:
            value = self.head.value # type: ignore
            self.head = self.tail = None
            self.length = 0
            return value

        current = self.head
        while current.next is not self.tail: # type: ignore
            current = current.next # type: ignore

        assert current is not None and self.tail is not None
        value = self.tail.value
        self.tail = current
        self.tail.next = None
        self.length -= 1
        return value

    def pop_first(self) -> Optional[Any]:
        if self.length == 0:
            return None
        assert self.head is not None
        value = self.head.value
        self.head = self.head.next
        if self.length == 1:
            self.tail = None
        self.length -= 1
        return value

    def insert(self, index: int, value: Any) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True

        new_node = Node(value)
        prev = self.get_node(index - 1)
        assert prev is not None
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True

    def remove(self, index: int) -> Optional[Any]:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev = self.get_node(index - 1)
        assert prev is not None and prev.next is not None
        value = prev.next.value
        prev.next = prev.next.next
        self.length -= 1
        return value

    def get(self, index: int) -> Optional[Any]:
        node = self.get_node(index)
        return node.value if node else None

    def set(self, index: int, value: Any) -> bool:
        node = self.get_node(index)
        if node is None:
            return False
        node.value = value
        return True

    def search(self, value: Any) -> int:
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def get_node(self, index: int) -> Optional[Node]:
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            assert current is not None
            current = current.next
        return current

    def __len__(self) -> int:
        return self.length

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
