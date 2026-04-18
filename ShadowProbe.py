# ============================================
# Tool: ShadowProbe
# Author: Mr Joker
# GitHub: https://github.com/mrjoker-web
# ============================================

import requests
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import sys
import re

# Cores
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

results = []

def banner():
    print(f"""{CYAN}
===========================================
   ShadowProbe - HTTP Probe Tool
   Author: Mr Joker
   GitHub: https://github.com/mrjoker-web

EX: python shadowsub.py -t example.com -w wordlist.txt
===========================================
{RESET}""")

def extract_title(html):
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)
    return match.group(1).strip() if match else "No Title"

def check_url(url):
    for protocol in ["http://", "https://"]:
        full_url = protocol + url.strip()

        try:
            response = requests.get(full_url, timeout=3)

            title = extract_title(response.text)

            print(f"{GREEN}[{response.status_code}]{RESET} {full_url} {YELLOW}| {title}{RESET}")

            results.append({
                "url": full_url,
                "status": response.status_code,
                "title": title
            })
            return
        except:
            continue

def load_targets(file):
    try:
        with open(file, "r") as f:
            return f.read().splitlines()
    except:
        print(f"{RED}[-] Erro ao carregar ficheiro{RESET}")
        sys.exit()

def progress(current, total):
    percent = (current / total) * 100
    bar = int(percent // 2)
    sys.stdout.write(f"\r{CYAN}[{('#'*bar).ljust(50)}] {percent:.1f}%{RESET}")
    sys.stdout.flush()

def scan(targets, threads):
    print(f"{CYAN}\n[+] Probing targets...{RESET}\n")

    total = len(targets)
    count = 0

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(check_url, t) for t in targets]

        for f in futures:
            f.result()
            count += 1
            progress(count, total)

    print("\n")

def save_output():
    with open("live_hosts.txt", "w") as f:
        for r in results:
            f.write(f"{r['url']} [{r['status']}] - {r['title']}\n")

    with open("live_hosts.json", "w") as f:
        json.dump(results, f, indent=4)

    print(f"{GREEN}[+] Output guardado em live_hosts.txt e live_hosts.json{RESET}")

def main():
    parser = argparse.ArgumentParser(description="ShadowProbe - HTTP Probe Tool")
    parser.add_argument("-l", "--list", required=True, help="Lista de targets")
    parser.add_argument("--threads", type=int, default=50)

    args = parser.parse_args()

    banner()

    targets = load_targets(args.list)
    scan(targets, args.threads)
    save_output()

if __name__ == "__main__":
    main()
