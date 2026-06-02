# =============================================================
# dfs_cycle.py — RF02
# Dev 2
# DFS com estados BRANCO/CINZA/PRETO para deteccao de ciclos
# Complexidade: O(V+E)
# PROIBIDO: qualquer lib que resolva ciclos automaticamente
# =============================================================

# ATENCAO: para input_estresse (50k nos) a recursao padrao do Python
# pode estourar. Usar uma das opcoes abaixo:
#   opcao A: sys.setrecursionlimit(200000) no topo do arquivo
#   opcao B: implementar DFS iterativa com pilha explicita (recomendado)

# TODO Dev 2: importar Graph de graph.py quando estiver pronto
# Por enquanto, usar: from mock_graph import Graph

BRANCO = 0
CINZA  = 1
PRETO  = 2


def detect_cycles(graph, janela_segundos: int) -> list:
    """
    Detecta ciclos no grafo e retorna lista de Cycle dicts.
    Ordenar resultado por duracao_segundos ASC antes de retornar.
    Ver contracts.py para formato exato de Cycle.
    """
    # TODO Dev 2: implementar DFS com os 3 estados
    # Passos:
    #   1. Inicializar estado de todos os nos como BRANCO
    #   2. Para cada no BRANCO, iniciar DFS
    #   3. Ao entrar num no: marcar CINZA, empilhar no caminho
    #   4. Vizinho CINZA = ciclo encontrado — reconstruir caminho
    #   5. Ao sair do no: marcar PRETO, desempilhar
    #   6. Para cada ciclo: calcular duracao e marcar suspeito
    #   7. Ordenar por duracao_segundos ASC
    pass
