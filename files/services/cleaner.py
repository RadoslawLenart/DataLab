def cleaner(df):

    df = df.drop_duplicates()
    df = df.dropna()

    df.columns = (df.columns
                  .str.lower()
                  .str.strip()
                  .str.replace(' ', '_'))
    return df