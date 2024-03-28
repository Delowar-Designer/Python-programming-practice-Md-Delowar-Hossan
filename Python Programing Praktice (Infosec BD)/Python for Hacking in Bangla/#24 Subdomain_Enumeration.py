#24 Subdomain_Enumeration
'''import requests
import sys

sub_list = open("wordlist2.txt").read()
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domains)

    except requests.ConnectionError:
        pass

    else:
        print("Valid domain: ", sub_domains)

        # Run the Code : python3 subdomain.py target_url'''

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <domain>")
    sys.exit(1)

domain = sys.argv[1]
sub_list = open("wordlist2.txt").read().splitlines()

for sub in sub_list:
    http_sub_domain = f"http://{sub}.{domain}"
    https_sub_domain = f"https://{sub}.{domain}"

    for url in (http_sub_domain, https_sub_domain):
        try:
            response = requests.get(url)

            if response.status_code < 400:
                print("Valid domain:", url)

        except requests.RequestException:
            pass
