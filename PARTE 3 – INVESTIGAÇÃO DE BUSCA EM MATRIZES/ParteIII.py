import random
import time

def gerar_matriz(linhas, colunas, min_val=1, max_val=100):
   
    return [[random.randint(min_val, max_val) for _ in range(colunas)] for _ in range(linhas)]

def busca_sequencial_matriz(matriz, valor_busca):
   
    linhas = len(matriz)
    colunas = len(matriz[0]) if linhas > 0 else 0
    comparacoes = 0
    
    for i in range(linhas):
        for j in range(colunas):
            comparacoes += 1
            if matriz[i][j] == valor_busca:
                return True, i, j, comparacoes
    
    return False, -1, -1, comparacoes

def exibir_matriz(matriz, titulo="Matriz"):
    
    print(f"\n{titulo}:")
    print("-" * 40)
    for linha in matriz:
      
        print(" ".join(f"{elem:4d}" for elem in linha))
    print("-" * 40)

def exibir_resultado_busca(encontrado, linha, coluna, comparacoes, valor_busca):
  
    print(f"\n RESULTADO DA BUSCA ")
    print(f"Valor procurado: {valor_busca}")
    print(f"Encontrado: {'SIM' if encontrado else 'NÃO'}")
    
    if encontrado:
        print(f"Posição: linha {linha}, coluna {coluna}")
    else:
        print("Valor não encontrado na matriz")
    
    print(f"Comparações realizadas: {comparacoes}")
   
def testar_busca(tamanho_linhas, tamanho_colunas, valor_busca=None):
    
   
    print(f" MATRIZ {tamanho_linhas} × {tamanho_colunas} ")
    print(f" Total de elementos: {tamanho_linhas * tamanho_colunas} ")

    

    matriz = gerar_matriz(tamanho_linhas, tamanho_colunas)
    
    
    if valor_busca is None:
        
        linha_aleatoria = random.randint(0, tamanho_linhas - 1)
        coluna_aleatoria = random.randint(0, tamanho_colunas - 1)
        valor_busca = matriz[linha_aleatoria][coluna_aleatoria]
        print(f"\n Buscando valor existente: {valor_busca}")
    else:
        print(f"\n Buscando valor: {valor_busca}")
    
   
    if tamanho_linhas <= 10 and tamanho_colunas <= 10:
        exibir_matriz(matriz, "Matriz gerada")
    else:
      
        print("\nMatriz gerada (prévia - primeiras 10 linhas e colunas):")
    
        for i in range(min(10, tamanho_linhas)):
            linha = matriz[i][:min(10, tamanho_colunas)]
            print(" ".join(f"{elem:4d}" for elem in linha))
            if i == 9:
                print("... (mais linhas)")

    
  
    inicio = time.time()
    encontrado, linha, coluna, comparacoes = busca_sequencial_matriz(matriz, valor_busca)
    tempo_busca = time.time() - inicio
    

    exibir_resultado_busca(encontrado, linha, coluna, comparacoes, valor_busca)
    print(f"Tempo de busca: {tempo_busca:.6f} segundos")
    
   
    total_elementos = tamanho_linhas * tamanho_colunas
    if encontrado:
        print(f"\n Análise:")
        print(f"  - Elementos percorridos até encontrar: {comparacoes}")
        print(f"  - Posição relativa: {comparacoes/total_elementos*100:.1f}% da matriz percorrida")
    else:
        print(f"\n Análise:")
        print(f"  - Matriz percorrida completamente: {total_elementos} elementos")
        print(f"  - Eficiência: O(n²) onde n = {tamanho_linhas} (pior caso)")

def testar_busca_inexistente(tamanho_linhas, tamanho_colunas):
   
   
    print(f" TESTE DE VALOR INEXISTENTE - {tamanho_linhas}×{tamanho_colunas} ")
    print(f" Total de elementos: {tamanho_linhas * tamanho_colunas} ")
 
    
  
    matriz = gerar_matriz(tamanho_linhas, tamanho_colunas)
    
    
    valor_busca = 9999
    
    print(f"\n Buscando valor: {valor_busca} (fora do intervalo da matriz)")
    
    
    if tamanho_linhas <= 10 and tamanho_colunas <= 10:
        exibir_matriz(matriz, "Matriz gerada")
    else:
        # Para matrizes grandes, mostra apenas uma prévia
        print("\nMatriz gerada (prévia - primeiras 10 linhas e colunas):")
     
        for i in range(min(10, tamanho_linhas)):
            linha = matriz[i][:min(10, tamanho_colunas)]
            print(" ".join(f"{elem:4d}" for elem in linha))
            if i == 9:
                print("... (mais linhas)")

    
    
    inicio = time.time()
    encontrado, linha, coluna, comparacoes = busca_sequencial_matriz(matriz, valor_busca)
    tempo_busca = time.time() - inicio
    
    
    exibir_resultado_busca(encontrado, linha, coluna, comparacoes, valor_busca)
    print(f"Tempo de busca: {tempo_busca:.6f} segundos")
    
    # Análise de eficiência
    total_elementos = tamanho_linhas * tamanho_colunas
    print(f"\n Análise:")
    print(f"  - Matriz percorrida completamente: {total_elementos} elementos")
    print(f"  - Eficiência: O(n²) onde n = {tamanho_linhas} (pior caso)")

def main():
  
    print(" BUSCA SEQUENCIAL EM MATRIZ ")
    print("\nA busca sequencial percorre todos os elementos")
    print("da matriz em ordem de linha (linha por linha).")
    
   
    random.seed(42)
    
   
    testar_busca(2, 2)
    testar_busca_inexistente(2, 2)
    
 
    testar_busca(10, 10)
    testar_busca_inexistente(10, 10)
    
   
    testar_busca(100, 100)
    testar_busca_inexistente(100, 100)
   
if __name__ == "__main__":
    main()
