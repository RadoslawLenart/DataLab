import pandas as pd
from flask import request
from charset_normalizer import from_path
from pathlib import Path

from werkzeug.datastructures import FileStorage


def csv_loader(UPLOAD_FOLDER, file_is_true):
    try:

        if not file_is_true:
            file = request.files["file"]
            file_path = UPLOAD_FOLDER / file.filename
            file.save(file_path)

        else:
            file_path = next(Path(UPLOAD_FOLDER).iterdir())

            file = FileStorage(
                stream=open(file_path, "rb"),
                filename=file_path.name
            )


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