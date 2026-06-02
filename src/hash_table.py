# =============================================================
# hash_table.py — RF03
# Dev 3
# Tabela Hash com Encadeamento Aberto
# Complexidade: O(1) medio insert/get
# PROIBIDO: dict do Python como substituto da hash, qualquer lib externa
# =============================================================

# TODO Dev 3: implementar Node e HashTable conforme contracts.py


class Node:
    """No da lista encadeada dentro de cada bucket."""

    def __init__(self, key: str, value: str):
        # TODO: armazenar key, value e referencia para o proximo no
        pass


class HashTable:

    def __init__(self, size: int = 1024):
        # TODO: inicializar lista de buckets (cada posicao = None)
        # NAO usar dict do Python como estrutura principal
        pass

    def _hash(self, key: str) -> int:
        # TODO: funcao de hash — somar ord(c) para c in key, % self._size
        pass

    def insert(self, key: str, value: str) -> None:
        # TODO: calcular bucket, percorrer lista encadeada, adicionar Node
        pass

    def get(self, key: str) -> list:
        # TODO: retornar lista de values para a key
        # NUNCA retornar None. Retornar [] se key nao existir.
        pass

    def get_anomalies(self) -> list:
        # TODO: percorrer todos os buckets
        # Para cada key com 2+ values: criar dict Anomaly
        # Ordenar por ip (str sort) antes de retornar
        # Ver contracts.py para formato exato de Anomaly
        pass
