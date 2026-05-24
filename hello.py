# ANSI Colors
CYAN = "\033[96m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

print(f"{GREEN}========================================{RESET}")
print(f"{CYAN}        🚢 Welcome Aboard 🚢{RESET}")
print(f"{GREEN}========================================{RESET}")

print(f"{YELLOW}Hello World!{RESET}")
print(f"{BLUE}Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}\n")

ship = rf"""
                         |\
                        /| \
                       /_|__\
                 ____/_____\____
                 \              /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

print(f"{CYAN}{ship}{RESET}")

print(f"{GREEN}System Ready ✔{RESET}")