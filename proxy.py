import re
import requests
import time

def check_proxy(proxy):
    url = "http://www.google.com"
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    try:
        print(f"[CHECKING] {proxy}...")
        response = requests.get(url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            print(f"[VALID] {proxy}")
            return True
    except requests.RequestException:
        print(f"[INVALID] {proxy}")
    return False

def extract_proxies(input_file, output_file):
    valid_proxies = []
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
        total = len(lines)
        for index, line in enumerate(lines, start=1):
            match = re.match(r'([\d\.]+:\d+)', line)
            if match:
                proxy = match.group(1)
                print(f"[{index}/{total}] Testing {proxy}")
                if check_proxy(proxy):
                    valid_proxies.append(proxy)
                time.sleep(1)  # Hindari terlalu banyak request dalam waktu singkat
    
    with open(output_file, 'w') as outfile:
        for proxy in valid_proxies:
            outfile.write(proxy + '\n')
    
    print(f"\n✅ Hasil ekstraksi disimpan di {output_file}")

# Nama file input dan output
input_filename = 'proxy_list.txt'  # Ubah sesuai nama file yang berisi daftar proxy
output_filename = 'cleaned_proxies.txt'  # File hasil output

# Ekstraksi
extract_proxies(input_filename, output_filename)
