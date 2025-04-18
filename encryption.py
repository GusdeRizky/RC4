def encrypt_decrypt(text, keystream):
    result = []
    result_binary = []
    
    # Convert text characters to binary ASCII representation
    text_binary = []
    for char in text:
        # Get ASCII value and convert to 8-bit binary
        ascii_val = ord(char)
        binary = format(ascii_val, '08b')
        text_binary.append(binary)
    
    print("\nText to binary conversion:")
    for i, char in enumerate(text):
        print(f"{char}: {text_binary[i]}")
    
    # Convert keystream numbers to binary representation
    keystream_binary = []
    for k in keystream:
        binary = format(k, '08b')
        keystream_binary.append(binary)
    
    print("\nKeystream to binary conversion:")
    for i, k in enumerate(keystream):
        print(f"{k}: {keystream_binary[i]}")
    
    # Perform XOR operation between text and keystream bytes
    print("\nXOR Operations:")
    for i in range(len(text)):
        # Get binary representations
        text_bin = text_binary[i]
        key_bin = keystream_binary[i]
        
        # Perform XOR operation bit by bit
        result_bin = ""
        for bit_idx in range(len(text_bin)):
            # XOR: 1⊕1=0, 0⊕0=0, 1⊕0=1, 0⊕1=1
            bit_result = '0' if text_bin[bit_idx] == key_bin[bit_idx] else '1'
            result_bin += bit_result
        
        result_binary.append(result_bin)
        
        # Convert the binary result back to ASCII character
        decimal_value = int(result_bin, 2)
        result_char = chr(decimal_value)
        result.append(result_char)
        
        # Print details of the XOR operation
        print(f"{text[i]} ({text_bin}) XOR keystream ({key_bin}) = {result_bin} ({result_char})")
    
    return ''.join(result)