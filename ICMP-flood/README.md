# flood-scapy
**A python script using scapy to send ICMP packets in a loop (ping flood)**

## Features
- Sends ICMP packets
- Customizable packet size (Bytes)
- Optional -N to unlock more size
- Stop with CTRL + C
- Colored with `colorama`

### Requirements
- python 3
- scapy
- colorama

---
`python3 -m pip install scapy colorama`
---
Run it with:
---
`sudo python3 icmp-flood.py IP BYTES -N(to unlock more size)`
