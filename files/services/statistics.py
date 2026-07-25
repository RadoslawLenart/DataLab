def statistics(df):
    df = df.describe()
    describe = {
        'Liczba wartości': df.iloc[0].to_dict(),
        'Średnia': df.iloc[1].to_dict(),
        'Odchylenie standardowe': df.iloc[2].to_dict(),
        'Minimum': df.iloc[3].to_dict(),
        'Pierwszy kwartyl (25%)': df.iloc[4].to_dict(),
        'Mediana (50%)': df.iloc[5].to_dict(),
        'Trzeci kwartyl (75%)': df.iloc[6].to_dict(),
        'Maksimum': df.iloc[7].to_dict(),
    }
    return describe