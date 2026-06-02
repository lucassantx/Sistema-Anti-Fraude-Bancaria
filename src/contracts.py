# =============================================================
# contracts.py — CONTRATO DE INTEGRACAO
# Nao alterar sem consenso do grupo.
# Commitar no dia 1, antes de qualquer logica.
# =============================================================

# ── Tipos base ────────────────────────────────────────────────
#
# Transaction: dict
#   { "de": str, "para": str, "valor": float, "timestamp": int }
#
# Account: str  (ex: "CPF001", "CNPJ001")
#
# Neighbor: tuple
#   (para: str, valor: float, timestamp: int)
#
# Cycle: dict
#   { "caminho": list[str], "duracao_segundos": int, "suspeito": bool }
#   - caminho: lista de nos, primeiro == ultimo  ex: ["A","B","C","A"]
#   - duracao_segundos: max(timestamp) - min(timestamp) das arestas do ciclo
#   - suspeito: True se duracao_segundos <= janela_suspeita_segundos
#
# Anomaly: dict
#   { "ip": str, "contas_associadas": list[str] }
#
# ── Interface do Grafo (graph.py — Dev 1) ────────────────────
#
# Instanciar: g = Graph()
#
# g.add_node(conta: str) -> None
#   Adiciona no. Idempotente: chamar 2x nao duplica.
#
# g.add_edge(de: str, para: str, valor: float, timestamp: int) -> None
#   Cria nos automaticamente se nao existirem.
#   Permite multiplas arestas entre o mesmo par.
#
# g.get_neighbors(conta: str) -> list[Neighbor]
#   Retorna lista de tuplas (para, valor, timestamp).
#   SEMPRE retorna list — nunca None, nunca lanca excecao.
#   Retorna [] se conta nao existir.
#
# g.get_all_nodes() -> list[str]
#   Retorna lista de todas as contas. Ordem nao garantida.
#
# ── Interface da DFS (dfs_cycle.py — Dev 2) ──────────────────
#
# detect_cycles(graph: Graph, janela_segundos: int) -> list[Cycle]
#   graph: instancia de Graph importada de graph.py
#   janela_segundos: limiar para marcar ciclo como suspeito
#   Retorna lista de Cycle dicts.
#   SEMPRE retorna list — nunca None, nunca lanca excecao.
#   Retorna [] se nao houver ciclos ou grafo for vazio.
#   Resultado DEVE ser ordenado por duracao_segundos ASC (output deterministico).
#
# ── Interface da Hash (hash_table.py — Dev 3) ────────────────
#
# Instanciar: ht = HashTable(size=1024)
#
# ht.insert(key: str, value: str) -> None
#   Insere value na lista encadeada do bucket de key.
#   Permite multiplos values para a mesma key.
#
# ht.get(key: str) -> list[str]
#   Retorna lista de values associados a key.
#   SEMPRE retorna list — nunca None, nunca lanca excecao.
#   Retorna [] se key nao existir.
#
# ht.get_anomalies() -> list[Anomaly]
#   Retorna Anomaly dicts para keys com 2+ values distintos.
#   Resultado DEVE ser ordenado por ip (str sort) — output deterministico.
#
# ── Interface do main.py (Dev 1) ─────────────────────────────
#
# Execucao:
#   python src/main.py --input <caminho> --output <caminho>
#
# Fluxo:
#   1. Ler e parsear input.json
#   2. Instanciar Graph(), popular com contas e transacoes
#   3. Instanciar HashTable(), popular com dispositivos
#   4. Chamar detect_cycles(graph, janela_suspeita_segundos)
#   5. Chamar ht.get_anomalies()
#   6. Gravar output.json com indent=2
#
# Em caso de erro: exit code 1 + mensagem no stderr. Nunca excecao crua.
