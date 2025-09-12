import os
print(os.getcwd())


from cryptography.fernet import Fernet

# Generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key saved to 'secret.key'")

# Load the key from file
def load_key():
    return open("secret.key", "rb").read()

# Encrypt message
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Decrypt message
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

# Main program
def main():
    choice = input("Encrypt or Decrypt (E/D)? ").upper()

    if choice == 'E':
        message = input("Enter message to encrypt: ")
        encrypted = encrypt_message(message)
        with open("encrypted.txt", "wb") as file:
            file.write(encrypted)
        print("Message encrypted and saved to 'encrypted.txt'")

    elif choice == 'D':
        with open("encrypted.txt", "rb") as file:
            encrypted = file.read()
        decrypted = decrypt_message(encrypted)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    # Generate key only once; comment this out after first run
    generate_key()

    main()
