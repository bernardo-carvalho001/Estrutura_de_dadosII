# Tabela de Operações por Algoritmo

| Tamanho do Array | Bubble Sort – Comparações | Bubble Sort – Trocas | Quick Sort – Comparações | Quick Sort – Movimentações* |
|---|---|---|---|---|
| 10 | 45 | 26 | 29 | 15 |
| 20 | 190 | 95 | 79 | 72 |
| 1.000 | 499.500 | 243.427 | 11.091 | 5.634 |

*Observação: O Quick Sort apresenta "Trocas" nos dados, que correspondem às movimentações de elementos durante o particionamento.

---

# Respostas às Perguntas

## a) Qual algoritmo realizou menos operações para 10 elementos?

Quick Sort realizou menos operações: 29 comparações + 15 movimentações = 44 operações totais, contra 45 comparações + 26 trocas = 71 operações do Bubble Sort.

## b) O comportamento permaneceu igual para 20 elementos?

Sim, permaneceu igual. O Quick Sort continuou sendo mais eficiente:

Quick Sort: 79 + 72 = 151 operações

Bubble Sort: 190 + 95 = 285 operações

A diferença começou a aumentar: Quick Sort foi cerca de 2,41x mais eficiente (contra 1,55x para 10 elementos).

## c) O que aconteceu quando o tamanho aumentou para 1.000 elementos?

Houve uma explosão nas operações do Bubble Sort enquanto o Quick Sort manteve crescimento moderado:

Bubble Sort: 499.500 + 243.427 = 742.927 operações

Quick Sort: 11.091 + 5.634 = 16.725 operações

O Quick Sort tornou-se 45,04x mais eficiente que o Bubble Sort.

## d) Qual algoritmo apresentou maior crescimento da quantidade de operações?

Bubble Sort apresentou crescimento muito maior. Enquanto:

Quick Sort cresceu de forma aproximadamente O(n log n)

Bubble Sort cresceu na ordem de O(n²)

Para visualizar:

De 10 para 1.000 elementos (100x mais dados):

Bubble Sort: operações aumentaram ~10.464 vezes

Quick Sort: operações aumentaram ~380 vezes

## e) Os resultados experimentais são coerentes com as complexidades teóricas estudadas?

Sim, perfeitamente coerentes.

Bubble Sort (complexidade O(n²)):

Para n=10: ~100 operações (próximo de 10²)

Para n=20: ~400 operações (próximo de 20² = 400)

Para n=1.000: ~1.000.000 operações (próximo de 1.000²)

Os dados mostram 742.927 operações, confirmando a complexidade quadrática.

Quick Sort (complexidade O(n log n)):

Para n=10: ~10 × log₂(10) ≈ 33 operações

Para n=20: ~20 × log₂(20) ≈ 86 operações

Para n=1.000: ~1.000 × log₂(1.000) ≈ 9.966 operações

Os dados mostram 16.725 operações, próximas do esperado teoricamente.

## f) Em qual situação você escolheria Bubble Sort?

Raramente seria a melhor escolha, mas poderia ser útil em:

Arrays muito pequenos (n < 10-20) - onde a simplicidade do código pode compensar a ineficiência teórica

Arrays quase ordenados - pois o Bubble Sort otimizado pode ter performance próxima de O(n)

Ambientes educacionais - para demonstrar conceitos básicos de ordenação

Recursos muito limitados - onde o overhead do Quick Sort (recursão) não é desejável

Quando a estabilidade é essencial - Bubble Sort é estável, mantendo a ordem de elementos iguais

## g) Em qual situação você escolheria Quick Sort?

O Quick Sort é a escolha preferível na grande maioria dos casos práticos:

Arrays grandes (n > 100) - onde a diferença de performance é significativa

Dados aleatórios/desordenados - onde seu desempenho é excelente

Sistemas com memória disponível - para suportar a recursão

Aplicações com requisitos de performance - onde a velocidade é crítica

Linguagens com boa otimização de recursão - como C/C++, Java, Python (com ajustes)

Quando a ordenação in-place é desejada - Quick Sort requer pouca memória extra
