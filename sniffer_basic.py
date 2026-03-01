from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

print("Starting Basic Packet Sniffer...")
sniff(count=10, prn=packet_callback)
print("Sniffing Completed.")