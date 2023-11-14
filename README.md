# Overview:
The encryption-decryption scheme named as “Ouroboros Scheme” which means as a never-ending cycle and begins where it ends and ends where it begins. In technical terms this scheme utilizes a reversed ASCII transformation method to secure plaintext. The process involves reversing the input text, inserting a secret key (numerical value), adjusting ASCII codes, and creating a mapping between the modified ASCII codes and the corresponding characters.

#Explanation:

2.1 Encryption Process:
The reversal of the plaintext adds an additional layer of complexity. The ASCII code transformation introduces variability, and the mapping ensures uniqueness, preventing information loss during encryption. This scheme is designed to handle repeating letters gracefully.

Program asks the user if he wants to perform Encryption or Decryption.
User Press 1 for Encryption:

 The user provides an input Plaintext.
 User enters the secret key (numerical value)
 The input Plaintext is then reversed using the reverse_text function.
 For each character in the reversed text:
    * The original ASCII code of the character is determined (e.g., k: 107).
    * The block size (secret key) is added to the original ASCII code to obtain the new ASCII code.
 If there are repeating letters, an index is appended to the new ASCII code to ensure uniqueness.
 The new ASCII codes are mapped to corresponding alphabet characters
 The encrypted text is formed by concatenating the mapped characters.

Example:
Plaintext: hulk
Secret Key: 2
Reversed String: kluh
Original ASCII Codes: k: 107, l: 108, u: 117, h: 104
New ASCII Codes: k: 107 + 2 = 109, l: 108 + 2 = 110, u: 117 + 2 = 119, h:
104 + 2 = 106
Alphabet Mapping:
109 = m
110 = n
119 = w
106 = j
Encrypted Text: mnwj

2.2 Decryption Process:
The decryption process involves reversing the text and restoring the original ASCII codes. The alphabet mapping facilitates the reconstruction of the original message.

Program asks the user if he wants to perform Encryption or Decryption.
User Press 2 for Decryption:

 The user provides an input Ciphertext.
 The input Ciphertext is reversed using the reverse_and_transform function.
 For each character in the reversed text:
 The original ASCII code of the character is determined (e.g., j: 106).
 The original ASCII code of each character is subtracted by the block size to obtain the new ASCII code.
 The new ASCII codes are mapped back to the corresponding alphabet characters
 The decrypted text is formed by concatenating the mapped characters.

Example:
Ciphertext: mnwj
Secret Key: 2
Reversed String: jwnm
Original ASCII Codes: j: 106, w: 119, n: 110, m: 109
New ASCII Codes: j: 104 - 2 = 102, w: 117 - 2 = 115, n: 108 - 2 = 106, m:
107 - 2 = 105
Alphabet Mapping:
j = 104
w = 117
n = 108
m = 107
Decrypted Text: hulk

#Analysis:

4.1 Strengths:
Reversal Technique: Enhances security by making patterns less predictable.
Variable Block Size: The scheme allows adjusting the block size for different security levels.

4.2 Weaknesses:
Block Size Dependency: Security relies on the secrecy of the block size; if known, it could compromise the encryption.
Mapping Complexity: For long texts, the alphabet mapping could become computationally expensive.
