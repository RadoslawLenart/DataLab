import pandas as pd
from flask import request
from charset_normalizer import from_path

def csv_loader(UPLOAD_FOLDER):
    try:
        file = request.files['file']

        file_path = UPLOAD_FOLDER/file.filename
        file.save(file_path)

        result = from_path(file_path).best()
        if result:
            encoding = result.encoding
        else:
            encoding = "utf-8"

        df = pd.read_csv(file_path, sep=None, engine='python', encoding=encoding)
        return df, file

    except pd.errors.EmptyDataError:
        return None, "Plik jest pusty"
    except pd.errors.ParserError:
        return None, "Plik CSV ma błędną strukturę"
    except UnicodeDecodeError:
        return None, "Nieprawidłowe kodowanie pliku"
    except FileNotFoundError:
        return None, "Nie znaleziono pliku"
    except Exception as e:
        return None, f"Nieoczekiwany błąd: {e}"