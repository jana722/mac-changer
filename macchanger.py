#!/usr/bin/env python3
import subprocess
import re
import os

def print_banner():
    # Updated full title with "MAC CHANGER", all in blue
    title = [
        "\033[94m  ███╗   ███╗ █████╗  ██████╗      ██████╗ ██████╗ \033[0m",
        "\033[94m  ████╗ ████║██╔══██╗██╔════╝     ██╔════╝██╔═══██╗\033[0m",
        "\033[94m  ██╔████╔██║███████║██║  ███╗    ██║     ██║   ██║\033[0m",
        "\033[94m  ██║╚██╔╝██║██╔══██║██║   ██║    ██║     ██║   ██║\033[0m",
        "\033[94m  ██║ ╚═╝ ██║██║  ██║╚██████╔╝    ╚██████╗╚██████╔╝\033[0m",
        "\033[94m  ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚═════╝ \033[0m"
    ]

    box_top = "\033[91m┌" + "─" * 58 + "┐\033[0m"
    box_bottom = "\033[91m└" + "─" * 58 + "┘\033[0m"

    print(box_top)
    print("\033[91m│" + " " * 58 + "│\033[0m")
    for line in title:
        print(f"\033[91m│\033[0m {line.ljust(56)} \033[91m│\033[0m")
    print("\033[91m│" + " " * 58 + "│\033[0m")

    print("\033[94m│      Author: N. Janarthanan                               │\033[0m")
    print("\033[94m│      Purpose: Educational tool to spoof MAC address       │\033[0m")
    print("\033[94m│      Usage: Just run './macchanger.py' and follow prompts │\033[0m")
    print(box_bottom)

    print("\033[92m[*] This tool allows you to change your MAC address quickly")
    print("[*] Useful for privacy testing, penetration testing, or bypassing MAC filters")
    print("[*] Make sure to run this script with root privileges (sudo)\033[0m\n")

def get_input():
    interface = input("\033[92m[?] Enter interface (e.g. eth0, wlan0): \033[0m")
    mac = input("\033[92m[?] Enter new MAC address (e.g. 11:22:33:44:55:66): \033[0m")
    return interface, mac

def change_mac(interface, mac):
    print(f"\033[92m[+] Changing MAC address for {interface} to {mac}\033[0m")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])

def check_mac(interface, mac):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    re_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if re_result:
        current_mac = re_result.group(0)
        if current_mac.lower() == mac.lower():
            print(f"\033[92m[+] MAC address was successfully changed to {current_mac}\033[0m")
        else:
            print(f"\033[91m[-] MAC address did not change. Current MAC: {current_mac}\033[0m")
    else:
        print("\033[91m[-] Could not read MAC address from interface output.\033[0m")

# === Main ===
os.system("clear")
print_banner()
interface, mac = get_input()
change_mac(interface, mac)
check_mac(interface, mac)
