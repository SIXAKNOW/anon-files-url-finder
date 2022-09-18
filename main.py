import requests
import random
import time
import os

print("Anonfiles url finder by https://github.com/BasedGamer01")

def get():
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"

    string = upper + lower + nums
    length = 10

    var = "".join(random.sample(string, length))

    url = f"https://api.anonfiles.com/v2/file/{var}/info"
    r = requests.get(url)
    code = r.status_code
    if code == 404:
        print(f"[NOT WORKING] {url}")
    elif code == 200:
        cwd = os.getcwd()
        print(f"[WORKING] {url}")
        print(f"Saved url at {cwd} in working.txt")
        with open("working.txt", "a") as o:
            o.write(f"[WORKING] {url}\n")
    else:
        print(f"[ERROR] {url}")
        print(r.status_code)
def menu():

    dir_list = os.listdir()
    cwd = os.getcwd()
    if "working.txt" not in dir_list:
        print(f"working.txt not in in {cwd}, making now")
        with open("working.txt", "w"):
            pass
    else:
        pass

    use_time = input("Use delay? y/n:  ").lower()
    if use_time == "y":
        delay = input("Delay seconds: ")
        amount = input("How many to scrape: ")
        for n in range(int(amount)):
            time.sleep(int(delay))
            get()
    elif use_time == "n":
        amount = input("Amount to scrape: ")
        for n in range(int(amount)):
            get()
    else:
        print("Invalid input, try again")
        menu()
menu()
