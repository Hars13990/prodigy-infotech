def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char  # Leave spaces and punctuation unchanged
    return result

def decrypt(message, shift):
    return encrypt(message, -shift)

# Main program
print("Caesar Cipher Program")
choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
text = input("Enter your message: ")
shift = int(input("Enter the shift value: "))

if choice == 'e':
    encrypted_text = encrypt(text, shift)
    print("Encrypted message:", encrypted_text)
elif choice == 'd':
    decrypted_text = decrypt(text, shift)
    print("Decrypted message:", decrypted_text)
else:
    print("Invalid choice!")
