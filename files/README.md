# 📊 DataLab

DataLab to aplikacja webowa napisana w Pythonie z wykorzystaniem frameworka Flask, która umożliwia analizę, czyszczenie oraz wizualizację danych zapisanych w plikach CSV.

Projekt pozwala użytkownikowi szybko sprawdzić jakość danych, wykryć potencjalne problemy oraz wygenerować raport zawierający wyniki analizy.

🔗 **Repozytorium GitHub:**  
https://github.com/RadoslawLenart/DataLab

---

## 🎯 Cel projektu

DataLab został stworzony jako projekt portfolio rozwijający umiejętności w zakresie:

- języka Python
- analizy danych z wykorzystaniem biblioteki Pandas
- tworzenia aplikacji webowych Flask
- wizualizacji danych
- generowania raportów PDF

---

# 🚀 Funkcje

## 📂 Obsługa plików CSV

- przesyłanie plików CSV
- automatyczne wykrywanie kodowania pliku
- obsługa różnych formatów plików CSV
- sprawdzanie poprawności danych wejściowych
- obsługa błędów (np. pusty plik, niepoprawny format)

---

## 📊 Analiza danych

Aplikacja automatycznie analizuje przesłany plik i wyświetla:

- nazwę pliku
- liczbę wierszy
- liczbę kolumn
- nazwy kolumn
- brakujące wartości
- liczbę duplikatów
- podstawowe statystyki opisowe

---

## 📈 Wizualizacja danych

DataLab automatycznie generuje wykresy dla danych numerycznych:

- histogramy kolumn typu `int` oraz `float`
- zapis wykresów do aplikacji
- prezentacja wykresów w dashboardzie

---

## 🧹 Czyszczenie danych

Aplikacja umożliwia przygotowanie danych poprzez:

- usuwanie duplikatów
- usuwanie rekordów zawierających brakujące wartości
- poprawianie nazw kolumn:

  - zamiana liter na małe
  - usuwanie zbędnych spacji
  - zamiana spacji na znak `_`

Przykład:

```
First Name → first_name
```

---

## 📄 Raport PDF

Po poprawnej analizie danych użytkownik może wygenerować raport PDF zawierający:

- informacje o pliku
- wyniki analizy
- statystyki opisowe
- informacje o jakości danych

---

## 📥 Eksport danych

Możliwość pobrania:

- oczyszczonego pliku CSV
- raportu PDF

---

# 🛠 Technologie

| Technologia | Zastosowanie |
|-------------|--------------|
| Python | główny język projektu |
| Flask | aplikacja webowa |
| Pandas | analiza i przetwarzanie danych |
| Matplotlib | generowanie wykresów |
| ReportLab | tworzenie raportów PDF |
| HTML | struktura strony |
| CSS | wygląd interfejsu |
| Jinja2 | szablony Flask |

---

# 📁 Struktura projektu

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

# ⚙️ Instalacja

## 1. Sklonowanie repozytorium

```bash
git clone https://github.com/RadoslawLenart/DataLab.git
```

Przejście do folderu projektu:

```bash
cd DataLab
```

---

## 2. Utworzenie środowiska wirtualnego

Windows:

```bash
python -m venv .venv
```

Aktywacja:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Instalacja bibliotek

```bash
pip install -r requirements.txt
```

---

## 4. Uruchomienie aplikacji

```bash
python app.py
```

Aplikacja będzie dostępna pod adresem:

```
http://127.0.0.1:5000
```

---

# 🔄 Jak działa aplikacja?

1. Użytkownik przesyła plik CSV.
2. DataLab analizuje strukturę danych.
3. Tworzony jest dashboard z wynikami.
4. Generowane są wykresy dla danych liczbowych.
5. Użytkownik może:
   - sprawdzić jakość danych,
   - oczyścić plik,
   - pobrać poprawiony CSV,
   - wygenerować raport PDF.

---

# 📸 Screenshots

*(Dodaj tutaj zrzuty ekranu aplikacji)*

Przykładowa struktura:

```
docs/
├── home.png
├── dashboard.png
└── report.png
```

### Strona główna

![Home](docs/home.png)

### Dashboard

![Dashboard](docs/dashboard.png)

### Raport PDF

![Report](docs/report.png)

---

# 🔮 Planowany rozwój

Możliwe dalsze funkcje:

- więcej typów wykresów
- eksport danych do Excela
- możliwość wyboru sposobu czyszczenia danych
- historia analiz
- zapis wyników użytkowników
- rozbudowany system raportów
- poprawa wyglądu interfejsu

---

# 👤 Autor

**Radosław Lenart**

GitHub:  
https://github.com/RadoslawLenart

---

Projekt wykonany jako aplikacja portfolio rozwijająca praktyczne umiejętności programowania w Pythonie, analizy danych oraz tworzenia aplikacji webowych.