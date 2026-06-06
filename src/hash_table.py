# =============================================================
# hash_table.py — RF03
# Dev 3
# Tabela Hash com Encadeamento Aberto
# Complexidade: O(1) medio insert/get
# PROIBIDO: dict do Python como substituto da hash, qualquer lib externa
# =============================================================

# TODO Dev 3: implementar Node e HashTable conforme contracts.py


# =============================================================
# hash_table.py — RF03
# Dev 3
# Tabela Hash com Encadeamento Aberto
# Complexidade: O(1) medio insert/get
# PROIBIDO: dict do Python como substituto da hash, qualquer lib externa
# =============================================================

class Node:
    """No da lista encadeada dentro de cada bucket."""
    
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    
    def __init__(self, size: int = 1024):
        self._size = size
        self._buckets = [None] * size
    
    def _hash(self, key: str) -> int:
        return sum(ord(c) for c in key) % self._size
    
    def insert(self, key: str, value: str) -> None:
        bucket = self._hash(key)
        node = Node(key, value)
        node.next = self._buckets[bucket]
        self._buckets[bucket] = node
    
    def get(self, key: str) -> list:
        bucket = self._hash(key)
        current = self._buckets[bucket]
        values = []
        
        while current is not None:
            if current.key == key:
                values.append(current.value)
            current = current.next
        
        return values  # Retorna lista vazia [] se não encontrar
    
    def get_anomalies(self) -> list:
        anomalies = []
        
        for bucket in self._buckets:
            current = bucket
            ip_accounts = {}
            
            while current is not None:
                if current.key not in ip_accounts:
                    ip_accounts[current.key] = []
                ip_accounts[current.key].append(current.value)
                current = current.next
            
            for ip, accounts in ip_accounts.items():
                if len(accounts) >= 2:
                    # Remove duplicatas mantendo ordem
                    unique = []
                    for acc in accounts:
                        if acc not in unique:
                            unique.append(acc)
                    anomalies.append({
                        "ip": ip,
                        "contas_associadas": unique
                    })
        
        anomalies.sort(key=lambda x: x["ip"])
        return anomalies