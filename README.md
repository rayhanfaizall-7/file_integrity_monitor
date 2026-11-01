# File Integrity Monitor (FIM)

A lightweight, Python-based File Integrity Monitor designed to track cryptographic states of critical files and instantly detect unauthorized modifications or tampering. 

I built this tool to better understand host-based intrusion detection systems (HIDS) and to ensure critical configuration files remain unmodified in secure environments.

---

## 🚀 Features
- **SHA-256 Hashing Engine:** Generates secure cryptographic fingerprints of target files.
- **Baseline Tracking:** Saves initial file states into a secure local baseline record (`baseline.txt`).
- **Tampering Alerts:** Automatically compares current file hashes against the stored baseline to spot even a single-byte alteration.
- **Efficient Chunk Reading:** Reads files in binary blocks (`4096 bytes`) to safely handle large files without exhausting system memory.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries Used:** 
  - `hashlib` (for SHA-256 cryptographic hashing)
  - `os` (for file path validation and system checks)

---

## ⚙️ How to Use It

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/file_integrity_monitor.git](https://github.com/rayhanfaizall-7/file_integrity_monitor.git)
   cd file_integrity_monitor