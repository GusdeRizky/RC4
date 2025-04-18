def generate_keystream(S, plaintext_length):
    i = 0
    j = 0
    keystream = []
    
    # Generate keystream bytes equal to the length of plaintext
    for byte in range(plaintext_length):
        i = (i + 1) % len(S)
        j = (j + S[i]) % len(S)
        
        # Swap S[i] and S[j]
        S[i], S[j] = S[j], S[i]
        
        # Generate keystream byte
        t = (S[i] + S[j]) % len(S)
        keystream_byte = S[t]
        keystream.append(keystream_byte)
    
    print(f"Generated keystream: {keystream}")
    return keystream