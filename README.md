# FidxDFT-Toolkit v1 (Digital ForensicsTool)

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey)

**FidxDFT-Toolkit** is a professional-grade, modular Digital Forensics Toolkit designed for efficient evidence analysis and artifact extraction. Built with Python, it offers both a robust Command Line Interface (CLI) and a modern, user-friendly GUI for forensic investigators.

## 🚀 Features

The toolkit is composed of six core modules, each designed to handle specific forensic tasks:

- **🔐 Hash Calculator**: 
  - verify file integrity using industry-standard algorithms: **MD5**, **SHA1**, and **SHA256**.
  - Batch processing capabilities for multiple files.

- **📸 EXIF Metadata Extractor**:
  - Extract hidden metadata from images (JPG, TIFF, WAV).
  - Retrieves GPS coordinates, camera models, timestamps, and software information.

- **🌐 Browser History Parser**:
  - Analyze web browsing history from SQLite databases (Chrome/Firefox).
  - Extracts visited URLs, timestamps, and visit counts.

- **📡 PCAP Analyzer (Mini)**:
  - Parse packet capture files (.pcap) to analyze network traffic.
  - Extracts source/destination IPs, protocols, and payload data.

- **⛏️ File Carver**:
  - Recover deleted or fragmented files from raw disk images or binary files.
  - Supports signature-based recovery for **JPG** and **PNG** formats.

- **📅 Timeline Generator**:
  - Create comprehensive timelines of forensic events.
  - Exports data to **JSON** for programmatic use and **PDF** for professional reporting.

## 🛠️ Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python Package Manager)

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/synexistech/fidxDFT-DigitalForensicsTool-.git
   cd fidxDFT-DigitalForensicsTool-
   ```

2. **Create and activate a virtual environment (Recommended):**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Graphical User Interface (GUI)
The GUI provides an intuitive dashboard for accessing all modules.
```bash
python gui.py
```

### Command Line Interface (CLI)
(Coming soon in v1.1 - currently integrated via module scripts)

## 📂 Project Structure

```
fidxDFT-Toolkit/
├── assets/              # Static assets (icons, images)
├── dft/                 # Core package
│   ├── modules/         # Forensic modules (hash, exif, pcap, etc.)
│   └── __init__.py
├── docs/                # Documentation
├── tests/               # Unit tests (pytest)
├── gui.py               # Main GUI application entry point
├── requirements.txt     # Python dependencies
├── LICENSE              # MIT License
└── README.md            # Project documentation
```

## 🧪 Testing

Run the comprehensive test suite to ensure all modules are functioning correctly:
```bash
pytest
```

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a Pull Request. Ensure all new features are covered by unit tests.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**SynExisTech**
*Advancing Digital Forensics*
