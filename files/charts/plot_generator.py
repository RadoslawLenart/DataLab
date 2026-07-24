import matplotlib.pyplot as plt

def plot(df, columns):
    charts = []
    counter = 0
    for column in columns:
        if df[column].dtype == 'int64' or df[column].dtype == 'float64':
            data = df[column]

            plt.figure()
            plt.hist(data, rwidth=0.8)
            plt.title(f"Wykres dla {column}")

            counter += 1
            plt.savefig(f"static/images/Wykres{counter}.png")
            plt.close()

            path_for_flask = f"static/images/Wykres{counter}.png"
            charts.append(path_for_flask)
    return charts