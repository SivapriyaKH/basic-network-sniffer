# 🛰️ Basic Network Sniffer using Python

## 📌 Description
This project captures and analyzes network packets using Python and Scapy.

It displays:
- Source IP
- Destination IP
- Protocol used
- Payload (if available)

## ⚙️ Technologies Used
- Python
- Scapy

## 📂 Files
- sniffer_basic.py → Basic packet capture
- sniffer_details.py → Detailed packet analysis

## 🚀 Installation

Install Scapy:

pip install scapy

Run as Administrator / Root.

## ▶️ Run

Basic Sniffer:
python sniffer_basic.py

Detailed Sniffer:
python sniffer_details.py

## 🧠 Learning Outcomes
- Packet structure understanding
- Network protocol basics
- Data flow analysis

## ⚠️ Note
Use only for educational purposes.

## 📤 Sample Output

### Basic Sniffer

Starting Basic Packet Sniffer...

Ether / IP / TCP 10.191.127.40 > 52.182.143.211
Ether / IPv6 / ICMPv6 Neighbor Discovery
Ether / IP / TCP 52.182.143.211 > 10.191.127.40

Sniffing Completed.

### Detailed Sniffer

📡 Packet Captured!
Source IP: 52.182.143.211
Destination IP: 10.191.127.40
Protocol: TCP

📡 Packet Captured!
Source IP: 10.191.127.215
Destination IP: 239.255.255.250
Protocol: UDP

Payload:
NOTIFY * HTTP/1.1
HOST: 239.255.255.250:1900
