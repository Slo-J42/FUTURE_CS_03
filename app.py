from flask import Flask, request, render_template, send_file, redirect, url_for, flash
import os
from datetime import datetime
from werkzeug.utils import secure_filename
from crypto_utils import encrypt_file, decrypt_file

app = Flask(__name__)
app.secret_key = 's3cr3t'  # Needed for session-based flash messages

UPLOAD_FOLDER = 'uploads'
DECRYPTED_FOLDER = 'decrypted'

# Create folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    """Render the file listing page with file metadata"""
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, filename)
        size = os.path.getsize(path)
        uploaded = datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M')
        files.append({'name': filename, 'size': size, 'date': uploaded})
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Encrypt and save uploaded file"""
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        encrypted = encrypt_file(file.read())
        with open(os.path.join(UPLOAD_FOLDER, filename), 'wb') as f:
            f.write(encrypted)
        flash(f"File '{filename}' uploaded successfully!", 'success')
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    """Decrypt and serve file to user"""
    path = os.path.join(UPLOAD_FOLDER, filename)
    with open(path, 'rb') as f:
        decrypted = decrypt_file(f.read())
    temp_path = os.path.join(DECRYPTED_FOLDER, filename)
    with open(temp_path, 'wb') as f:
        f.write(decrypted)
    return send_file(temp_path, as_attachment=True)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    """Delete file from uploads"""
    try:
        os.remove(os.path.join(UPLOAD_FOLDER, filename))
        flash(f"File '{filename}' deleted successfully.", 'info')
    except Exception:
        flash("Error deleting file.", 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
