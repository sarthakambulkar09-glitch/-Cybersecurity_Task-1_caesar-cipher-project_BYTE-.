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
    print("\n=== Auto-Cracker ===")

    for shift in range(1, 26):
        candidate = decrypt(ciphertext, shift)
        print(f"Shift {shift:2}: {candidate}")


def main():
    print("=== Caesar Cipher Tool ===")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Auto-Crack")

    choice = input("\nChoose option (1/2/3): ")

    if choice == "1":
        text = input("Enter plaintext: ")
        shift = int(input("Enter shift value: "))

        print("\nCiphertext:", encrypt(text, shift))

    elif choice == "2":
        text = input("Enter ciphertext: ")
        shift = int(input("Enter shift value: "))

        print("\nPlaintext:", decrypt(text, shift))

    elif choice == "3":
        text = input("Enter ciphertext: ")
        brute_force(text)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
