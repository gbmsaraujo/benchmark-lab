from src.controller.benchmark_controller import BenchmarkController
from src.datastrutures.linked_list import LinkedList
from src.datastrutures.python_list import PythonList



linked_list = LinkedList()
my_list = PythonList()

qnt_values = 10000

linked_list_benchmark = BenchmarkController(linked_list, qnt_values=qnt_values)
list_benchmark = BenchmarkController(my_list, qnt_values=qnt_values)

option = "insertion"

print("Executando benchmarks...\n")

print("✅ Inserção:")
print(f"Python List: {list_benchmark.calculation(option)} segundos")
print(f"Python Linked List: {linked_list_benchmark.calculation(option)} segundos")