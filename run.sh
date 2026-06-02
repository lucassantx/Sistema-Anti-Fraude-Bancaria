#!/bin/bash
set -e

echo "Sistema Anti-Fraude Bancaria - Projeto 9"
echo "========================================="

echo ""
echo "[1/3] input basico..."
python src/main.py --input data/input_basico.json --output data/output_basico.json

echo "[2/3] input avancado..."
python src/main.py --input data/input_avancado.json --output data/output_avancado.json

echo "[3/3] input estresse..."
python src/main.py --input data/input_estresse.json --output data/output_estresse.json

echo ""
echo "Concluido. Outputs gerados em /data."