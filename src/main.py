import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from graph import Graph
from dfs_cycle import detect_cycles
from hash_table import HashTable


def load_input(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: arquivo nao encontrado: {path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Erro: JSON invalido: {e}", file=sys.stderr)
        sys.exit(1)


def build_graph(data: dict) -> Graph:
    g = Graph()
    for conta in data.get("contas", []):
        g.add_node(conta)
    for t in data.get("transacoes", []):
        # ignorar campos extras como "_comentario" ou "_edge_case"
        if "de" in t and "para" in t:
            g.add_edge(t["de"], t["para"], float(t["valor"]), int(t["timestamp"]))
    return g


def build_hash(data: dict) -> HashTable:
    ht = HashTable()
    for d in data.get("dispositivos", []):
        ht.insert(d["ip"], d["conta"])
    return ht


def build_output(cycles: list, anomalies: list) -> dict:
    return {
        "ciclos_detectados": cycles,
        "anomalias_dispositivo": anomalies
    }


def save_output(output: dict, path: str) -> None:
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
    except OSError as e:
        print(f"Erro ao gravar output: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Sistema Anti-Fraude Bancaria")
    parser.add_argument("--input",  required=True, help="Caminho do input.json")
    parser.add_argument("--output", required=True, help="Caminho do output.json")
    args = parser.parse_args()

    data      = load_input(args.input)
    graph     = build_graph(data)
    ht        = build_hash(data)
    cycles    = detect_cycles(graph, data["janela_suspeita_segundos"])
    anomalies = ht.get_anomalies()
    output    = build_output(cycles, anomalies)
    save_output(output, args.output)

    print(f"Concluido: {args.output}")


if __name__ == "__main__":
    main()