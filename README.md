# Sistema Anti-Fraude Bancaria — Projeto 9

> Engenharia de Software — Estruturas de Dados & Algoritmos

## Membros

| Dev | GitHub |
|-----|--------|
| Dev 1 | @— |
| Dev 2 | @— |
| Dev 3 | @— |

## Projeto escolhido

**Projeto 9 — Sistema Anti-Fraude Bancaria**  
Detecta lavagem de dinheiro identificando ciclos financeiros fechados em um grafo direcionado de transacoes bancarias.

## Estruturas implementadas manualmente

| RF | Estrutura | Arquivo | Complexidade |
|----|-----------|---------|--------------|
| RF01 | Grafo Direcionado (Lista de Adjacencia) | `src/graph.py` | O(1) insert · O(V+E) traverse |
| RF02 | DFS com estados BRANCO/CINZA/PRETO | `src/dfs_cycle.py` | O(V+E) |
| RF03 | Hash Table com Encadeamento Aberto | `src/hash_table.py` | O(1) medio |

> Nenhuma biblioteca de alto nivel foi utilizada nas estruturas principais.

## Como executar

```bash
# 1. Gerar os arquivos de teste
python data/generate_stress.py

# 2. Rodar todos os cenarios
bash run.sh

# 3. Ou rodar individualmente
python src/main.py --input data/input_basico.json   --output data/output_basico.json
python src/main.py --input data/input_avancado.json --output data/output_avancado.json
python src/main.py --input data/input_estresse.json --output data/output_estresse.json
```

**Requisitos:** Python 3.8+ · Sem dependencias externas para execucao.

## Estrutura do repositorio

```
antifraude/
├── src/
│   ├── contracts.py       # Contrato de integracao (nao alterar sem consenso)
│   ├── graph.py           # RF01 — Grafo
│   ├── dfs_cycle.py       # RF02 — DFS
│   ├── hash_table.py      # RF03 — Hash
│   └── main.py            # CLI principal
├── data/
│   ├── input_basico.json
│   ├── input_avancado.json
│   ├── input_estresse.json
│   └── generate_stress.py
├── docs/
│   └── complexidade.md
├── run.sh
└── README.md
```

## Documentacao tecnica

Ver [`docs/complexidade.md`](docs/complexidade.md) para justificativa de complexidade assintotica de cada estrutura.
