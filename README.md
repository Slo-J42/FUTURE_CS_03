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
git clone https://github.com/yourusername/secure-file-share.git
cd secure-file-share
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
