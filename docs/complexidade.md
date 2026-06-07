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

**Estrutura:** DFS iterativa com pilha explicita. Tres estados por no:
- `BRANCO (0)` — nao visitado
- `CINZA (1)` — em progresso (esta na pilha de DFS atual)
- `PRETO (2)` — finalizado (todos os vizinhos processados)

**Complexidade de tempo:** O(V + E)  
Cada no transita exatamente uma vez por BRANCO -> CINZA -> PRETO.  
Cada aresta e examinada exatamente uma vez (cursor de indice por no na pilha).  
A deteccao de ciclo ao encontrar um vizinho CINZA e O(1) com o dict `caminho_pos`.  
A reconstrucao do caminho e O(L) onde L e o comprimento do ciclo — amortizado no total das arestas.

**Complexidade de espaco:** O(V)  
- `estado`: dicionario com V entradas
- `caminho_nos`: lista com no maximo V nos simultaneamente (profundidade da DFS)
- `caminho_pos`: dicionario espelho de `caminho_nos`, tambem O(V)
- `caminho_ts`: dicionario de timestamps do caminho atual, O(V)
- `pilha`: no maximo V frames simultaneamente

**Por que DFS iterativa (nao recursiva):**  
Python tem limite de recursao padrao de 1000 chamadas. Para `input_estresse.json`
com 50.000 nos, um caminho degenerado (lista encadeada) estouraria a pilha.
A implementacao iterativa com pilha explicita elimina esse risco sem depender de
`sys.setrecursionlimit`.

**Por que nao busca exaustiva:**  
Testar todos os caminhos possiveis seria O(V!) — inviavel para 50.000 nos.  
A DFS em O(V+E) e a unica abordagem adequada para o volume exigido.

**Calculo de duracao do ciclo:**  
Para o ciclo `[A, B, C, A]` com arestas A->B (ts=t1), B->C (ts=t2), C->A (ts=t3):  
`duracao = max(t1, t2, t3) - min(t1, t2, t3)`  
Autoloop `[A, A]`: apenas uma aresta, `duracao = 0`.

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
