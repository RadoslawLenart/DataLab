import matplotlib.pyplot as plt
import pandas as pd

def plot(df, columns):
    charts = []
    counter = 0
    for column in columns:
        if df[column].dtype == 'int64':
            data = df[column]

            plt.figure()
            plt.hist(data, rwidth=0.8)
            plt.title(f"Wykres dla {column}")

            counter += 1
            plt.savefig(f"static/images/Wykres{counter}.png")
            plt.close()

            path_for_flask = f"images/Wykres{counter}.png"
            charts.append(path_for_flask)
    return charts