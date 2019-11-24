# encrypt.py
# Main code to encrypt a plaintext file.

from crypto import encrypt_file
BLOCK_SIZE = 16

e = 0   # replace by e from the recipient's public key
n = 0   # replace by n from the recipient's public key

encrypt_file("decrypted2.txt", "ciphertext.txt", e, n, BLOCK_SIZE, None)


