from scapy.all import rdpcap, IP, TCP, UDP
from collections import Counter
import os
from dft.utils.logger import logger
import pandas as pd

def analyze_pcap(pcap_path):
    """
    Analyzes a PCAP file to extract summary statistics.

    Args:
        pcap_path (str): Path to the .pcap file.

    Returns:
        dict: A dictionary containing:
            - 'packet_count': Total number of packets.
            - 'src_ips': Counter of source IPs.
            - 'dst_ips': Counter of destination IPs.
            - 'top_ports': Counter of destination ports.
            - 'protocols': Counter of protocols (TCP/UDP).
            - 'dataframe_data': List of dicts for DataFrame creation.
    """
    if not os.path.isfile(pcap_path):
        logger.error(f"File not found: {pcap_path}")
        return None

    try:
        packets = rdpcap(pcap_path)
        logger.info(f"Loaded {len(packets)} packets from {pcap_path}")

        stats = {
            'packet_count': len(packets),
            'src_ips': Counter(),
            'dst_ips': Counter(),
            'top_ports': Counter(),
            'protocols': Counter(),
            'dataframe_data': []
        }

        for pkt in packets:
            pkt_info = {'time': float(pkt.time), 'src': None, 'dst': None, 'proto': None, 'sport': None, 'dport': None}
            
            if IP in pkt:
                stats['src_ips'][pkt[IP].src] += 1
                stats['dst_ips'][pkt[IP].dst] += 1
                pkt_info['src'] = pkt[IP].src
                pkt_info['dst'] = pkt[IP].dst
                pkt_info['proto'] = pkt[IP].proto

            if TCP in pkt:
                stats['top_ports'][pkt[TCP].dport] += 1
                stats['protocols']['TCP'] += 1
                pkt_info['sport'] = pkt[TCP].sport
                pkt_info['dport'] = pkt[TCP].dport
            elif UDP in pkt:
                stats['top_ports'][pkt[UDP].dport] += 1
                stats['protocols']['UDP'] += 1
                pkt_info['sport'] = pkt[UDP].sport
                pkt_info['dport'] = pkt[UDP].dport
            
            stats['dataframe_data'].append(pkt_info)

        logger.info(f"Analysis complete for {pcap_path}")
        return stats

    except Exception as e:
        logger.error(f"Error analyzing PCAP {pcap_path}: {e}")
        return None

def export_pcap_csv(stats, output_path):
    """
    Exports PCAP analysis data to CSV.
    """
    if not stats or 'dataframe_data' not in stats:
        return False
    
    try:
        df = pd.DataFrame(stats['dataframe_data'])
        df.to_csv(output_path, index=False)
        logger.info(f"PCAP data exported to {output_path}")
        return True
    except Exception as e:
        logger.error(f"Error exporting PCAP CSV: {e}")
        return False
