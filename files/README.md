# 📊 DataLab

DataLab to aplikacja webowa napisana w Pythonie z wykorzystaniem Flaska, która umożliwia analizę, czyszczenie i wizualizację danych zapisanych w plikach CSV.

Projekt został stworzony jako aplikacja do nauki Pythona, Pandas oraz tworzenia aplikacji webowych we Flasku.

---

## Funkcje

- Przesyłanie plików CSV
- Automatyczne wykrywanie kodowania pliku
- Analiza danych:
  - liczba wierszy
  - liczba kolumn
  - nazwy kolumn
  - brakujące dane
  - duplikaty
  - statystyki opisowe
- Generowanie wykresów
- Czyszczenie danych
- Generowanie raportu PDF
- Pobieranie poprawionego pliku CSV
- Obsługa błędów (np. pusty plik, błędny format)

---

## Technologie

- Python
- Flask
- Pandas
- Matplotlib
- ReportLab
- HTML
- CSS

---

## Struktura projektu

```
DataLab/
│
├── app.py
├── config.py
├── requirements.txt
│
├── charts/
│   └── plot_generator.py
│
├── services/
│   ├── analyzer.py
│   ├── cleaner.py
│   ├── csv_loader.py
│   ├── pdf_generator.py
│   └── statistics.py
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── error.html
│
├── static/
│   ├── css/
│   ├── images/
│   └── reports/
│
└── uploads/
```

---

## Instalacja

Sklonuj repozytorium:

```bash
git clone https://github.com/TWOJ_LOGIN/DataLab.git
```

Przejdź do katalogu projektu:

```bash
cd DataLab
```

Utwórz środowisko wirtualne:

```bash
python -m venv .venv
```

Aktywuj środowisko:

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Zainstaluj wymagane biblioteki:

```bash
pip install -r requirements.txt
```

Uruchom aplikację:

```bash
python app.py
```

Otwórz przeglądarkę:

```
http://127.0.0.1:5000
```

---

## Przykładowy przebieg

1. Wybierz plik CSV.
2. Aplikacja analizuje dane.
3. Wyświetlany jest dashboard z wynikami.
4. W razie potrzeby wyczyść dane.
5. Pobierz raport PDF lub poprawiony plik CSV.

---

## Przykładowe zrzuty ekranu

Tutaj warto dodać kilka obrazów, np.

```
docs/
├── home.png
├── dashboard.png
└── report.png
```

i w README:

```md
### Strona główna

![Home](docs/home.png)

### Dashboard

![Dashboard](docs/dashboard.png)
```

---

## Autor

Radosław Lenart

Projekt wykonany w celu nauki języka Python, biblioteki Pandas oraz frameworka Flask.