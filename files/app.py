from flask import Flask, render_template, request
from pathlib import Path
import pandas as pd

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

    df = pd.read_csv(file_path, sep='[;,]', engine='python')

    info = {
        'ilość_wierszy': df.shape[0],
        'ilość_kolumn': df.shape[1],
        'kolumny': list(df.columns)
    }

    missing = df.isnull().sum().to_dict()

    columns = []
    for column in info['kolumny']:
        columns.append(column)

    counter = 0
    status = None
    for column in missing.values():
        if column == 0:
            counter += 1
            if counter == (info['ilość_wierszy'] + 1) and df.duplicated().sum() == 0:
                status = 'Poprawny'
        else:
            status = 'Niepoprawny'
            break

    ananyst = {
        'Nazwa_pliku': file.filename,
        'Ilość_wierszy': {info['ilość_wierszy']},
        'ilość_kolumn': {info['ilość_kolumn']},
        'Kolumny': columns,
        'Brakujące_dane': missing,
        'Duplikaty': df.duplicated().sum(),
        'Analiza_statystyczna': df.describe(),
        'Status': status
    }


    return render_template('dashboard.html', ananyst=ananyst)


if __name__ == '__main__':
    app.run(debug=True)