from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

UPLOAD = '/projects/07cb54a4-9729-4508-ad4f-95fc7891551c/Team Members/Dev Patel/deploy_template/'
app.config['UPLOAD_FOLDER'] = UPLOAD

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('download_file', name=filename))
    return render_template('main.html')

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")