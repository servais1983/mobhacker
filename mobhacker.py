#!/usr/bin/env python3

import argparse
from core import analyze, decompile, check
from core.utils import run_script_yaml

def main():
    parser = argparse.ArgumentParser(prog="mobhacker", description="Mobile Pentest CLI - Kali Linux")
    subparsers = parser.add_subparsers(dest="command")

    analyze_cmd = subparsers.add_parser("analyze")
    analyze_cmd.add_argument("apk")

    decompile_cmd = subparsers.add_parser("decompile")
    decompile_cmd.add_argument("apk")

    subparsers.add_parser("check")

    run_cmd = subparsers.add_parser("run")
    run_cmd.add_argument("file")

    args = parser.parse_args()

    if args.command == "analyze":
        analyze.run(args.apk)
    elif args.command == "decompile":
        decompile.run(args.apk)
    elif args.command == "check":
        check.run()
    elif args.command == "run":
        run_script_yaml(args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()