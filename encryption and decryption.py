def encrypt_xor(data, key):
    encrypted_data = bytearray()
    for byte in data.encode():
        encrypted_data.append(byte ^ key)
    return encrypted_data

def decrypt_xor(encrypted_data, key):
    decrypted_data = bytearray()
    for byte in encrypted_data:
        decrypted_data.append(byte ^ key)
    return decrypted_data.decode()

def get_valid_key():
    while True:
        try:
            key = int(input("Enter the encryption key (0-255): "))
            if 0 <= key <= 255:
                return key
            else:
                print("Key must be between 0 and 255.")
        except ValueError:
            print("Invalid key input. Please enter a valid integer.")

def main():
    
    print("This program encrypts your input using XOR encryption and then decrypts it")
    print("Please enter the plaintext and the encryption key")

    plaintext = input("\nEnter the plaintext to encrypt: ")
    key = get_valid_key()

    encrypted = encrypt_xor(plaintext, key)
    print("\nEncrypted data:", encrypted)

    decrypted = decrypt_xor(encrypted, key)
    print("Decrypted data:", decrypted)


if __name__ == "__main__":
    main()
