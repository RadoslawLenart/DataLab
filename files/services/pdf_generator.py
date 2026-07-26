from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont, pdfmetrics
from pathlib import Path


def pdf_generator(analyst, charts, describe):
    BASE_DIR = Path(__file__).parent

    font_path = BASE_DIR / "fonts" / "DejaVuSans.ttf"

    pdfmetrics.registerFont(
        TTFont("DejaVu", str(font_path))
    )

    styles = getSampleStyleSheet()

    for style in styles.byName.values():
        style.fontName = "DejaVu"
    print(styles["Normal"].fontName)
    print(styles["Heading1"].fontName)


    doc = SimpleDocTemplate('static/reports/raport.pdf')

    elements = []

    elements.append(Paragraph("Raport analizy danych", styles["Heading1"]))
    elements.append(Paragraph(f"Nazwa pliku: {analyst['Nazwa_pliku']}", styles["Normal"]))
    elements.append(Paragraph(f"Liczba wierszy: {analyst['Ilość_wierszy']}", styles["Normal"]))
    elements.append(Paragraph(f"Liczba kolumn: {analyst['Ilość_kolumn']}", styles["Normal"]))
    elements.append(Paragraph(f"Kolumny: {analyst['Kolumny']}", styles["Normal"]))
    elements.append(Spacer(1, 15))

    for statistic, columns in describe.items():
        elements.append(Paragraph(statistic, styles["Normal"]))
        elements.append(Spacer(1,10))
        for column, value in columns.items():
            elements.append(Paragraph(column, styles["Normal"]))
            value = str(value)
            elements.append(Paragraph(value, styles["Normal"]))
            elements.append(Spacer(1, 5))


    for chart in charts:
        elements.append(Image(chart))

    doc.build(elements)