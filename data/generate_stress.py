# =============================================================
# generate_stress.py — Dev 3
# Gera automaticamente os 3 arquivos de input.
# Uso: python data/generate_stress.py
# Bibliotecas permitidas: random, json (stdlib)
# =============================================================

import random
import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__))


def gerar_basico():
    """Ja existe como input_basico.json — nao sobrescrever."""
    print("input_basico.json: ja existe, pulando.")


def gerar_avancado():
    """Ja existe como input_avancado.json — nao sobrescrever."""
    print("input_avancado.json: ja existe, pulando.")


def gerar_estresse():
    """
    Meta do professor para o Projeto 9:
      - 50.000 contas
      - 200.000 transacoes
      - 100 ciclos fechados plantados propositalmente
    """
    N_CONTAS = 50_000
    N_TRANS  = 200_000
    N_CICLOS = 100

    print(f"Gerando input_estresse.json ({N_CONTAS} contas, {N_TRANS} transacoes)...")

    contas = [f"CPF{i:05d}" for i in range(N_CONTAS)]

    # Transacoes aleatorias
    transacoes = [
        {
            "de":        random.choice(contas),
            "para":      random.choice(contas),
            "valor":     round(random.uniform(10.0, 50000.0), 2),
            "timestamp": random.randint(0, 86400 * 365)
        }
        for _ in range(N_TRANS)
    ]

    # Plantar 100 ciclos fechados propositais (janela < 86400s)
    # Estes DEVEM ser detectados pelo sistema para validar o RF02
    for i in range(N_CICLOS):
        a = f"CPF{i:05d}"
        b = f"CPF{i + 1:05d}"
        c = f"CPF{i + 2:05d}"
        t = i * 200  # timestamps crescentes, todos dentro de 1 dia
        transacoes.append({"de": a, "para": b, "valor": 500.0,  "timestamp": t})
        transacoes.append({"de": b, "para": c, "valor": 490.0,  "timestamp": t + 60})
        transacoes.append({"de": c, "para": a, "valor": 480.0,  "timestamp": t + 120})

    # Dispositivos — 1 por conta + 50 IPs compartilhados para forcar anomalias
    dispositivos = [
        {"ip": f"192.168.{i // 256}.{i % 256}", "conta": f"CPF{i:05d}"}
        for i in range(N_CONTAS)
    ]
    for i in range(50):
        dispositivos.append({"ip": "10.0.0.1", "conta": f"CPF{i + 100:05d}"})

    data = {
        "contas":                    contas,
        "transacoes":                transacoes,
        "dispositivos":              dispositivos,
        "janela_suspeita_segundos":  86400
    }

    path = os.path.join(OUTPUT_DIR, "input_estresse.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    size_mb = os.path.getsize(path) / 1_000_000
    print(f"input_estresse.json gerado: {size_mb:.1f} MB")
    print(f"  {N_CICLOS} ciclos plantados — todos devem ser detectados pelo RF02.")


if __name__ == "__main__":
    gerar_basico()
    gerar_avancado()
    gerar_estresse()
    print("\nConcluido. Rode 'bash run.sh' para testar.")
