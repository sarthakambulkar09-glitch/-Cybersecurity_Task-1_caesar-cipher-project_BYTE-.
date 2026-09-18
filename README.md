CYB_Task1_CaesarCipher_BYTE

A Python-based Caesar Cipher encryption and decryption tool created for Cybersecurity Internship Task 1.

Features

- Encrypts text using a configurable shift value
- Decrypts encrypted text
- Supports different shift values
- Preserves spaces, numbers, and special characters
- Includes brute-force auto-cracking
- Displays all possible Caesar Cipher shifts
- Works on Termux and standard Python environments

Technologies Used

- Python 3
- Termux
- GitHub

How to Run

Make sure Python 3 is installed.

python caesar_cipher.py

Example

Input

Enter text: hello world
Enter shift value: 3

Output

Encrypted: khoor zruog
Decrypted: hello world

Brute Force Example

For ciphertext:

khoor zruog

The program tests possible shifts from 1 to 25 and displays the resulting text.

Shift 1: jgnnq yqtnf
Shift 2: ifmmp xpsme
Shift 3: hello world

Project Structure

caesar-cipher-project/
├── caesar_cipher.py
├── README.md
├── sample_input.txt
├── sample_output.txt
└── screenshot.png

Task

Task 1 — Caesar Cipher (Text Encryption/Decryption)

This project demonstrates basic cryptography concepts including substitution, encryption, decryption, configurable keys, and brute-force analysis.
