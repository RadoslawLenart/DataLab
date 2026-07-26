# DataLab

DataLab to aplikacja webowa napisana w Pythonie z wykorzystaniem frameworka Flask, umożliwiająca analizę, czyszczenie oraz wizualizację danych zapisanych w plikach CSV. Projekt został stworzony jako element portfolio, prezentujący praktyczne umiejętności w zakresie analizy danych oraz tworzenia aplikacji webowych.

---

## Cel projektu

Celem projektu jest rozwój kompetencji w obszarach:

- programowania w języku Python,
- analizy i przetwarzania danych z wykorzystaniem biblioteki **Pandas**,
- budowy aplikacji webowych opartych o **Flask**,
- wizualizacji danych z użyciem **Matplotlib**,
- generowania raportów PDF,
- projektowania struktury aplikacji oraz organizacji kodu.

---

## Funkcjonalności

### Obsługa plików CSV

- przesyłanie plików CSV przez interfejs webowy,
- automatyczne wykrywanie kodowania pliku,
- obsługa różnych formatów CSV,
- walidacja poprawności danych wejściowych,
- obsługa błędów (np. pusty plik, niepoprawny format).

### Analiza danych

Aplikacja generuje podstawowy raport dotyczący struktury danych:

- nazwa pliku,
- liczba wierszy i kolumn,
- nazwy kolumn,
- liczba brakujących wartości,
- liczba duplikatów,
- statystyki opisowe dla danych liczbowych.

### Wizualizacja danych

- automatyczne tworzenie histogramów dla kolumn typu `int` oraz `float`,
- zapisywanie wykresów w aplikacji,
- prezentacja wyników w dashboardzie.

### Czyszczenie danych

Możliwość przygotowania danych poprzez:

- usuwanie duplikatów,
- usuwanie rekordów zawierających brakujące wartości,
- normalizację nazw kolumn:
  - zamiana liter na małe,
  - usuwanie zbędnych spacji,
  - zamiana spacji na znak `_`.

Przykład:

```
First Name → first_name
```

### Raport PDF

Generowanie raportu zawierającego:

- informacje o pliku,
- wyniki analizy,
- statystyki opisowe,
- informacje o jakości danych.

### Eksport danych

Możliwość pobrania:

- oczyszczonego pliku CSV,
- wygenerowanego raportu PDF.

---

## Technologie

| Technologia | Zastosowanie |
|-------------|--------------|
| Python | logika aplikacji |
| Flask | backend webowy |
| Pandas | analiza i przetwarzanie danych |
| Matplotlib | generowanie wykresów |
| ReportLab | tworzenie raportów PDF |
| HTML / CSS | interfejs użytkownika |
| Jinja2 | szablony widoków |

---

## Struktura projektu

```text
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

## Instalacja i uruchomienie

### 1. Klonowanie repozytorium

```bash
git clone https://github.com/RadoslawLenart/DataLab.git
cd DataLab
```

### 2. Utworzenie środowiska wirtualnego

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalacja zależności

```bash
pip install -r requirements.txt
```

### 4. Uruchomienie aplikacji

```bash
python app.py
```

Aplikacja będzie dostępna pod adresem:

```text
http://127.0.0.1:5000
```

---

## Planowany rozwój

Projekt znajduje się w pierwszej wersji i będzie rozwijany. Planowane funkcje:

- dodatkowe typy wykresów,
- eksport danych do Excela,
- możliwość wyboru sposobu czyszczenia danych,
- historia analiz,
- rozbudowany system raportów,
- ulepszenia interfejsu użytkownika.

---

## Autor

**Radosław Lenart**  
GitHub: https://github.com/RadoslawLenart
