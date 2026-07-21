import pandas as pd
from flask import request
from charset_normalizer import from_path

def csv_loader(UPLOAD_FOLDER):
    file = request.files['file']

    file_path = UPLOAD_FOLDER/file.filename
    file.save(file_path)

    result = from_path(file_path).best()
    if result:
        encoding = result.encoding
    else:
        encoding = "utf-8"

    df = pd.read_csv(file_path, sep='[;,]', engine='python', encoding=encoding)
    return file, df