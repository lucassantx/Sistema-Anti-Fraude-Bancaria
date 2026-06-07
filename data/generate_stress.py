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
    return {
        "contas": ["CPF001", "CPF002", "CPF003", "CPF004", "CPF005"],
        "transacoes": [
            {"de": "CPF001", "para": "CPF002", "valor": 1000.0, "timestamp": 0},
            {"de": "CPF002", "para": "CPF003", "valor": 950.0, "timestamp": 3600},
            {"de": "CPF003", "para": "CPF001", "valor": 900.0, "timestamp": 7200},
            {"de": "CPF004", "para": "CPF005", "valor": 500.0, "timestamp": 100},
        ],
        "dispositivos": [
            {"ip": "10.0.0.1", "conta": "CPF001"},
            {"ip": "10.0.0.1", "conta": "CPF002"},
            {"ip": "10.0.0.2", "conta": "CPF003"},
        ],
        "janela_suspeita_segundos": 86400
    }


def gerar_avancado():
    return {
        "contas": [f"CPF{i:03d}" for i in range(1, 21)],
        "transacoes": [
            # Ciclo dentro da janela
            {"de": "CPF001", "para": "CPF002", "valor": 100.0, "timestamp": 1000},
            {"de": "CPF002", "para": "CPF003", "valor": 100.0, "timestamp": 2000},
            {"de": "CPF003", "para": "CPF001", "valor": 100.0, "timestamp": 3000},
            # Ciclo fora da janela
            {"de": "CPF004", "para": "CPF005", "valor": 100.0, "timestamp": 0},
            {"de": "CPF005", "para": "CPF006", "valor": 100.0, "timestamp": 50000},
            {"de": "CPF006", "para": "CPF004", "valor": 100.0, "timestamp": 100000},
            # Ciclo longo
            {"de": "CPF007", "para": "CPF008", "valor": 100.0, "timestamp": 10000},
            {"de": "CPF008", "para": "CPF009", "valor": 100.0, "timestamp": 11000},
            {"de": "CPF009", "para": "CPF010", "valor": 100.0, "timestamp": 12000},
            {"de": "CPF010", "para": "CPF011", "valor": 100.0, "timestamp": 13000},
            {"de": "CPF011", "para": "CPF007", "valor": 100.0, "timestamp": 14000},
            # Autoloop
            {"de": "CPF012", "para": "CPF012", "valor": 50.0, "timestamp": 5000},
            # Transacao duplicada
            {"de": "CPF013", "para": "CPF014", "valor": 200.0, "timestamp": 15000},
            {"de": "CPF013", "para": "CPF014", "valor": 200.0, "timestamp": 15000},
        ],
        "dispositivos": [
            {"ip": "192.168.1.100", "conta": "CPF001"},
            {"ip": "192.168.1.100", "conta": "CPF002"},
            {"ip": "192.168.1.100", "conta": "CPF003"},
            {"ip": "192.168.1.100", "conta": "CPF004"},
            {"ip": "192.168.1.100", "conta": "CPF005"},
            {"ip": "10.0.0.1", "conta": "CPF006"},
            {"ip": "10.0.0.2", "conta": "CPF007"},
            {"ip": "172.16.0.1", "conta": "CPF008"},
            {"ip": "172.16.0.1", "conta": "CPF009"},
        ],
        "janela_suspeita_segundos": 86400
    }


def gerar_estresse():
    N_CONTAS = 50_000
    N_TRANS = 200_000
    N_CICLOS = 100
    
    contas = [f"CPF{i:05d}" for i in range(N_CONTAS)]
    
    transacoes = []
    for _ in range(N_TRANS):
        transacoes.append({
            "de": random.choice(contas),
            "para": random.choice(contas),
            "valor": round(random.uniform(10, 50000), 2),
            "timestamp": random.randint(0, 86400 * 365)
        })
    
    for i in range(N_CICLOS):
        a = f"CPF{i:05d}"
        b = f"CPF{i+1:05d}"
        c = f"CPF{i+2:05d}"
        t = i * 100
        transacoes += [
            {"de": a, "para": b, "valor": 500.0, "timestamp": t},
            {"de": b, "para": c, "valor": 490.0, "timestamp": t + 30},
            {"de": c, "para": a, "valor": 480.0, "timestamp": t + 60},
        ]
    
    dispositivos = []
    for i in range(N_CONTAS):
        dispositivos.append({
            "ip": f"192.168.{i//256}.{i%256}",
            "conta": f"CPF{i:05d}"
        })
    
    for i in range(50):
        ip = f"10.0.{i//256}.{i%256}"
        for j in range(5):
            idx = i * 5 + j + 1000
            if idx < N_CONTAS:
                dispositivos.append({"ip": ip, "conta": f"CPF{idx:05d}"})
    
    return {
        "contas": contas,
        "transacoes": transacoes,
        "dispositivos": dispositivos,
        "janela_suspeita_segundos": 86400
    }


if __name__ == "__main__":
    with open("data/input_basico.json", "w") as f:
        json.dump(gerar_basico(), f, indent=2)
    with open("data/input_avancado.json", "w") as f:
        json.dump(gerar_avancado(), f, indent=2)
    with open("data/input_estresse.json", "w") as f:
        json.dump(gerar_estresse(), f, indent=2)
    
    print("3 inputs gerados com sucesso.")
    print("- data/input_basico.json")
    print("- data/input_avancado.json")
    print("- data/input_estresse.json")