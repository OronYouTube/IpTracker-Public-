#Tool Created By GhostEE#9999

import requests
import json
import whois
import os

clear = lambda: os.system('cls')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
pass

def lookup():
    args = input(bcolors.OKBLUE + "Enter IP: \n" + bcolors.ENDC)
    r = requests.get("http://ip-api.com/json/" + args)
    clear()
    parsed = json.loads(r.content)
    print("Lookup Complete: ")
    print(bcolors.WARNING + "IP: " + parsed["query"])
    print("Status: " + parsed["status"])
    print("ISP: " + parsed["isp"])
    print("ORG: " + parsed['org'])
    print("Region: " + parsed["region"])
    print("Country: " + parsed["country"])
    print("City: " + parsed["city"])
    print("Zip: " + parsed["zip"] + bcolors.ENDC)

    stayOpen()
pass

def tocheck():
    args = input(bcolors.OKBLUE + "Enter IP: \n" + bcolors.ENDC)
    clear()
    w = whois.whois(args)
    print("Target IP: " + args)
    print(w)

    stayOpen()
pass

def stayOpen():
    print("Press Enter To Continue...")
    input()
pass

def main():
    print("Choose the method: (1/2)")
    print("[1] IP Lookup")
    print("[2] Who Is")
    #print("[3] DDOS Attack")
    method = input()

    if method == '1':
        clear()
        lookup()
    elif method == '2':
        clear()
        tocheck()
    else:
        clear()
        print(bcolors.FAIL + "[Usage]: 1/2, Pleaes try again" + bcolors.ENDC)
        main()
    pass
pass
main()

stayOpen()