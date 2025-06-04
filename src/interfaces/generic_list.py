from abc import ABC, abstractmethod
from typing import Any, Optional


class IGenericList(ABC):

    @abstractmethod
    def insert(self, index: int, value: Any) -> Any:
        pass

    @abstractmethod
    def remove(self, index: int) -> Any:
        pass

    @abstractmethod
    def search(self, value: Any) -> Any:
        pass

    @abstractmethod
    def get(self, index: int) -> Optional[Any]:
        pass

    @abstractmethod
    def set(self, index: int, value: Any) -> Any:
        pass

    @abstractmethod
    def append(self, value: Any) -> Any:
        pass

    @abstractmethod
    def prepend(self, value: Any) -> Any:
        pass
