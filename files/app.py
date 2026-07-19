from itertools import count

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

    print(f'Nazwa pliku:\n{file.filename}')
    print('Podstawowe informacje:')
    print(f'Ilość wierszy: {info['ilość_wierszy']}')
    print(f'ilość_kolumn: {info['ilość_kolumn']}')
    print('Kolumny:')
    for column in info['kolumny']:
        print(column)
    print()
    print('Brakujące dane:')
    for column in missing.items():
        print(f'{column[0]}: {column[1]}')
    print()
    print('Status:')
    counter = 0
    for column in missing.values():
        if column == 0:
            counter += 1
            if counter == info['ilość_wierszy'] + 1:
                print('Poprawny')
        else:
            print('Niepoprawny')
            break


    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)