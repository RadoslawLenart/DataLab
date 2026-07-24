from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def pdf_generator(analyst, charts, describe):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate('static/reports/raport.pdf')

    elements = []

    elements.append(Paragraph("<b>Raport analizy danych</b>", styles["Heading1"]))
    elements.append(Paragraph(f"Nazwa pliku: {analyst['Nazwa_pliku']}", styles["Normal"]))
    elements.append(Paragraph(f"Liczba wierszy: {analyst['ilość_wierszy']}", styles["Normal"]))
    elements.append(Paragraph(f"Liczba kolumn: {analyst['ilość_kolumn']}", styles["Normal"]))
    elements.append(Paragraph(f"Kolumny: {analyst['Kolumny']}", styles["Normal"]))
    elements.append(Spacer(1, 15))

    for statistic, columns in describe.items():
        elements.append(Paragraph(statistic))
        elements.append(Spacer(1,10))
        for column, value in columns.items():
            elements.append(Paragraph(column, styles["Normal"]))
            value = str(value)
            elements.append(Paragraph(value, styles["Normal"]))
            elements.append(Spacer(1, 5))


    for chart in charts:
        elements.append(Image(chart))

    doc.build(elements)