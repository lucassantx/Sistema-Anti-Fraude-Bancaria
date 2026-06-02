# =============================================================
# graph.py — RF01
# Dev 1
# Grafo Direcionado com Lista de Adjacencia
# Complexidade: O(1) insert | O(V+E) traverse
# PROIBIDO: collections.defaultdict, networkx ou qualquer lib externa
# =============================================================

# TODO Dev 1: implementar a classe Graph conforme contracts.py


class Graph:

    def __init__(self):
        # TODO: inicializar estrutura interna (dict puro, sem defaultdict)
        pass

    def add_node(self, conta: str) -> None:
        # TODO: adicionar no. Idempotente.
        pass

    def add_edge(self, de: str, para: str, valor: float, timestamp: int) -> None:
        # TODO: criar nos se nao existirem, adicionar aresta
        pass

    def get_neighbors(self, conta: str) -> list:
        # TODO: retornar list de tuplas (para, valor, timestamp)
        # NUNCA retornar None. Retornar [] se conta nao existir.
        pass

    def get_all_nodes(self) -> list:
        # TODO: retornar lista de todas as contas
        pass
