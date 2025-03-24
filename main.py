from update_manager import update_code
from colorama import Fore

update_code()

print(Fore.MAGENTA + "Test Software" + Fore.WHITE)

name = input("What is your name: ")
print("Hello, " + name)
