import pandas as pd
from flask import request

def csv_loader(UPLOAD_FOLDER):
    file = request.files['file']

    file_path = UPLOAD_FOLDER/file.filename
    file.save(file_path)

    df = pd.read_csv(file_path, sep='[;,]', engine='python')
    return file, df