import os

def run():
    print("[*] Vérification de patterns dangereux (démo)...")
    if os.path.exists("decompiled_app"):
        for root, _, files in os.walk("decompiled_app"):
            for f in files:
                if f.endswith(".java") or f.endswith(".smali"):
                    path = os.path.join(root, f)
                    with open(path, errors='ignore') as file:
                        content = file.read()
                        if "Base64" in content or "SharedPreferences" in content:
                            print(f"[!] Stockage ou encodage faible détecté dans {path}")
    else:
        print("[!] Aucun dossier décompilé trouvé.")