from scapy.all import IP, ICMP, sniff
from colorama import Fore, init
from datetime import datetime
init(autoreset=True)
try:
    def _sniff(paquete):
        if IP in paquete and ICMP in paquete:
            ip_origuen=paquete[IP].src
            ip_destino=paquete[IP].dst
            tipo=paquete[ICMP].type
            datos=bytes(paquete[ICMP].payload)
            if tipo == 0:
                tipo_icmp="Echo Reply"
            elif tipo==8:
                tipo_icmp="Echo Request"
            else:
                tipo_icmp=f"ICMP tipo ({tipo})"
            try:
                texto=datos.decode('utf-8')
                texto_contenido=Fore.GREEN+f"Contenido legible: {texto}"
                
            except UnicodeDecodeError:
                texto=datos.hex()
                texto_contenido=Fore.RED+f"Contenido no legible (hex): {texto}"
                
            texto_imprimir=f"""
        [+]{datetime.now().strftime('%H:%M:%S')} | {ip_origuen} ---> {ip_destino}
            -{tipo_icmp}
            -{texto_contenido}
        """
            print(texto_imprimir)
    sniff(filter="icmp", prn=_sniff, store=0)
except KeyboardInterrupt:
    exit()
