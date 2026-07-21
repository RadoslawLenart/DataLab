from flask import Flask, render_template, request
from pathlib import Path
import pandas as pd
from charset_normalizer import from_path
import matplotlib

matplotlib.use("Agg")

from charts.plot_generator import plot
from services.csv_loader import csv_loader
from services.analyzer import analyzer
from services.cleaner import cleaner

app = Flask(__name__)

def folder():
    UPLOAD_FOLDER = Path('./uploads')
    UPLOAD_FOLDER.mkdir(exist_ok=True)
    return UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/uploads', methods=['GET', 'POST'])
def upload():
    global file
    global df
    UPLOAD_FOLDER = folder()
    file, df = csv_loader(UPLOAD_FOLDER)

    analyst, columns = analyzer(
        UPLOAD_FOLDER,
        file,
        df
    )
    charts = plot(df, columns)

    return render_template(
        'dashboard.html',
        analyst=analyst,
        charts=charts
    )


@app.route('/clean', methods=['GET', 'POST'])
def clean():
    UPLOAD_FOLDER = folder()
    file_path = UPLOAD_FOLDER / file.filename

    result = from_path(file_path).best()

    if result:
        encoding = result.encoding
    else:
        encoding = "utf-8"

    df = pd.read_csv(file_path, sep='[;,]', engine='python', encoding=encoding)

    df = cleaner(df)

    analyst, columns = analyzer(
        UPLOAD_FOLDER,
        file,
        df
    )
    charts = plot(df, columns)

    return render_template(
        'dashboard.html',
        analyst=analyst,
        charts=charts
    )


if __name__ == '__main__':
    app.run(debug=True)