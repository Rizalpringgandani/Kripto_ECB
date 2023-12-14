def xor_binary(bin_str1, bin_str2):
    """Perform XOR operation on two binary strings."""
    return ''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(bin_str1, bin_str2))

def left_shift(bin_str):
    """Perform left shift operation on a binary string."""
    return bin_str[1:] + bin_str[0]

def encrypt(plaintext_hex, key_bin):
    """Encrypt plaintext using the given key."""
    # Convert plaintext from hexadecimal to binary
    plaintext_bin = bin(int(plaintext_hex, 16))[2:]

    # Divide the plaintext into blocks of 4 bits
    blocks = [plaintext_bin[i:i+4] for i in range(0, len(plaintext_bin), 4)]

    # Perform XOR and left shift operations on each block
    encrypted_blocks = []
    for block in blocks:
        xor_result = xor_binary(block, key_bin)
        shifted_result = left_shift(xor_result)
        encrypted_blocks.append(shifted_result)

    # Convert the encrypted blocks back to hexadecimal
    encrypted_hex = ''.join(hex(int(block, 2))[2:] for block in encrypted_blocks)

    return encrypted_hex

# Example usage
print("Nama : Rizal Pringgandani")
print("NIM : 312110151")
plaintext_hex = input("Masukkan Plainteks\t:")
key_bin = input("Masukan Kunci\t:")

encrypted_result = encrypt(plaintext_hex, key_bin)
print("Encrypted Result:", encrypted_result)
