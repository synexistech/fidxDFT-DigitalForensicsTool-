# FidxDFT-Toolkit v1 (Digital ForensicsTool)

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Portfolio_Ready-d32f2f?style=for-the-badge)
![GUI](https://img.shields.io/badge/GUI-Tkinter-blue?style=for-the-badge)

**FidxDFT-Toolkit** is a professional-grade, modular Digital Forensics application built with Python. Designed with a "Cyber Red" aesthetic, it provides a comprehensive suite of tools for forensic analysis, including file integrity checking, metadata extraction, network packet analysis, and data recovery.

> **⚠️ EDUCATIONAL USE ONLY**: This tool is developed for educational purposes and portfolio demonstration. Do not use on unauthorized systems.

## 🚀 Features

*   **🔒 File Integrity**: Calculate MD5, SHA1, and SHA256 hashes to verify evidence integrity.
*   **📸 EXIF Extraction**: Reveal hidden metadata (GPS, timestamps, device info) from image files.
*   **🌐 Network Forensics**: Analyze `.pcap` files to identify top talkers, suspicious ports, and protocol distribution using `Scapy`.
*   **🕵️ Browser Forensics**: Parse and analyze Chrome/Edge history databases (SQLite) to reconstruct user activity.
*   **💾 File Carving**: Recover deleted images (JPG/PNG) from raw binary dumps using header/footer signature analysis.
*   **timeline Timeline Generation**: Correlate events into a chronological timeline and export professional PDF reports.
*   **💻 Modern GUI**: A dark-themed, responsive interface built with `Tkinter` and `ttk` styling.

## 🛠️ Skills Demonstrated

This project demonstrates proficiency in:
*   **Python Development**: Modular architecture, OOP, and type hinting.
*   **GUI Programming**: Building responsive desktop apps with `Tkinter`.
*   **Network Analysis**: Packet level analysis using `Scapy`.
*   **Database Management**: Interacting with SQLite databases for forensic data.
*   **File Systems**: Binary file handling and signature-based data recovery.
*   **Data Visualization**: Generating PDF reports with `ReportLab`.
*   **Software Engineering**: Unit testing (`pytest`), CI/CD (GitHub Actions), and documentation.

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/FidxDFT-Toolkit.git
    cd FidxDFT-Toolkit
    ```

2.  **Run the Setup Script (Windows):**
    Double-click `setup_and_run.bat` to automatically create a virtual environment, install dependencies, and launch the tool.

    *Alternatively, manual setup:*
    ```bash
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python gui.py
    ```

## 🖥️ Usage

1.  **Launch the Tool**: Run `gui.py`.
2.  **Select a Module**: Click on the tabs (HASH, EXIF, PCAP, etc.) to switch tools.
3.  **Load Evidence**: Use the "SELECT FILE" or "LOAD" buttons to import data.
4.  **Analyze & Export**: View results in the console panel and export findings to CSV or PDF.

## 📂 Project Structure

```
FidxDFT-Toolkit/
├── dft/
│   ├── modules/        # Core forensic modules (hash, exif, pcap, etc.)
│   └── utils/          # Helper functions and logging
├── assets/             # Sample evidence files for testing
├── docs/               # Documentation and user guides
├── tests/              # Unit tests (Pytest)
├── gui.py              # Main GUI Application
├── setup_and_run.bat   # Automated setup script
└── requirements.txt    # Project dependencies
```

## 🔮 Roadmap

- [ ] **Registry Analysis**: Module to parse Windows Registry hives.
- [ ] **Keyword Search**: Global search across loaded evidence.
- [ ] **Cloud Forensics**: API integration for cloud log analysis.
- [ ] **Dark/Light Toggle**: User-selectable themes.

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---
*Built by [Your Name] for Cybersecurity Portfolio.*
