def normalize_column(df, col_name):
    x_max = df[col_name].max()
    x_min = df[col_name].min()
    df[f"{col_name}_norm"] = (df[col_name] - x_min) / (x_max - x_min)
    return df

df = normalize_column(df, "review_count")
df = normalize_column(df, "rating")

reviews_df['time_created'] = pd.to_datetime(reviews_df['time_created'])
reviews_df['hour'] = reviews_df['time_created'].dt.hou
reviews_df = normalize_column(reviews_df, "rating")