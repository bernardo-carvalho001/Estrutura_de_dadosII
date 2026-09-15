# Etapa 3 – Resultados

| Tamanho | Bubble Comparações | Bubble Trocas | Insertion Comparações | Insertion Mov. | Selection Comparações | Selection Trocas | Quick Comparações | Quick Mov. |
|--------:|-------------------:|--------------:|----------------------:|---------------:|----------------------:|-----------------:|------------------:|-----------:|
| 10      | 44                 | 19            | 27                    | 28             | 45                    | 7                | 29                | 8          |
| 20      | 189                | 84            | 99                    | 103            | 190                   | 16               | 58                | 30         |
| 1.000   | 499122             | 239681        | 240670                | 240680         | 499500                | 992              | 10385             | 4718       |


# Respostas do Questionário

## a) Qual algoritmo realizou o menor número de comparações para 10 elementos?

O Insertion Sort, com 27 comparações. Em seguida vieram o Quick Sort (29), o Bubble Sort (44) e o Selection Sort (45).

---

## b) Qual algoritmo realizou menos trocas ou movimentações?

Considerando trocas + movimentações para 10 elementos:

| Algoritmo      | Trocas | Movimentações | Total |
|----------------|--------|---------------|-------|
| Bubble Sort    | 19     | 0             | 19    |
| Insertion Sort | 0      | 28            | 28    |
| Selection Sort | 7      | 0             | 7     |
| Quick Sort     | 0      | 8             | 8     |

O Selection Sort realizou o menor número de operações de movimentação (7 trocas), seguido pelo Quick Sort (8 movimentações).

---

## c) O comportamento observado para 10 elementos permaneceu semelhante quando o tamanho aumentou para 20?

Sim, em grande parte. O Insertion Sort continuou sendo o que faz menos comparações (99), o Selection Sort continuou com o menor número de trocas (16), e o Quick Sort manteve o melhor equilíbrio geral (58 comparações e 30 movimentações). A única inversão foi que o Selection Sort passou a ter mais comparações que o Bubble Sort (190 contra 189) — diferença de apenas 1, praticamente empate.

---

## d) O que aconteceu com a quantidade de operações quando o vetor passou para 1.000 elementos?

Houve um crescimento explosivo para os algoritmos quadráticos:

- **Bubble Sort:** de 189 para 499.122 comparações (~2.640× mais).
- **Insertion Sort:** de 99 para 240.670 comparações (~2.430× mais).
- **Selection Sort:** de 190 para 499.500 comparações (~2.629× mais).
- **Quick Sort:** de 58 para 10.385 comparações (~179× mais).

O Quick Sort cresceu de forma muito mais moderada, evidenciando sua complexidade O(n log n) contra O(n²) dos demais.

---

## e) Bubble Sort, Insertion Sort e Selection Sort apresentam complexidade O(n²) em situações típicas estudadas. Eles apresentaram exatamente a mesma quantidade de operações? Explique utilizando seus resultados.

Não. Apesar de todos serem O(n²), o número concreto de operações difere bastante:

**Comparações (n = 1.000):**

- Bubble: 499.122
- Insertion: 240.670 (≈ metade do Bubble)
- Selection: 499.500 (sempre o pior caso teórico: n(n−1)/2)

**Trocas/Movimentações (n = 1.000):**

- Bubble: 239.681 trocas
- Insertion: 240.680 movimentações
- Selection: apenas 992 trocas

**Explicação:** a notação O(n²) descreve apenas a ordem de crescimento, não o valor exato. Cada algoritmo executa uma quantidade diferente de operações dentro do mesmo limite assintótico:

- O Selection Sort sempre faz n(n−1)/2 comparações, independentemente da ordem de entrada — por isso atinge 499.500.
- O Insertion Sort interrompe o laço interno assim que encontra a posição correta, fazendo em média metade das comparações do Bubble.
- O Bubble Sort tem desempenho dependente da ordem inicial e realizou 499.122 comparações — praticamente o pior caso.

---

## f) Qual algoritmo apresentou maior crescimento no número de operações?

O Bubble Sort e o Selection Sort apresentaram o maior crescimento absoluto em comparações (de ~190 para ~499.500, ou seja, ~2.630×). Em número de trocas, o Bubble Sort disparou de 84 para 239.681 — o maior salto entre todos os algoritmos.

---

## g) Como o comportamento experimental do Quick Sort se diferenciou dos demais algoritmos?

O Quick Sort se destacou por:

- **Crescimento muito mais lento:** de 29 para 10.385 comparações (n=10 → n=1.000), enquanto os demais ultrapassaram 240 mil.
- **Menor tempo de execução:** 0,002570 s contra 0,062–0,107 s dos demais em n=1.000 — cerca de 24 a 42× mais rápido.
- **Poucas movimentações:** 4.718 em n=1.000, contra 239.681 do Bubble e 240.680 do Insertion.
- **Comportamento típico O(n log n)**, confirmando a teoria.

---

## h) Os resultados encontrados são coerentes com as complexidades teóricas estudadas?

Sim, totalmente coerentes.

| Algoritmo      | Complexidade teórica (média) | Comportamento observado                              |
|----------------|------------------------------|------------------------------------------------------|
| Bubble Sort    | O(n²)                        | Crescimento quadrático confirmado                    |
| Insertion Sort | O(n²)                        | Crescimento quadrático confirmado                    |
| Selection Sort | O(n²)                        | Sempre n(n−1)/2 comparações — confirmado             |
| Quick Sort     | O(n log n)                   | Crescimento suave e muito inferior — confirmado      |

Os valores de comparação do Selection Sort (499.500 = 1000·999/2) confirmam exatamente a fórmula teórica do pior caso.

---

## i) Se você fosse responsável pelo sistema da central de distribuição e precisasse ordenar milhares de pedidos, qual dos quatro algoritmos escolheria? Justifique utilizando os resultados do experimento.

Escolheria o Quick Sort.

**Justificativa baseada nos resultados:**

- Menor número de comparações em todos os tamanhos testados — em n=1.000, apenas 10.385 contra ~240–500 mil dos demais.
- Menor tempo de execução — 0,002570 s em n=1.000, cerca de 42× mais rápido que o Bubble Sort e 24× mais rápido que o Insertion Sort.
- Menor número de movimentações — 4.718 em n=1.000, contra ~240 mil do Bubble e do Insertion.
- Escalabilidade comprovada — enquanto os algoritmos O(n²) explodem com o crescimento do vetor, o Quick Sort mantém crescimento próximo de O(n log n), essencial para uma central que processa milhares de pedidos diariamente.
- Tempos praticamente idênticos em vetores pequenos (n=10), mostrando que não há desvantagem em usá-lo também para lotes pequenos.

Portanto, o Quick Sort é a escolha mais adequada para garantir desempenho e escalabilidade no sistema da central de distribuição.
