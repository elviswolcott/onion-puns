#!/usr/bin python3

import os
from os import system
import random
from threading import Timer
import time

names = ["Abraham Linksys",
    "The LAN before time",
    "It burns when IP",
    "Friendly neighborhood spider-LAN",
    "Wi-Fight the inevitable",
    "Get off my LAN!",
    "Wu-Tang LAN",
    "Look ma, no wires!",
    "Hidden Network",
    "Free Wi-Fi",
    "LANdo Calrissian",
    "Keep it on the Download",
    "The password is 'Gullible'",
    "Every day I'm buffering",
    "Get off your phone",
    "Zelda a Linksys to the past",
    "Searching...",
    "No networks found",
    "Tell my Wi-Fi love her",
    "Not in range",
    "The LAN down under",
    "LAN of the free",
    "Wi-Fi so serious",
    "Alt F4 to continue",
    "One LAN to rule them all",
    "ObiWANkenobi",
    "slow wi-fi no dont call it that",
    "The lord of the pings"]

def setup():
	os.system("uci set wireless.@wifi-iface[0].ApCliEnable=0") #disable WiFi
	os.system("uci commit wireless") #commit changes
	os.system("wifi") #restart network
	print("Restarting network...")

def name(ssid, pswrd):
	os.system('uci set wireless.@wifi-iface[0].ssid="' + ssid + '"')
	os.system('uci set wireless.@wifi-iface[0].key="' + pswrd + '"')
	os.system("wifi") #restart network
	print("Restarting network...")
	
def loop():
	temp = random.choice(names)
	print("Setting to " + temp)
	name(temp, "PASSWORD") #name the network randomly
	time.sleep(30)
	loop()
	
print("Setting up...")
setup()

print("Looping")
loop()
	
setup()
