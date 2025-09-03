python3 -c import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def shift_decode(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

def b16_decode(enc):
    plain = ""
    for i in range(0, len(enc), 2):
        # Get position in ALPHABET for each character
        c1 = ALPHABET.index(enc[i])
        c2 = ALPHABET.index(enc[i + 1])
        # Convert back to binary (4 bits each)
        binary = "{0:04b}{1:04b}".format(c1, c2)
        # Convert binary to character
        plain += chr(int(binary, 2))
    return plain

encrypted = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"

# Try all possible single character keys
for key in ALPHABET:
    dec = ""
    # First undo the shift cipher
    for i, c in enumerate(encrypted):
        dec += shift_decode(c, key)
    
    try:
        # Then try to decode the b16 encoding
        flag = b16_decode(dec)
        # If we can decode it and it looks like a flag
        if all(32 <= ord(c) <= 126 for c in flag):
            print(f"Key \"{key}\": {flag}")
    except:
        continue
