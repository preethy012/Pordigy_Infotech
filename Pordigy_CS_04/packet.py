from scapy.layers.inet import IP, TCP, UDP
from scapy.packet import Raw
from scapy.sendrecv import sniff
from datetime import datetime


def packet_callback(packet):
    print("\n" + "="*50)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
    if TCP in packet:
        tcp_layer = packet[TCP]
        print("Protocol: TCP")
        print(f"Source Port: {tcp_layer.sport}")
        print(f"Destination Port: {tcp_layer.dport}")
    elif UDP in packet:
        udp_layer = packet[UDP]
        print("Protocol: UDP")
        print(f"Source Port: {udp_layer.sport}")
        print(f"Destination Port: {udp_layer.dport}")
    if Raw in packet:
        payload = packet[Raw].load
        try:
            decoded = payload.decode('utf-8', errors='replace')
            print(f"Payload (decoded):\n{decoded}")
        except:
            print(f"Payload (raw): {payload}")
def main():
    print("DISCLAIMER")
    print( "=" * 20)
    print('''This script is intended for educational and authorized testing purposes only.
Do NOT use this tool to capture or inspect network traffic on systems or networks
you do not own or do not have explicit permission to monitor.
Unauthorized use of this tool may violate privacy laws and terms of service,
and could result in legal consequences.
By using this script, you agree to use it responsibly and ethically.
Use at your own risk''')
    print("\n" + "=" * 50)
    print("Starting Packet Sniffer... Press Ctrl+C to stop.\n")
    sniff(prn=packet_callback, store=0)
if __name__ == "__main__":
    main()
