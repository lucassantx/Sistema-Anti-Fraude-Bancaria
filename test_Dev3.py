# test_rapido.py
from src.hash_table import HashTable

print("Testando HashTable corrigida...")

ht = HashTable()

# Inserir dados
ht.insert("10.0.0.1", "CPF001")
ht.insert("10.0.0.1", "CPF002")
ht.insert("10.0.0.2", "CPF003")

# Teste 1: get em chave existente (ordem não importa)
result = ht.get("10.0.0.1")
print(f"get('10.0.0.1') = {result}")
assert set(result) == {"CPF001", "CPF002"}, f"ERRO: esperado CPF001 e CPF002, got {result}"
print("✅ Teste 1 passou")

# Teste 2: get em chave inexistente
result = ht.get("10.0.0.999")
print(f"get('10.0.0.999') = {result}")
assert result == [], f"ERRO: esperado [], got {result}"
print("✅ Teste 2 passou")

# Teste 3: anomalias (ordem das contas não importa)
anomalies = ht.get_anomalies()
print(f"get_anomalies() = {anomalies}")
assert anomalies[0]["ip"] == "10.0.0.1"
assert set(anomalies[0]["contas_associadas"]) == {"CPF001", "CPF002"}
print("✅ Teste 3 passou")

print("\n🎉 Todos os testes passaram! HashTable está correta!")