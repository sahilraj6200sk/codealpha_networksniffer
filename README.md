# Basic Network Sniffer

A Python-based network packet sniffer built for the **CodeAlpha Cyber Security Internship - Task 1**.

## 📌 Description

This program captures live network traffic and displays useful information for each packet, including:

- Source and Destination IP addresses
- Protocol used (TCP, UDP, ICMP)
- Source and Destination ports (for TCP/UDP)
- TCP flags
- Payload data (first 50 bytes)

This helps understand how data flows through a network and the basic structure of network packets and protocols.

## 🛠 Technologies Used

- **Python 3**
- **Scapy** library for packet capturing
- **Kali Linux** (run inside a VM)

## ⚙️ Setup Instructions

1. Make sure Python 3 is installed (comes pre-installed on Kali Linux)
2. Install Scapy if not already available:
   ```bash
   sudo apt update
   sudo apt install python3-scapy -y
   ```

## ▶️ How to Run

1. Open a terminal
2. Navigate to the project folder:
   ```bash
   cd CodeAlpha_NetworkSniffer
   ```
3. Run the script with root privileges (required for packet sniffing):
   ```bash
   sudo python3 network_sniffer.py
   ```
4. The sniffer will start capturing live packets. Press `Ctrl+C` to stop.

## 📷 Sample Output

```
Source IP      : 10.0.2.15
Destination IP : 10.0.2.3
Protocol       : UDP
Source Port    : 35189
Destination Port: 53

Source IP      : 10.0.2.15
Destination IP : 57.144.49.32
Protocol       : TCP
Source Port    : 52022
Destination Port: 443
``



## ⚠️ Disclaimer

This tool is built for **educational purposes only**, as part of a cybersecurity internship task.
Only run this on networks/devices you own or have explicit permission to monitor.
Unauthorized packet sniffing on networks you don't own may be illegal.

## 🎓 What I Learned

- How network packets are structured (IP, TCP, UDP, ICMP layers)
- How to use Scapy to capture and analyze live network traffic
- The role of ports in identifying services (e.g., port 53 = DNS, port 443 = HTTPS)
- Basics of network protocols and how data flows between devices

---
**Internship:** CodeAlpha - Cyber Security Domain
**Task:** Task 1 - Basic Network Sniffer
