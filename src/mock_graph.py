# =============================================================
# mock_graph.py — SOMENTE para Dev 2 e Dev 3 usarem
# enquanto graph.py nao esta pronto.
# APAGAR antes da entrega final.
# =============================================================


class Graph:

    def __init__(self):
        self._adj = {
            "CPF001": [("CPF002", 1000.0, 0)],
            "CPF002": [("CPF003", 950.0, 3600)],
            "CPF003": [("CPF001", 900.0, 7200)],
            "CPF004": [],   # no isolado — sem arestas
            "CPF005": [("CPF001", 200.0, 99999)],  # aresta fora da janela
        }

    def add_node(self, conta: str) -> None:
        if conta not in self._adj:
            self._adj[conta] = []

    def add_edge(self, de: str, para: str, valor: float, timestamp: int) -> None:
        self.add_node(de)
        self.add_node(para)
        self._adj[de].append((para, valor, timestamp))

    def get_neighbors(self, conta: str) -> list:
        return self._adj.get(conta, [])

    def get_all_nodes(self) -> list:
        return list(self._adj.keys())
