from flask import Flask, render_template, request, send_file
from pathlib import Path
import matplotlib

matplotlib.use("Agg")

from config import UPLOAD_FOLDER
from charts.plot_generator import plot
from services.csv_loader import csv_loader
from services.analyzer import analyzer
from services.cleaner import cleaner
from services.statistics import statistics
from services.pdf_generator import pdf_generator

folder = Path('uploads')
for file in folder.iterdir():
    if file.is_file():
        file.unlink()
folder = Path('static/images')
for file in folder.iterdir():
    if file.is_file():
        file.unlink()

app = Flask(__name__)


def generate_analysis(UPLOAD_FOLDER, file, df):
    analyst, columns = analyzer(
            UPLOAD_FOLDER,
            file,
            df
        )
    charts = plot(df, columns)
    describe = statistics(df)

    return analyst, charts, describe


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/uploads', methods=['GET', 'POST'])
def upload():

    df, file = csv_loader(UPLOAD_FOLDER, False)
    if df is None:
        return render_template('error.html', error=file)

    analyst, charts, describe = generate_analysis(UPLOAD_FOLDER, file, df)

    return render_template(
        'dashboard.html',
        analyst=analyst,
        charts=charts,
        describe=describe
    )


@app.route('/clean', methods=['POST'])
def clean():

    df, file = csv_loader(UPLOAD_FOLDER, True)
    if df is None:
        return render_template('error.html', error=file)
    df = cleaner(df)

    analyst, charts, describe = generate_analysis(UPLOAD_FOLDER, file, df)

    return render_template(
        'dashboard.html',
        analyst=analyst,
        charts=charts,
        describe=describe
    )
@app.route('/download', methods=['GET', 'POST'])
def download():
    df, file = csv_loader(UPLOAD_FOLDER, True)
    if df is None:
        return render_template('error.html', error=file)
    analyst, charts, describe = generate_analysis(UPLOAD_FOLDER, file, df)

    pdf_generator(analyst, charts, describe)

    pdf_folder = Path('static/reports')
    pdf_path = pdf_folder / 'raport.pdf'

    return send_file(pdf_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)