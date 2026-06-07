# =============================================================
# dfs_cycle.py — RF02
# Dev 2
# DFS iterativa com estados BRANCO/CINZA/PRETO para deteccao de ciclos
# Complexidade: O(V+E) tempo | O(V) espaco
# PROIBIDO: qualquer lib que resolva ciclos automaticamente
# =============================================================
#
# Implementacao iterativa com pilha explicita para suportar grafos
# grandes (50k nos) sem estourar o limite de recursao do Python.

BRANCO = 0  # nao visitado
CINZA  = 1  # em progresso (esta na pilha de DFS atual)
PRETO  = 2  # finalizado (todos os vizinhos processados)

# Ciclos maiores que este limite sao ignorados: improvaveis em fraude real
# e evitam MemoryError em grafos aleatorios densos do input_estresse.
MAX_CYCLE_LEN = 1000


def detect_cycles(graph, janela_segundos: int) -> list:
    """
    Detecta todos os ciclos no grafo dirigido usando DFS com 3 estados.

    Parametros:
        graph          - instancia de Graph (de graph.py ou mock_graph.py)
        janela_segundos - ciclos com duracao <= este valor sao marcados suspeito=True

    Retorna lista de dicts Cycle, ordenada por duracao_segundos ASC.
    Retorna [] se nao houver ciclos ou o grafo for vazio. Nunca lanca excecao.

    Formato de cada Cycle:
        {
            "caminho": list[str],        # primeiro == ultimo, ex: ["A","B","A"]
            "duracao_segundos": int,     # max(ts) - min(ts) das arestas do ciclo
            "suspeito": bool             # True se duracao <= janela_segundos
        }

    Calculo de duracao:
        - Coleta o timestamp de cada aresta que faz parte do ciclo
        - duracao = max(timestamps) - min(timestamps)
        - Autoloop (A->A): duracao = 0 (unica aresta, sem diferenca)
    """
    nos = graph.get_all_nodes()
    if not nos:
        return []

    estado = {no: BRANCO for no in nos}
    ciclos = []
    vistos = set()  # (tuple(caminho), duracao) — evita duplicatas

    for no_inicial in nos:
        if estado[no_inicial] != BRANCO:
            continue

        # --- estruturas do caminho atual da DFS ---
        caminho_nos = []            # nos na ordem em que entraram (estado CINZA)
        caminho_pos = {}            # node -> indice em caminho_nos (lookup O(1))
        caminho_ts  = {}            # node -> timestamp da aresta que o colocou aqui

        estado[no_inicial] = CINZA
        caminho_nos.append(no_inicial)
        caminho_pos[no_inicial] = 0
        caminho_ts[no_inicial] = None   # no raiz nao tem aresta de entrada

        # pilha: (no_atual, indice_do_proximo_vizinho_a_examinar)
        pilha = [(no_inicial, 0)]

        while pilha:
            no, idx = pilha[-1]
            vizinhos = graph.get_neighbors(no)

            if idx < len(vizinhos):
                vizinho, _valor, ts = vizinhos[idx]
                pilha[-1] = (no, idx + 1)  # avanca o cursor antes de processar

                if estado[vizinho] == CINZA:
                    # Aresta de retorno: ciclo encontrado
                    _registrar_ciclo(
                        vizinho, caminho_nos, caminho_pos, caminho_ts,
                        ts, janela_segundos, ciclos, vistos
                    )

                elif estado[vizinho] == BRANCO:
                    estado[vizinho] = CINZA
                    caminho_pos[vizinho] = len(caminho_nos)
                    caminho_nos.append(vizinho)
                    caminho_ts[vizinho] = ts
                    pilha.append((vizinho, 0))

                # vizinho PRETO: ignora (aresta cruzada, nao forma ciclo novo)

            else:
                # Todos os vizinhos processados: backtrack
                pilha.pop()
                caminho_nos.pop()
                del caminho_pos[no]
                estado[no] = PRETO

    return sorted(ciclos, key=lambda c: c["duracao_segundos"])


# ---------------------------------------------------------------------------
# Funcao auxiliar — extrair e registrar um ciclo detectado
# ---------------------------------------------------------------------------

def _registrar_ciclo(vizinho_cinza, caminho_nos, caminho_pos, caminho_ts,
                     ts_aresta_retorno, janela_segundos, ciclos, vistos):
    """
    Reconstroi o ciclo a partir da pilha de caminho e o adiciona a `ciclos`
    se ainda nao foi registrado.

    O ciclo comeca em `vizinho_cinza` (no CINZA encontrado como destino da
    aresta de retorno) e termina no no atual (cujo vizinho e `vizinho_cinza`).
    A aresta de fechamento tem timestamp `ts_aresta_retorno`.

    Timestamps das arestas do ciclo:
      - Para cada no intermediario n em caminho_ciclo[1:-1]:
            timestamp = caminho_ts[n]  (ts da aresta que o colocou no caminho)
      - Aresta de fechamento: ts_aresta_retorno
    """
    idx_inicio = caminho_pos[vizinho_cinza]

    if len(caminho_nos) - idx_inicio + 1 > MAX_CYCLE_LEN:
        return  # ciclo excessivamente longo — pula para economizar memoria

    caminho_ciclo = caminho_nos[idx_inicio:] + [vizinho_cinza]

    # caminho_ciclo[1:-1] sao os nos entre o inicio e o fim (exclusive)
    ts_arestas = [caminho_ts[n] for n in caminho_ciclo[1:-1]]
    ts_arestas.append(ts_aresta_retorno)

    # ts_arestas nunca sera vazio: sempre tem pelo menos ts_aresta_retorno
    duracao = max(ts_arestas) - min(ts_arestas)

    chave = (tuple(caminho_ciclo), duracao)
    if chave in vistos:
        return

    vistos.add(chave)
    ciclos.append({
        "caminho": caminho_ciclo,
        "duracao_segundos": duracao,
        "suspeito": duracao <= janela_segundos,
    })
