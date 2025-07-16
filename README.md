# 🔐 Secure File Sharing with AES Encryption

A simple yet secure Flask web app for encrypted file uploads and downloads using AES-256 encryption.

## ✨ Features

- 📤 Upload files (encrypted with AES-256)
- 📥 Download files (decrypted on-the-fly)
- 🗑 Delete files
- 🌙 Dark mode toggle
- ✅ Upload notifications
- 🧾 File size & timestamp display

## 🔐 Encryption Details

- AES-256 in CBC mode with random IV
- Key stored securely via `.env`
- PKCS7 padding, decrypted files auto-served

## 🚀 Setup

```bash
git clone https://github.com/Slo-J42/FUTURE_CS_03
cd secure-file-share
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a .env file:
AES_KEY=your_64_char_hex_key_here

Run the app:
python app.py


📁 Folder Structure
uploads/ – stores encrypted files

decrypted/ – temporary decrypted files

templates/ – HTML frontend

crypto_utils.py – AES logic

app.py – Flask web app

## 🔐 Security
See SECURITY.md for full encryption and key handling details.
