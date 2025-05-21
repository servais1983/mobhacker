# MobHacker CLI

Pentest CLI pour applications mobiles (Android APK) – Kali Linux.

## ⚙️ Installation

```bash
chmod +x install.sh
./install.sh
```

## 🛠️ Commandes

* `analyze <apk>` : Analyse statique de l'APK
* `decompile <apk>` : Décompile avec JADX
* `check` : Recherche de patterns faibles (démo)
* `run <yaml>` : Exécute un scénario YAML

## 🚀 Exemple

```bash
python3 mobhacker.py run scripts/android_scan.yaml
```