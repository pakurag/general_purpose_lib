import sys

def print_check(message, check_result, exit_on_failed = false):
    green = '\033[92m'
    red = '\033[91m'
    reset_color = '\033[0m'
    
    if check_result:
        print(f"{message} {green}Passed{reset_color}")
    else:
        print(f"{message} {red}Failed{reset_color}")
        if exit_on_failed:
            sys.exit(1)

def search_string_in_file(file_path, search_string):
    with open(file_path, 'r') as file:
        for line in file:
            if search_string in line:
                start_pos = line.find(search_string) + len(search_string)
                return line[start_pos:].strip()
    return None

def search_crc_in_file(file_path, search_string):
    value = search_string_in_file(file_path, search_string)
    
    if value and len(value) == 8 and all(c in '0123456789abcdefABCDEF' for c in value):
        return value
    return None
