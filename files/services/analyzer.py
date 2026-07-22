def analyzer(UPLOAD_FOLDER, file, df):
    analyst = {
        'ilość_wierszy': df.shape[0],
        'ilość_kolumn': df.shape[1],
        'kolumny': list(df.columns)
    }

    columns = []
    for column in analyst['kolumny']:
        columns.append(column)

    missing = df.isnull().sum().to_dict()
    counter = 1
    status = None
    for column in missing.values():
        if column == 0:
            counter += 1
            if counter == (analyst['ilość_kolumn']) and df.duplicated().sum() == 0:
                status = 'Poprawny'
        else:
            status = 'Niepoprawny'
            break

    analyst.update({
        'Nazwa_pliku': file.filename,
        'Kolumny': columns,
        'Brakujące_dane': missing,
        'Duplikaty': df.duplicated().sum(),
        'Status': status,
    })
    return analyst, columns