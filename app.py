

from flask import Flask, render_template, request, send_file, flash, redirect
import os
import io
from crypto import encrypt_data, decrypt_data

app = Flask(__name__)
app.secret_key = "super_secret_session_key" # Pour les messages flash
UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect('/')
    
    file = request.files['file']
    if file.filename == '':
        return redirect('/')

    # Lire le contenu, le chiffrer et l'enregistrer
    file_data = file.read()
    encrypted_content = encrypt_data(file_data)
    
    with open(os.path.join(UPLOAD_FOLDER, file.filename + ".enc"), "wb") as f:
        f.write(encrypted_content)
    
    flash(f"Fichier '{file.filename}' chiffré et sauvegardé !")
    return redirect('/')

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    
    with open(file_path, "rb") as f:
        encrypted_data = f.read()
    
    decrypted_content = decrypt_data(encrypted_data)
    
    if decrypted_content is None:
        return "Erreur de déchiffrement", 403

    # On renvoie le fichier déchiffré au navigateur sans le stocker sur le disque
    original_name = filename.replace(".enc", "")
    return send_file(
        io.BytesIO(decrypted_content),
        download_name=original_name,
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)
