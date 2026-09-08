

**Resultado da Busca**
- Valor procurado: 9999
- Encontrado: NÃO
- Valor não encontrado na matriz
- Comparações realizadas: 10000
- Tempo de busca: 0.000454 segundos

**Análise:**
- Matriz percorrida completamente: 10000 elementos
- Eficiência: O(n²) onde n = 100 (pior caso)

---

# Tabela de Comparações

| Matriz | Nº de elementos | Busca no início | Busca no final | Valor inexistente |
|--------|----------------|-----------------|----------------|-------------------|
| 2 × 2 | 4 | 3 | 4 | 4 |
| 10 × 10 | 100 | 4 | 100 | 100 |
| 100 × 100 | 10.000 | 134 | 10.000 | 10.000 |

Os números representam a quantidade de comparações realizadas.

---

# Respostas às Perguntas

## a) Por que encontrar um elemento no início exige menos operações?

Porque a busca sequencial percorre os elementos em ordem linear (linha por linha). Quando o elemento está no início, ele é encontrado rapidamente, com poucas comparações. Quanto mais próximo do início, menos elementos precisam ser verificados antes de encontrar o valor procurado.

## b) O que acontece quando o elemento procurado não existe?

Quando o elemento não existe na matriz, a busca percorre **todos os elementos** da matriz (100% deles) e só então conclui que o valor não está presente. Isso representa o **pior caso** da busca sequencial.

## c) Qual é o pior caso da busca sequencial?

O pior caso ocorre quando:
- O elemento procurado está na **última posição** da matriz, ou
- O elemento **não existe** na matriz

Nestes casos, a busca percorre todos os elementos da matriz, realizando o máximo de comparações possível.

## d) Como o aumento das dimensões da matriz influencia a quantidade de operações?

O aumento das dimensões da matriz aumenta proporcionalmente a quantidade de operações:
- Matriz 2×2 (4 elementos): pior caso = 4 comparações
- Matriz 10×10 (100 elementos): pior caso = 100 comparações
- Matriz 100×100 (10.000 elementos): pior caso = 10.000 comparações

A quantidade de operações cresce na mesma proporção que o número total de elementos da matriz.

## e) Qual a complexidade da busca sequencial em uma matriz com m linhas e n colunas?

A complexidade da busca sequencial em uma matriz m×n é **O(m × n)** ou **O(N)** onde N é o número total de elementos.

Em notação Big O:
- **Melhor caso:** O(1) - quando o elemento está na primeira posição
- **Caso médio:** O(m×n) - percorre aproximadamente metade dos elementos
- **Pior caso:** O(m×n) - percorre todos os elementos

Como a matriz tem m linhas e n colunas, o total de elementos é m×n, portanto a complexidade é linear em relação ao número total de elementos.
