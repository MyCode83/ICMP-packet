# ICMP Sniffer
![Scapy](https://img.shields.io/badge/dependency-Scapy-green?logo=python&logoColor=white)


This script uses **Scapy** to capture ICMP (ping) packets on the network and displays:
- Source and destination IP
- ICMP type (Echo Request / Echo Reply / Others)
- Payload content (UTF-8 if readable, or hex otherwise)

## Requirements

- Python 3.10+
- [Scapy](https://scapy.net/)
- [Colorama](https://pypi.org/project/colorama/)

Install dependencies:


`pip install scapy colorama`
## Disclaimer

This project is intended **for educational and research purposes only**.  
The author is **not responsible** for any misuse of this code.  
Sniffing network traffic without proper authorization may be **illegal** in your country.  
Use this tool only in environments where you have **explicit permission** (e.g., your own network or lab setups).


Press CTRL + C to stop.
