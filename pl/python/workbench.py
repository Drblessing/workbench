import colorama
from colorama import Fore, Style

colorama.init(autoreset=False)
width = 40


pattern_1 = Fore.YELLOW + Style.BRIGHT + "*"
pattern_2 = (
    Fore.RED
    + Style.BRIGHT
    + "*"
    + Fore.GREEN
    + Style.BRIGHT
    + "*"
    + Fore.MAGENTA
    + Style.BRIGHT
    + "*"
)

print(" " * 10 + pattern_1)
print(" " * 9 + pattern_2)


# print("test".center(40))
# print("test 23q4123".center(40))
