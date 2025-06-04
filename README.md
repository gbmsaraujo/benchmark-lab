# 🧪 DS Benchmark Lab

**DS Benchmark Lab** é um projeto educacional que compara o desempenho prático entre a lista nativa do Python (`list`) e uma implementação manual de lista ligada (`LinkedList`). O foco é avaliar operações comuns de estruturas lineares com medição de tempo real, usando `time.perf_counter()`.

---

## 🚀 Objetivo

Investigar o custo computacional de operações básicas em listas dinâmicas, como inserção, remoção, busca, leitura e escrita. O projeto foi criado para fins de aprendizado de estruturas de dados e benchmarking em Python.

A ideia é expandir o projeto para incluir **comparativos entre várias estruturas de dados**, como:

* Fila, Pilha, Deque
* Hash Table
* Árvore Binária, Heap, Trie

### ❓ Vale comparar qualquer estrutura?

Sim, **desde que a comparação tenha propósito**:

* ✅ Comparar **estruturas equivalentes** (ex: `list` vs `linked list`) é ideal
* ⚠️ Comparar **estruturas diferentes** (ex: lista vs árvore) só faz sentido se estiver resolvendo o mesmo problema (ex: busca, ordenação, inserção rápida)

---

## ⚙️ Estruturas Comparadas

* `PythonList`: Wrapper sobre a lista nativa do Python
* `LinkedList`: Implementação manual de uma lista ligada simples

Ambas seguem a mesma interface (`IGenericList`) para permitir comparações consistentes.

---

## 🧪 Operações Comparadas

| Operação  | Descrição                             |
| --------- | ------------------------------------- |
| `append`  | Adiciona elemento ao final da lista   |
| `prepend` | Adiciona elemento no início da lista  |
| `insert`  | Insere elemento em posição arbitrária |
| `remove`  | Remove elemento de posição arbitrária |
| `search`  | Busca um valor na lista               |
| `get`     | Acessa o valor por índice             |
| `set`     | Altera o valor de um índice           |

Cada operação é executada N vezes (ex: 1.000, 10.000) com valores aleatórios, e o tempo de execução total é registrado.

---

## 📊 Exemplo de Saída

```
Executando benchmarks...

✅ Inserção:
- Python List:       0.0026 segundos
- Linked List:       0.0063 segundos

✅ Busca:
- Python List:       0.0009 segundos
- Linked List:       0.0084 segundos
```

---

## 📁 Estrutura do Projeto

```
ds-benchmark-lab/
├── datastructures/
│   ├── linked_list.py
│   └── python_list.py
├── interfaces/
│   └── generic_list.py
├── utils/
│   └── timer.py
├── controller/
│   └── benchmark_controller.py
├── main.py
└── README.md
```

---

## 📚 Requisitos

* Python 3.10+
* Nenhuma dependência externa

---

## 🤝 Contribuição

Sinta-se à vontade para abrir issues ou pull requests com melhorias, novas estruturas ou métricas adicionais (como consumo de memória).

---

## 🧠 Inspiração

Este projeto foi desenvolvido como parte de estudos sobre estruturas de dados, complexidade algorítmica e boas práticas de benchmarking em Python.
