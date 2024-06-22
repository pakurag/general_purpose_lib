import sys

def print_check(message, check_result, exit_on_failed):
    green = '\033[92m'
    red = '\033[91m'
    reset = '\033[0m'
    
    if check_result:
        print(f"{message} {green}Passed{reset}")
    else:
        print(f"{message} {red}Failed{reset}")
        if exit_on_failed:
            sys.exit(1)
