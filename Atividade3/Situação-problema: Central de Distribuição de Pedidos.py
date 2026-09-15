import random
import time


comparacoes = 0
trocas = 0
movimentacoes = 0


def reset_contadores():
    global comparacoes, trocas, movimentacoes
    comparacoes = 0
    trocas = 0
    movimentacoes = 0



# BUBBLE SORT

def bubble_sort(vetor):
    global comparacoes, trocas
    n = len(vetor)
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            comparacoes += 1
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                trocas += 1
                trocou = True
        if not trocou:
            break



# INSERTION SORT

def insertion_sort(vetor):
    global comparacoes, movimentacoes
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                movimentacoes += 1
                j -= 1
            else:
                break
        vetor[j + 1] = chave
        movimentacoes += 1  # inserção da chave



# SELECTION SORT

def selection_sort(vetor):
    global comparacoes, trocas
    n = len(vetor)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes += 1
            if vetor[j] < vetor[min_idx]:
                min_idx = j
        if min_idx != i:
            vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]
            trocas += 1


# QUICK SORT 

def quick_sort(vetor, inicio=0, fim=None):
    global comparacoes, movimentacoes
    if fim is None:
        fim = len(vetor) - 1

    if inicio < fim:
        pivo = vetor[fim]
        i = inicio - 1
        for j in range(inicio, fim):
            comparacoes += 1
            if vetor[j] <= pivo:
                i += 1
                if i != j:
                    vetor[i], vetor[j] = vetor[j], vetor[i]
                    movimentacoes += 1
        vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
        movimentacoes += 1
        p = i + 1
        quick_sort(vetor, inicio, p - 1)
        quick_sort(vetor, p + 1, fim)



# EXPERIMENTO

def executar_experimento(tamanho):
    
    print(f" VETOR COM {tamanho} ELEMENTOS")
  

    original = [random.randint(1, 10_000) for _ in range(tamanho)]
    print(f"Vetor original (5 primeiros): {original[:5]} ...")

    
    vetor_bubble = original.copy()
    vetor_insertion = original.copy()
    vetor_selection = original.copy()
    vetor_quick = original.copy()

    algoritmos = [
        ("Bubble Sort", bubble_sort, vetor_bubble),
        ("Insertion Sort", insertion_sort, vetor_insertion),
        ("Selection Sort", selection_sort, vetor_selection),
        ("Quick Sort", quick_sort, vetor_quick),
    ]

    print(f"\n{'Algoritmo':<16}{'Comparações':>14}{'Trocas':>10}"
          f"{'Movimentações':>16}{'Tempo (s)':>12}")


    for nome, func, vetor in algoritmos:
        reset_contadores()
        inicio = time.perf_counter()
        func(vetor)
        fim = time.perf_counter()

        # Verificação de ordenação
        assert vetor == sorted(original), f"{nome} não ordenou corretamente!"

        print(f"{nome:<16}{comparacoes:>14}{trocas:>10}"
              f"{movimentacoes:>16}{fim - inicio:>12.6f}")



# EXECUÇÃO PRINCIPAL

if __name__ == "__main__":
    random.seed(42)  # reprodutibilidade
    for tam in [10, 20, 1000]:
        executar_experimento(tam)
