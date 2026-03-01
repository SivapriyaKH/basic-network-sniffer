from scapy.all import *

def packet_callback(packet):

    if packet.haslayer(IP):

        ip_layer = packet[IP]

        print("\n📡 Packet Captured!")
        print("Source IP:", ip_layer.src)
        print("Destination IP:", ip_layer.dst)
        print("Protocol Number:", ip_layer.proto)

        # Identify Protocol
        if packet.haslayer(TCP):
            print("Protocol: TCP")
        elif packet.haslayer(UDP):
            print("Protocol: UDP")
        elif packet.haslayer(ICMP):
            print("Protocol: ICMP")

        # Show Payload
        if packet.haslayer(Raw):
            print("Payload:", packet[Raw].load)

print("Starting Detailed Packet Sniffer...")
sniff(filter="ip", prn=packet_callback, count=10)
print("Sniffing Completed.")