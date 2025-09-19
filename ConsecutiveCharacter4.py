# encode bigrams

def encode_bigrams(s):
    # Chunk the string in pairs of characters (The last one can be a single character)
    chunks = [s[i:i+2] for i in range(0, len(s), 2)]
    
    output = []
    curr = None
    count = 0

    for chunk in chunks:
        if chunk == curr:
            count += 1
        else:
            if curr is not None:
                output.append(f"{curr}{count}")
            curr = chunk
            count = 1
    
    if curr is not None:
        output.append(f"{curr}{count}")

    return ''.join(output)