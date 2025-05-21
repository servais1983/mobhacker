import yaml
from core import analyze, decompile, check

def run_script_yaml(path):
    print(f"[*] Chargement du scénario : {path}")
    with open(path, "r") as f:
        data = yaml.safe_load(f)

    apk = data.get("apk", "")

    for step in data.get("steps", []):
        if step == "analyze":
            analyze.run(apk)
        elif step == "decompile":
            decompile.run(apk)
        elif step == "check":
            check.run()
        else:
            print(f"[!] Étape inconnue : {step}")