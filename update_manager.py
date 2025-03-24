import subprocess
import os
from colorama import Fore

REPO_DIR = "../git-test"

def update_code():
    cwd = os.getcwd()
    os.chdir(REPO_DIR)

    subprocess.run(["git", "fetch"], check=True)
    result = subprocess.run(["git", "rev-list", "HEAD...origin/main", "--count"], capture_output=True, text=True)

    if result.stdout.strip() != "0":
        print(f"{Fore.GREEN}[+]{Fore.WHITE} Update found. Pulling latest version...")
        subprocess.run(["git", "reset", "--hard", "origin/main"], check=True)
        subprocess.run(["git", "clean", "-fd"], check=True)
    else:
        print(f"{Fore.GREEN}[+]{Fore.WHITE} Already up to date.")

    os.chdir(cwd)
