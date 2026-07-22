def statistics(df):
    df = df.describe()
    describe = {
        'count': df.iloc[0].to_dict(),
        'mean': df.iloc[1].to_dict(),
        'std': df.iloc[2].to_dict(),
        'min': df.iloc[3].to_dict(),
        '25%': df.iloc[4].to_dict(),
        '50%': df.iloc[5].to_dict(),
        '75%': df.iloc[6].to_dict(),
        'max': df.iloc[7].to_dict(),
    }
    return describe