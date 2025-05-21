import os

def run(apk_path):
    print(f"[*] Décompilation de {apk_path} avec JADX...")
    os.system(f"jadx {apk_path} -d decompiled_app")
    print("[+] Décompilation terminée. Résultat dans le dossier 'decompiled_app'")