import random
from typing import Any
from src.interfaces.generic_list import IGenericList
from src.utils.timer import calculate_time, now_time


class BenchmarkController:
    def __init__(self, generic_list: IGenericList, qnt_values: int = 100) -> None:
        self.generic_list = generic_list
        self.random_values = self.__generate_values(qnt_values)
        self.operations = {"insertion": self.__insert_calculation}

    def __insert_calculation(self):
        start = now_time()

        for i, value in enumerate(self.random_values):
            self.generic_list.insert(i, value)

        end = now_time()

        return calculate_time(start, end)

    def calculation(self, option: str) -> Any:
        if option not in self.operations:
            raise ValueError(f"Operação inválida: '{option}'")
        return self.operations[option]()

    def __generate_values(self, qnt_values: int = 100):
        return [random.randint(100, 1000) for _ in range(qnt_values)]
