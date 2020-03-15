# -*- coding: utf-8 -*-
__author__ = '@D3R3LI'

import requests
import threading
import sys
import random
import time
import colorama

# UserAgent and subdomain list
USERAGENT = [agent.strip() for agent in open('/Users/x/useragents.txt')]
SUBDOMAIN = [sub.strip() for sub in open('/Users/x/subdomain-list.txt')]

say = 0 #Increase the domain in the subdomain list by 1 each time

def Subdomain_HTTP_Code_Scanner():
    global USERAGENT
    global SUBDOMAIN
    global say

    try:
        request = requests.get(SUBDOMAIN[say], headers={'User-Agent':random.choice(USERAGENT)}, timeout=8)
        status_code = request.status_code
        print("Site: "+str(SUBDOMAIN[say])+" - "+str(status_code)+ " || Referrer: "+str(request.history))

    except requests.exceptions.ConnectionError as conError:
        print(colorama.Fore.RED+"Error " + str(SUBDOMAIN[say])+colorama.Style.RESET_ALL)

    except requests.exceptions.Timeout as timeout:
        print(colorama.Fore.RED+"Error " + str(SUBDOMAIN[say])+colorama.Style.RESET_ALL)

    except requests.exceptions.SSLError as ssl:
        print(colorama.Fore.RED+"Error " + str(SUBDOMAIN[say])+colorama.Style.RESET_ALL)

    say +=1


# THREAD SECTION

thread = []

for i in range(len(SUBDOMAIN)):
    th = threading.Thread(target=Subdomain_HTTP_Code_Scanner)
    thread.append(th)
    th.start()
    time.sleep(0.2)

for thjoin in thread:
    thjoin.join()






