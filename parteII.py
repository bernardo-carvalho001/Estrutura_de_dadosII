import random
import time
import copy

def bubble_sort(arr):
    n = len(arr)
    comparacoes = 0
    trocas = 0
    
    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1
                
    return comparacoes, trocas

def quick_sort(arr):
    
    comparacoes = 0
    trocas = 0
    
    def _quick_sort(arr, low, high):
        nonlocal comparacoes, trocas
        
        if low < high:
            pi, comp, troc = _partition(arr, low, high)
            comparacoes += comp
            trocas += troc
            
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)
    
    def _partition(arr, low, high):
        comp = 0
        troc = 0
        
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            comp += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                troc += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        troc += 1
        
        return i + 1, comp, troc
    
    _quick_sort(arr, 0, len(arr) - 1)
    return comparacoes, trocas

def gerar_array(tamanho, min_val=1, max_val=1000):
    return [random.randint(min_val, max_val) for _ in range(tamanho)]

def testar_algoritmos(tamanho):

    print(f" TESTE COM {tamanho} ELEMENTOS ")
  
    
    arr_original = gerar_array(tamanho)
    print(f"Array original (primeiros 20): {arr_original[:20]}")
    
    arr_bubble = copy.deepcopy(arr_original)
    arr_quick = copy.deepcopy(arr_original)
    
    print(f"\n BUBBLE SORT ")
    inicio = time.time()
    comp_bubble, troc_bubble = bubble_sort(arr_bubble)
    tempo_bubble = time.time() - inicio
    
    print(f"Comparações: {comp_bubble:,}")
    print(f"Trocas: {troc_bubble:,}")
    print(f"Tempo: {tempo_bubble:.6f}s")
    print(f"Ordenado: {arr_bubble[:20]}")
    
    print(f"\nQUICK SORT ")
    inicio = time.time()
    comp_quick, troc_quick = quick_sort(arr_quick)
    tempo_quick = time.time() - inicio
    
    print(f"Comparações: {comp_quick:,}")
    print(f"Trocas: {troc_quick:,}")
    print(f"Tempo: {tempo_quick:.6f}s")
    print(f"Ordenado: {arr_quick[:20]}")
    
    print(f"\nArrays iguais: {arr_bubble == arr_quick}")
    
    print(f"\nRESUMO ")
    print(f"Bubble: {comp_bubble:,} comp, {troc_bubble:,} trocas, {tempo_bubble:.6f}s")
    print(f"Quick:  {comp_quick:,} comp, {troc_quick:,} trocas, {tempo_quick:.6f}s")
    print(f"Quick é {comp_bubble/comp_quick:.2f}x mais eficiente")

def main():
  
    print(" ANÁLISE DE ALGORITMOS ")
  
    
    random.seed(42)
    tamanhos = [10, 20, 1000]
    
    for tamanho in tamanhos:
        testar_algoritmos(tamanho)
  
if __name__ == "__main__":
    main()
