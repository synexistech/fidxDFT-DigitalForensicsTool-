import pytest
from dft.modules.pcap_analyzer import analyze_pcap
from scapy.all import wrpcap, Ether, IP, TCP

def test_analyze_pcap(tmp_path):
    # Create a dummy PCAP file
    pcap_file = tmp_path / "test.pcap"
    
    # Create a simple packet: Ether / IP / TCP
    pkt = Ether()/IP(src="192.168.1.1", dst="192.168.1.2")/TCP(dport=80)
    wrpcap(str(pcap_file), [pkt])
    
    stats = analyze_pcap(str(pcap_file))
    
    assert stats is not None
    assert stats['packet_count'] == 1
    assert stats['src_ips']["192.168.1.1"] == 1
    assert stats['dst_ips']["192.168.1.2"] == 1
    assert stats['top_ports'][80] == 1
    assert stats['protocols']['TCP'] == 1

def test_analyze_pcap_file_not_found():
    stats = analyze_pcap("non_existent.pcap")
    assert stats is None
