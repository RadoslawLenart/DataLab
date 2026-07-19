from flask import Flask, render_template, request
from pathlib import Path

app = Flask(__name__)

UPLOAD_FOLDER = Path('./uploads')
UPLOAD_FOLDER.mkdir(exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/uploads', methods=['GET', 'POST'])
def upload():

    file = request.files['file']

    file_path = UPLOAD_FOLDER/file.filename
    file.save(file_path)

    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)