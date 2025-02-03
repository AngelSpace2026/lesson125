def hex_to_bin(hex_list):
    """Convert a list of hex values to a binary string."""
    return ''.join(f"{int(h, 16):08b}" for h in hex_list)

def find_duplicate(a, b):
    """Find duplicate values in a and b."""
    set_a = set(a)
    for hex_value in b:
        if hex_value in set_a:
            return hex_value
    return None

def compress_data(data):
    """Compress data by finding a duplicate and adding a compression flag."""
    a, b = data
    duplicate = find_duplicate(a, b)

    if duplicate:
        # Apply compression by reducing the length of the binary representation by 1 bit
        compressed_a = a
        compressed_b = b
        compression_bits = '0'  # 1 bit for compression
        compressed_length = 47  # After compression, length should be 47 bits
    else:
        # No compression
        compressed_a = a
        compressed_b = b
        compression_bits = '1'  # 1 bit for no compression
        compressed_length = 49  # No compression, length is 49 bits

    return compressed_a, compressed_b, compression_bits, compressed_length, duplicate

def decompress_data(compressed_data, compression_bits):
    """Decompress data based on the compression flag."""
    compressed_a, compressed_b = compressed_data

    # Decompress by removing the compression bit if present
    if compression_bits == '0':  # Was compressed, remove the flag
        decompressed_b = compressed_b
    else:
        decompressed_b = compressed_b

    return compressed_a, decompressed_b

def print_compressed_bits(d):
    """Print compressed bits."""
    print(f"Compressed data (f bits): {d} bits")

def print_original_data(data):
    """Print the original data."""
    a, b = data
    binary_a = hex_to_bin(a)
    binary_b = hex_to_bin(b)
    print("\nOriginal Data (e bits):")
    print("a (Binary):", binary_a)
    print("b (Binary):", binary_b)
    original_length = len(binary_a) + len(binary_b)
    print(f"Original Data Length (e bits): {original_length} bits")

# Get input from the user (space-separated hex values)
user_input_a = input("Enter the first hex list (e.g., '30 c9 57'): ")
user_input_b = input("Enter the second hex list (e.g., '44 ba ca'): ")

# Convert the space-separated input into lists
a = user_input_a.split()
b = user_input_b.split()

# Print the original binary data (e bits)
print_original_data((a, b))

# Compress the data
compressed_data = compress_data((a, b))
compressed_a, compressed_b, compression_bits, compressed_length, duplicate = compressed_data

# Print compressed binary data before and after adding the compression flag
print("\nCompressed Data (Before Flag):")
compressed_data_before_flag = hex_to_bin(compressed_a) + hex_to_bin(compressed_b)

# Modify the compressed data as requested: Add '0010001' at the front and use only 40 bits of the remaining data
compressed_data_modified = '0010001' + compressed_data_before_flag[:40]
print("Compressed Data (7 bits + 40 bits):")
print(compressed_data_modified)

# Add the compression flag (0 for compression, 1 for no compression)
compressed_bin_str_with_flag = compression_bits + compressed_data_modified
print("\nCompressed Data with Flag:")
print(compressed_bin_str_with_flag)

# Print only the compressed data after modification
print(f"\nFinal Compressed Data:")
print(compressed_data_modified)
print(len(compressed_data_modified))

# Decompress the data
decompressed_data = decompress_data((compressed_a, compressed_b), compression_bits)
print("\nDecompressed Data (Hex):")
print(decompressed_data)

# Print compressed data length (f bits)
print_compressed_bits(len(compressed_data_modified))