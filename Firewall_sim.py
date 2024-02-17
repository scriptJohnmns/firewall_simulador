import random

check_icon = chr(10004)
block_icon = chr(128502)

def generate_random_ip():
    return f"192.168.1.{random.randint(0, 20)}"

def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return f"allow | {check_icon}"


def main():
    
    print("| --------- FIREWALL SIMULATOR --------- |")

    firewall_rules = {
        "192.168.1.1" : f"block | {block_icon}",
        "192.168.1.5" : f"block | {block_icon}",
        "192.168.1.9" : f"block | {block_icon}",
        "192.168.1.13" : f"block | {block_icon}",
        "192.168.1.18" : f"block | {block_icon}"
    }
    
    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0,9999)
        print(f"IP: {ip_address} -> Action: {action}")


if __name__ == "__main__" :
    main()

    