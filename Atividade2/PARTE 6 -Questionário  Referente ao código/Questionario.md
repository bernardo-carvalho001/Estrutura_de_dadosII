## Perguntas e Respostas

### 1. O aumento do tamanho da estrutura de dados influencia a quantidade de operações?

**R:** Sim. As operações crescem proporcionalmente ao número de elementos - **O(m × n)**.

### 2. Bubble Sort e Quick Sort crescem da mesma maneira quando o número de elementos aumenta?

**R:** Não. Cada algoritmo apresenta um comportamento diferente:

| Algoritmo | Comportamento | Complexidade |
|-----------|---------------|--------------|
| **Bubble Sort** | Crescimento "explosivo" | **O(n²)** |
| **Quick Sort** | Crescimento mais "suave" | **O(n log n)** |

### 3. Por que analisar somente o resultado final da ordenação não é suficiente para comparar algoritmos?

**R:** Porque o resultado final (array ordenado) é o mesmo para ambos os algoritmos, mas o **custo computacional** para chegar a esse resultado é completamente diferente. Enquanto um algoritmo pode realizar poucas operações, o outro pode realizar milhares de operações para chegar ao mesmo resultado.
