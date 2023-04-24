import matplotlib.pyplot as plt

#Histograma del número de negocios por ciudad:

# Agrupar los negocios por ciudad y contar la cantidad de negocios por ciudad
city_counts = df.groupby('location.city').size().reset_index(name='count')

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(city_counts['location.city'], city_counts['count'])
plt.xticks(rotation=90)
plt.xlabel('Ciudad')
plt.ylabel('Cantidad de negocios')
plt.title('Cantidad de negocios por ciudad')
plt.show()

#Gráfica de barras de los 10 negocios con más reviews:
top10 = df.nlargest(10, 'review_count')
top10.plot.bar(x='name', y='review_count')

#Gráfica de barras de la distribución de los precios:
df['price'] = df['price'].apply(lambda x: len(x))

# Gráfica de barras de la distribución de los precios:
df['price'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Número de caracteres')
plt.ylabel('Frecuencia')
plt.title('Distribución de los precios')
plt.show()

#Histograma de la distribución de ratings:
plt.hist(reviews_df['rating'], bins=5, color='green', edgecolor='black', linewidth=1.2)
plt.title('Distribución de las valoraciones')
plt.xlabel('Valoración')
plt.ylabel('Número de valoraciones')
plt.show()

#Gráfica de barras de la distribución de ratings por hora del día:
plt.bar(reviews_df.groupby('hour')['rating'].mean().index, reviews_df.groupby('hour')['rating'].mean())
plt.title('Media de las puntuaciones por hora')
plt.xlabel('Hora del día')
plt.ylabel('Puntuación media')
plt.show()

