# Wifi-Hacking-Script
Wifi hacking script for Raspberry Pi.
# NOTICE
## Script may not work propely on each try, I recommend to run it twice.

## How to use it
#### Things to have:
- Raspberry with aircrack-ng / Laptop with kali
- USB network adapter (could try without(on laptop), but raspberry pi have to have wifi module)
- SSH server on Raspberry
- Be in sudoers file / have root permissions

#### How to use it
First open code editor and edit:
Line 8 change BSSID to your target BSSID
Line 23 Same thing as in 8th line.
Line 41 Same.

Ok. Now your script is ready to start.
Save it on your raspberry.

From SSH server execute this script(with sudo)
If you don't do this you will be asked for sudo password.

After that you will be disconnected from SSH, because wpa_supplicant process will be killed.
If your Raspberry will not reboot in TWO or THREE minutes, reboot it manually ( like unplug it from power and plug it again )

After that you can try crack this with this command:
aircrack-ng -w wordlist.txt wpa2crack.cap

If it fails ( this command throws errors ) you have to run script again.

##### This should work

## Known bugs
1. Raspberry is not rebooting automatically after the script ends.
