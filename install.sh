#!/bin/bash
echo "[*] Installation de MobHacker sur Kali..."

sudo apt update
sudo apt install -y python3 python3-pip jadx
pip3 install -r requirements.txt

echo "[+] Installation terminée. Utilisez : python3 mobhacker.py run scripts/android_scan.yaml"