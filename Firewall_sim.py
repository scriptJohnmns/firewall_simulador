import random

CHECK_ICON = chr(10004)
BLOCK_ICON = chr(128502)

def generate_random_ip():
    return f"192.168.1.{random.randint(0, 20)}" #gera o octeto dos hosts que serão bloqueados

def check_firewall_rules(ip_adress, firewall_rules):
    return firewall_rules.get(ip_adress, f"allow | {CHECK_ICON}")

def main():
    
    print("| --------- FIREWALL SIMULATOR --------- |")

    firewall_rules = {
        #lista de ips para bloquear
        "192.168.1.2" : f"block | {BLOCK_ICON}",
        "192.168.1.5" : f"block | {BLOCK_ICON}",
        "192.168.1.9" : f"block | {BLOCK_ICON}",
        "192.168.1.13" : f"block | {BLOCK_ICON}",
        "192.168.1.18" : f"block | {BLOCK_ICON}"
    }

    for _ in range(15):
        ip_address = generate_random_ip()    
        action = check_firewall_rules(ip_address, firewall_rules)              
        print(f"IP: {ip_address} -> Action: {action}")
        

if __name__ == "__main__" :
    main()

    