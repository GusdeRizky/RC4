def key_scheduling(plaintext, key):
    # Initialize the state array S with values equal to the length of plaintext
    S = list(range(len(plaintext)))
    
    # Create key array K by repeating the key if necessary
    K = []
    for i in range(len(S)):
        K.append(int(key[i % len(key)]))
    
    # Permute the array S based on the key K
    j = 0
    for i in range(len(S)):
        j = (j + S[i] + K[i]) % len(S)
        S[i], S[j] = S[j], S[i]
        
    print(f"After KSA, state array S = {S}")
    print(f"Key array K = {K}")
    
    return S