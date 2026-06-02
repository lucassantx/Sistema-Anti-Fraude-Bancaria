#!/bin/bash
set -e

echo "================================================="
echo " Sistema Anti-Fraude Bancaria — Projeto 9"
echo "================================================="

echo ""
echo "[1/3] Rodando input basico..."
python src/main.py --input data/input_basico.json --output data/output_basico.json
echo "      -> data/output_basico.json gerado"

echo ""
echo "[2/3] Rodando input avancado..."
python src/main.py --input data/input_avancado.json --output data/output_avancado.json
echo "      -> data/output_avancado.json gerado"

echo ""
echo "[3/3] Rodando input estresse..."
python src/main.py --input data/input_estresse.json --output data/output_estresse.json
echo "      -> data/output_estresse.json gerado"

echo ""
echo "Concluido. Verifique os outputs em /data."
