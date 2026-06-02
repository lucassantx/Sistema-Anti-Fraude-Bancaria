# =============================================================
# main.py — CLI principal
# Dev 1
# Orquestra todos os modulos. Le input.json, gera output.json.
# Uso: python src/main.py --input <caminho> --output <caminho>
# =============================================================

import argparse
import json
import sys
import os

# TODO Dev 1: trocar mock_graph por graph quando pronto
sys.path.insert(0, os.path.dirname(__file__))
from mock_graph import Graph       # <- substituir por: from graph import Graph
from dfs_cycle import detect_cycles
from hash_table import HashTable


def load_input(path: str) -> dict:
    # TODO Dev 1: ler e parsear input.json
    # Em caso de erro: print para stderr e sys.exit(1)
    pass


def build_graph(data: dict) -> Graph:
    # TODO Dev 1: instanciar Graph, popular com contas e transacoes
    pass


def build_hash(data: dict) -> HashTable:
    # TODO Dev 1: instanciar HashTable, popular com dispositivos
    pass


def build_output(cycles: list, anomalies: list) -> dict:
    # TODO Dev 1: montar dict de saida conforme formato em contracts.py
    pass


def save_output(output: dict, path: str) -> None:
    # TODO Dev 1: gravar output.json com indent=2
    pass


def main():
    parser = argparse.ArgumentParser(description="Sistema Anti-Fraude Bancaria")
    parser.add_argument("--input",  required=True, help="Caminho do input.json")
    parser.add_argument("--output", required=True, help="Caminho do output.json")
    args = parser.parse_args()

    try:
        data      = load_input(args.input)
        graph     = build_graph(data)
        ht        = build_hash(data)
        cycles    = detect_cycles(graph, data["janela_suspeita_segundos"])
        anomalies = ht.get_anomalies()
        output    = build_output(cycles, anomalies)
        save_output(output, args.output)
        print(f"Output gerado: {args.output}")
    except Exception as e:
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
