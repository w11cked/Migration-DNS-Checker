import socket
import pandas as pd
from colorama import Fore, Style, init

init(autoreset=True)

# Datei mit Domains
dateiname = "domains.txt"

# IP-Adressen
new_ip = "172.30.30.1"  # Neuer DNS
old_ip = "10.10.0.7"  # Alter DNS

# Ergebnisliste initialisieren
results = []

# Domains aus Datei lesen
with open(dateiname, "r") as f:
    domains = [line.strip() for line in f if line.strip() and not line.startswith("#")]
print(f"{Fore.RED}----------------------------------------------------------------------------------------------")
print(f"{Fore.GREEN}DNS-Checker by w11cked")
print(f"{Fore.RED}----------------------------------------------------------------------------------------------")
print(f"{Fore.MAGENTA}Python 3.12 + Pandas 2.2.3")
print(f"{Fore.RED}----------------------------------------------------------------------------------------------")
# DNS-Abfrage durchführen
for domain in domains:
    try:
        ip_address = socket.gethostbyname(domain)

        if ip_address == new_ip:
            status_text = "OK - IST UMGEZOGEN"
            color = Fore.GREEN
        elif ip_address == old_ip:
            status_text = "ALT - NOCH ALTER DNS"
            color = Fore.YELLOW
        else:
            status_text = "EXTERN - UNBEKANNTE IP"
            color = Fore.RED
    except socket.gaierror:
        ip_address = "Nicht gefunden"
        status_text = "FEHLER - DOMAIN NICHT GEFUNDEN"
        color = Fore.MAGENTA

    # Ergebnisse
    results.append([domain, ip_address, status_text])
    print(f"{Fore.CYAN}{domain:<40}{Fore.WHITE}{ip_address:<20}{color}{status_text}")

# speichern
df = pd.DataFrame(results, columns=["Domain", "DNS IP", "Status"])
df.to_csv("dns_check_results.csv", index=False)
print(f"{Fore.RED}----------------------------------------------------------------------------------------------")
print(f"\n{Fore.GREEN}Ergebnisse gespeichert in dns_check_results.csv")
print(f"{Fore.RED}----------------------------------------------------------------------------------------------")