import subprocess
import os

REPO_DIR = "../git-test"

def update_code():
    cwd = os.getcwd()
    os.chdir(REPO_DIR)

    subprocess.run(["git", "fetch"], check=True)
    result = subprocess.run(["git", "rev-list", "HEAD...origin/main", "--count"], capture_output=True, text=True)

    if result.stdout.strip() != "0":
        print("[+] Update found. Pulling latest version...")
        subprocess.run(["git", "reset", "--hard", "origin/main"], check=True)
        subprocess.run(["git", "clean", "-fd"], check=True)
    else:
        print("[+] Already up to date.")

    os.chdir(cwd)

update_code()
print("Updates pov lol")
