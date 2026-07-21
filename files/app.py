from flask import Flask, render_template
from pathlib import Path


import matplotlib
matplotlib.use("Agg")

from charts.plot_generator import plot
from services.csv_loader import csv_loader
from services.analyzer import analyzer

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

    UPLOAD_FOLDER = folder()
    file, df= csv_loader(UPLOAD_FOLDER)

    analyst, columns = analyzer(UPLOAD_FOLDER, file, df)
    charts = plot(df, columns)


    return render_template('dashboard.html', analyst=analyst, charts=charts)


if __name__ == '__main__':
    app.run(debug=True)