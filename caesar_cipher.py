def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def brute_force(ciphertext):
    print("\nBrute Force Results:\n")

    for shift in range(1, 26):
        candidate = decrypt(ciphertext, shift)
        print(f"Shift {shift:2}: {candidate}")


def main():
    print("=== Caesar Cipher Tool ===")

    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))

    encrypted = encrypt(text, shift)
    decrypted = decrypt(encrypted, shift)

    print("\nEncrypted:", encrypted)
    print("Decrypted:", decrypted)

    choice = input("\nRun brute-force auto-cracker? (y/n): ")

    if choice.lower() == "y":
        brute_force(encrypted)


if __name__ == "__main__":
    main()
