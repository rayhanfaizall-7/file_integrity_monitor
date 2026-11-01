import hashlib
import os

def calculate_file_hash(file_path):
    """Calculates the SHA-256 cryptographic hash of a given file."""
    sha256_hash = hashlib.sha256()
    
    if not os.path.exists(file_path):
        print(f"[!] Error: File '{file_path}' not found.")
        return None

    # Read the file in binary chunks to handle files of any size efficiently
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
            
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    print("[*] File Integrity Monitor (FIM) Initialized.")
    target_file = input("Enter the path of the file to monitor (e.g., test.txt): ").strip()
    
    file_hash = calculate_file_hash(target_file)
    if file_hash:
        print(f"[+] SHA-256 Baseline Hash for '{target_file}':")
        print(f"    {file_hash}")