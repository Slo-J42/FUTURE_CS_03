# 🔐 Security Overview – Secure File Sharing System

## 1. Encryption Method

- **Algorithm:** AES (Advanced Encryption Standard)
- **Mode:** CBC (Cipher Block Chaining)
- **Key Size:** 256 bits (32 bytes)
- **IV:** A new 16-byte random IV is generated per file and prepended to ciphertext
- **Padding:** PKCS7 padding is used to ensure block alignment

## 2. Key Handling

- **Key Source:** AES key is stored in a `.env` file as a hex string (64 characters = 32 bytes)
- **Environment Access:** Key is loaded securely using `python-dotenv`
- **Key Management Best Practices:**
  - `.env` is excluded from version control (`.gitignore`)
  - In production, keys should be stored in a secret manager or hardware vault
  - Rotate keys periodically and re-encrypt stored data accordingly

## 3. File Storage

- Encrypted files are saved in the `uploads/` folder
- On download, files are decrypted temporarily in `decrypted/` and served to the user
- Temporary decrypted files can be purged with a cleanup job or session logic

## 4. Authentication (To Be Added)

- Basic app does not include user login yet
- Suggested additions: Flask-Login, hashed passwords, per-user file access

## 5. Transport Security

- Current setup runs locally on HTTP
- In production, **always use HTTPS** (e.g., via NGINX reverse proxy or Flask SSL context)
