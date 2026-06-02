# Justificativa de Complexidade — Projeto 9

## RF01 — Grafo com Lista de Adjacencia

**Estrutura:** dicionario Python onde cada chave e uma conta (str) e o valor e uma lista de tuplas `(para, valor, timestamp)`.

**add_node:** O(1)  
Acesso direto ao dicionario pelo CPF/CNPJ.

**add_edge:** O(1) amortizado  
Append na lista do no de origem.

**get_neighbors:** O(grau do no)  
No pior caso O(E) para um no hub com todas as arestas.

**Espaco:** O(V + E)  
V = numero de contas, E = numero de transacoes.

---

## RF02 — DFS para Deteccao de Ciclos

**Complexidade de tempo:** O(V + E)  
Cada no e visitado exatamente uma vez (transicao BRANCO -> CINZA -> PRETO).  
Cada aresta e examinada exatamente uma vez.

**Complexidade de espaco:** O(V)  
Dicionario de estados (V entradas) + pilha de recursao no pior caso O(V).

**Por que nao busca exaustiva:**  
Testar todos os caminhos possiveis seria O(V!) — inviavel para 50.000 nos.  
A DFS em O(V+E) e a unica abordagem adequada para o volume exigido.

---

## RF03 — Hash Table com Encadeamento

**Funcao de hash:** soma dos valores ASCII dos caracteres da key, modulo size.

**insert:** O(1) amortizado  
Hash da key em O(|key|), append na lista encadeada em O(1).

**get:** O(1) medio, O(n) pior caso  
Com size=1024 e distribuicao uniforme, colisoes sao raras.  
No pior caso (todas as keys no mesmo bucket): O(n).

**get_anomalies:** O(N + B)  
N = total de entradas, B = numero de buckets.

**Espaco:** O(N)  
N = numero de pares (ip, conta) inseridos.
