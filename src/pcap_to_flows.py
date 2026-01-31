from scapy.all import rdpcap, IP, TCP, UDP
import pandas as pd
from collections import defaultdict
from tqdm import tqdm

PCAP_FILE = "data/sample.pcap"
FLOW_TIMEOUT = 60  # seconds

flows = defaultdict(lambda: {
    "start_time": None,
    "end_time": None,
    "total_bytes": 0,
    "packet_count": 0
})

print("[+] Reading PCAP...")
packets = rdpcap(PCAP_FILE)

for pkt in tqdm(packets):
    if IP not in pkt:
        continue

    proto = None
    if TCP in pkt:
        proto = "TCP"
        sport = pkt[TCP].sport
        dport = pkt[TCP].dport
    elif UDP in pkt:
        proto = "UDP"
        sport = pkt[UDP].sport
        dport = pkt[UDP].dport
    else:
        continue

    src = pkt[IP].src
    dst = pkt[IP].dst
    timestamp = pkt.time
    size = len(pkt)

    flow_key = (src, dst, sport, dport, proto)

    flow = flows[flow_key]

    if flow["start_time"] is None:
        flow["start_time"] = timestamp

    flow["end_time"] = timestamp
    flow["total_bytes"] += size
    flow["packet_count"] += 1

print("[+] Converting flows to DataFrame...")

rows = []
for key, data in flows.items():
    src, dst, sport, dport, proto = key
    duration = data["end_time"] - data["start_time"]

    rows.append({
        "src_ip": src,
        "dst_ip": dst,
        "src_port": sport,
        "dst_port": dport,
        "protocol": proto,
        "duration_sec": round(duration, 2),
        "total_bytes": data["total_bytes"],
        "packet_count": data["packet_count"],
        "bytes_per_sec": round(data["total_bytes"] / max(duration, 1), 2)
    })

df = pd.DataFrame(rows)
df.to_csv("data/flows.csv", index=False)

print("[✓] Flow extraction complete!")
print(df.head())
