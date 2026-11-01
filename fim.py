import hashlib
import os

BASELINE_FILE = "baseline.txt"

def calculate_file_hash(file_path):
    """Calculates the SHA-256 cryptographic hash of a given file in chunks."""
    sha256_hash = hashlib.sha256()
    
    if not os.path.exists(file_path):
        print(f"[!] Error: File '{file_path}' not found.")
        return None

    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
            
    return sha256_hash.hexdigest()

def save_baseline(target_file):
    """Creates and saves the initial cryptographic baseline for the target file."""
    file_hash = calculate_file_hash(target_file)
    if file_hash:
        with open(BASELINE_FILE, "w") as f:
            f.write(f"{target_file}:{file_hash}")
        print(f"[+] Baseline successfully created and saved to '{BASELINE_FILE}'.")

def check_integrity(target_file):
    """Compares the current file hash against the saved baseline to detect tampering."""
    if not os.path.exists(BASELINE_FILE):
        print(f"[!] Error: No baseline found. Please create a baseline first.")
        return

    # Read the stored baseline
    baseline_data = {}
    with open(BASELINE_FILE, "r") as f:
        line = f.read().strip()
        if ":" in line:
            f_path, f_hash = line.split(":", 1)
            baseline_data[f_path] = f_hash

    if target_file not in baseline_data:
        print(f"[!] Error: '{target_file}' was not found in the baseline record.")
        return

    # Calculate current hash
    current_hash = calculate_file_hash(target_file)
    
    print(f"\n[*] Checking integrity for: {target_file}")
    if current_hash == baseline_data[target_file]:
        print(f"[+] STATUS: OK. No changes detected. File is secure.")
    else:
        print(f"[!] ALERT: FILE MODIFICATION DETECTED!")
        print(f"    Original Baseline Hash: {baseline_data[target_file]}")
        print(f"    Current File Hash:     {current_hash}")

if __name__ == "__main__":
    print("--- File Integrity Monitor (FIM) ---")
    print("1. Create Baseline")
    print("2. Check Integrity")
    
    choice = input("Select an option (1 or 2): ").strip()
    target_file = input("Enter target file name (e.g., test.txt): ").strip()
    
    if choice == "1":
        save_baseline(target_file)
    elif choice == "2":
        check_integrity(target_file)
    else:
        print("[!] Invalid choice. Please run the script again.")