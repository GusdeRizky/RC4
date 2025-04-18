from key_scheduling import key_scheduling
from prga import generate_keystream
from encryption import encrypt_decrypt

def rc4_encryption():
    print("==== RC4 ENCRYPTION ALGORITHM ====")
    plaintext = input("Masukan plaintext: ")
    key = input("Masukan Kunci Enkripsi(Angka): ")
    
    # Step 1: Key Scheduling Algorithm (KSA)
    print("\n==== Step 1: Key Scheduling Algorithm ====")
    S = key_scheduling(plaintext, key)
    
    # Step 2: Pseudo-Random Generation Algorithm (PRGA)
    print("\n==== Step 2: Pseudo-Random Generation Algorithm ====")
    keystream = generate_keystream(S, len(plaintext))
    
    # Step 3: Encryption using XOR
    print("\n==== Step 3: Enkripsi dengan XOR ====")
    ciphertext = encrypt_decrypt(plaintext, keystream)
    
    print("\n==== Hasil Enkripsi ====")
    print(f"Plaintext: {plaintext}")
    print(f"Kunci: {key}")
    print(f"Ciphertext: {ciphertext}")
    
    # Verify decryption works (RC4 is symmetric)
    print("\n==== Hasil Dekripsi ====")
    # Re-initialize the state array S for decryption
    S_decrypt = key_scheduling(ciphertext, key)
    keystream_decrypt = generate_keystream(S_decrypt, len(ciphertext))
    decrypted = encrypt_decrypt(ciphertext, keystream_decrypt)
    print(f"Dekripsi teks: {decrypted}")

if __name__ == "__main__":
    rc4_encryption()