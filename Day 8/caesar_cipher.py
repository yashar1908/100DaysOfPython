alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ");
message = input("Enter the message to encrypt/decrypt: ").lower();
shift = int(input("Enter the number of letters to shift the message by: "));

def encrypt(message, shift):
    encrypted = "";
    for char in message:
        index = alphabet.index(char);
        new_index = index + shift;
        if new_index > 25:
            new_index -= 26;
        char = alphabet[new_index];
        encrypted += char;
    print("The encrypted message is:", encrypted);

def decrypt(message, shift):
    decrypted = "";
    for char in message:
        index = alphabet.index(char);
        new_index = index - shift;
        if new_index < 0:
            new_index += 26;
        char = alphabet[new_index];
        decrypted += char;
    print("The decrypted message is:", decrypted);

if direction == 'encrypt':
    encrypt(message, shift);
    
elif direction == 'decrypt':
    decrypt(message, shift);

