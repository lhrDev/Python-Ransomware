# Python-Ransomware
This Python script serves as a simple encryption and decryption tool for files within a directory. It offers functionalities to encrypt files using Fernet encryption and subsequently decrypt them with the provided key.
## 🚀Features
* <b>File Encryption:</b> The tool encrypts files within a specified directory using the Fernet encryption algorithm.
* <b>Key Delivery via Email:</b> It generates a decryption key and sends it securely via email to the specified recipient.
* <b>File Decryption:</b> Allows users to decrypt the encrypted files using the provided decryption key.
## 📝How to Use:
1. <b>Installation:</b> Ensure you have Python installed. Clone or download this repository.
2. <b>Setup:</b> Customize the excluded files list and provide your email credentials  <b>(gmail_user and gmail_password)</b> in the script. Also, set the recipient's email <b>(to)</b> to receive the key.
3. <b>Execution:</b> Run the script. It will encrypt the files within the directory, send the decryption key via email, and provide a simple GUI for decryption upon entering the correct key.

## ℹ️Usage Notes:
* Adjust the excluded files list to exclude specific files from encryption or decryption.
* Ensure to replace <b>gmail_user</b> with the Gmail address that will send the email. For security, enable "Less secure app access" or generate an App Password for the sending email in Google Account settings.
* Replace <b>gmail_password</b> with the corresponding password or App Password generated for the sending email.
* Set the <b>to</b> variable with the recipient's email address to receive the decryption key.

## 📋Requireents
* Python 3.x
* Required Python packages: <b>cryptography, tkinter, smtplib, email</b>

# ⚠️ IMPORTANT
This tool is intended for educational purposes and basic file encryption/decryption tasks. Ensure to use it responsibly and in compliance with applicable laws and regulations. The tool does not provide enterprise-grade security and is not suitable for securing highly sensitive or critical data.
