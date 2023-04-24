#Histograma del número de negocios por ciudad:
df['location.city'].hist()

#Gráfica de barras de los 10 negocios con más reviews:
top10 = df.nlargest(10, 'review_count')
top10.plot.bar(x='name', y='review_count')

#Gráfica de barras de la distribución de los precios:
df['price'].value_counts().plot(kind='bar')

#Histograma de la distribución de ratings:
reviews_df['rating'].hist()

#Gráfica de barras de la distribución de ratings por hora del día:
reviews_df.groupby('hour')['rating'].mean().plot(kind='bar')

#Gráfica de línea del número de reviews por fecha:
reviews_df.groupby('time_created')['text'].count().plot(kind='line')