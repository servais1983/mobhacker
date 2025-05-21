import zipfile
import re

def run(apk_path):
    print(f"[*] Analyse statique de {apk_path}...")

    try:
        with zipfile.ZipFile(apk_path, 'r') as apk:
            files = apk.namelist()
            if "AndroidManifest.xml" in files:
                print("[+] Manifest détecté")
            for f in files:
                if "api" in f.lower() or "token" in f.lower():
                    print(f"[!] Possible endpoint ou clé trouvée : {f}")
    except Exception as e:
        print(f"[!] Erreur analyse APK : {e}")