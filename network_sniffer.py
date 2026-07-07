from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw


def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto_num = ip_layer.proto

        proto_name = {1: "ICMP", 6: "TCP", 17: "UDP"}.get(proto_num, f"Other({proto_num})")

        print("=" * 60)
        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")
        print(f"Protocol       : {proto_name}")

        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"Source Port    : {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
            print(f"Flags          : {tcp_layer.flags}")

        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"Source Port    : {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")

        elif ICMP in packet:
            icmp_layer = packet[ICMP]
            print(f"ICMP Type      : {icmp_layer.type}")
            print(f"ICMP Code      : {icmp_layer.code}")

        if Raw in packet:
            payload = packet[Raw].load
            try:
                printable_payload = payload[:50].decode(errors="replace")
            except Exception:
                printable_payload = str(payload[:50])
            print(f"Payload (50 bytes): {printable_payload}")

        print("=" * 60)
        print()


def main():
    print("Starting Network Sniffer...")
    print("Press Ctrl+C to stop.\n")
    sniff(prn=process_packet, store=False, count=0)


if __name__ == "__main__":
    main()
