# DFT User Guide

## Introduction
This guide provides step-by-step instructions on how to use the Digital Forensics Toolkit (DFT) for basic analysis tasks.

## Case Study: Suspicious Network Activity

**Scenario**: You have received a packet capture (`suspicious.pcap`) and a suspect image (`evidence.jpg`). You need to analyze them.

### Step 1: Verify Integrity
1. Open DFT (`python gui.py`).
2. Go to the **File Hash** tab.
3. Click **Select File** and choose `suspicious.pcap`.
4. Record the MD5 hash to ensure the file hasn't been tampered with.

### Step 2: Analyze Network Traffic
1. Go to the **PCAP Analyzer** tab.
2. Click **Select PCAP** and choose `suspicious.pcap`.
3. Review the "Top Source IPs" and "Top Ports".
4. Look for high traffic on unusual ports or connections to known bad IPs.
5. Click **Export CSV** to save the detailed packet list for further analysis in Excel.

### Step 3: Extract Metadata
1. Go to the **EXIF Extractor** tab.
2. Click **Select Image** and choose `evidence.jpg`.
3. Check for "GPSInfo" or "DateTimeOriginal". This can tell you where and when the photo was taken.

### Step 4: Generate Report
1. (Optional) If you analyzed browser history, go to the **Timeline** tab.
2. Click **Generate Timeline**.
3. Save the PDF report to present your findings.

## Troubleshooting
- **Scapy Error**: If you get an error loading PCAP files on Windows, ensure Npcap is installed with "WinPcap API-compatible mode" enabled.
- **Database Locked**: If parsing browser history fails, make sure the browser is closed, or copy the `History` file to a temporary location first.
