# scripts/monitor_snort_log.py

import time

LOG_FILE = "/var/log/snort/alert"

def monitor():
    with open(LOG_FILE, "r") as file:
        file.seek(0, 2)  # Vai para o fim do arquivo
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.5)
                continue
            if "SQL" in line or "Injection" in line:
                print(f"[!] Alerta de possível SQLi: {line.strip()}")

if __name__ == "__main__":
    monitor()
