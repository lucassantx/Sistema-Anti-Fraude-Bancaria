# RF01 - Grafo Direcionado com Lista de Adjacencia
# Complexidade: O(1) insert | O(V+E) traverse

class Graph:

    def __init__(self):
        self._adj = {}

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