import sublist3r
import requests
from bs4 import BeautifulSoup
import random
from time import sleep
import multiprocessing

def banner():
    global colors

    print(f"""{random.choice(colors)}

  ██████  █    ██  ▄▄▄▄        █████▒██▓ ███▄    █ ▓█████▄ ▓█████  ██▀███  
▒██    ▒  ██  ▓██▒▓█████▄    ▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▓██  ▒██░▒██▒ ▄██   ▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
  ▒   ██▒▓▓█  ░██░▒██░█▀     ░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▒▒█████▓ ░▓█  ▀█▓   ░▒█░   ░██░▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▒▓███▀▒    ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░░░▒░ ░ ░ ▒░▒   ░     ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
░  ░  ░   ░░░ ░ ░  ░    ░     ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░    ░     ░░   ░ 
      ░     ░      ░                 ░           ░    ░       ░  ░   ░     
                        ░                           ░                      
\033[0m""")

def sublist3r_service(domain):
    subdomains = sublist3r.main(domain=domain, threads=40, savefile=None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)
    return subdomains


def crt_service(domain):
    response = requests.get(f'https://crt.sh/?q={domain}')
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('tr')

    subs = []

    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 6:
            domain = cells[4].text.strip()
            if domain not in subs:
                subs.append(domain)
                
    del subs[0]
    return subs



def run_services(domain):

    global is_loading

    sublister = sublist3r_service(domain)
    crt = crt_service(domain)

    all_subs = sublister + crt

    #is_loading = False
    print('<================RESULT================>')
    return list(set(all_subs))



def loading():
    global is_loading

    frames = ['    ','O   ','OO  ', 'OOO ', 'OOOO']

    while is_loading:
        for frame in frames:
            if is_loading == False: break
            print('↳ Loading('+frame+')', end='\r')
            sleep(0.2)
    



if __name__ == '__main__':

    colors = ["\33[91m","\33[94m","\033[32m","\033[93m","\033[0;35m","\033[36m"]
    is_loading = True

    banner()

    domain = input('Enter Domain Name: ')
    print()

    prc = multiprocessing.Process(target=loading)
    prc.daemon = True
    prc.start()

    sub_domains = run_services(domain)

    list_to_str = '\n'.join(map(str, sub_domains))

    print('\n', list_to_str)

    open(domain+'.txt', 'w').write(list_to_str)




