from textblob import TextBlob
import matplotlib.colors as mcolors

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity
	
reviews_df[['polarity', 'subjectivity']] = reviews_df['clean_text'].apply(get_sentiment).apply(pd.Series)


combined_df = pd.merge(df, reviews_df, on='id')

#Polaridad vs. Subjetividad por calificación
# Escala de colores de rojo a azul
colors = mcolors.LinearSegmentedColormap.from_list("", ["red", "yellow", "white", "lightblue", "blue"])

plt.scatter(combined_df['polarity'], combined_df['subjectivity'], c=combined_df['rating_x'], cmap=colors)
plt.xlabel('Polaridad')
plt.ylabel('Subjetividad')
plt.title('Polaridad vs. Subjetividad por calificación')
plt.colorbar()
plt.show()

#Polaridad promedio por hora del día
hourly_polarity = combined_df.groupby('hour')['polarity'].mean()

plt.bar(hourly_polarity.index, hourly_polarity)
plt.xlabel('Hora del día')
plt.ylabel('Polaridad promedio')
plt.title('Polaridad promedio por hora del día')
plt.show()


#Polaridad promedio por día de la semana
weekday_polarity = combined_df.groupby(combined_df['time_created'].dt.weekday)['polarity'].mean()

plt.bar(weekday_polarity.index, weekday_polarity)
plt.xlabel('Día de la semana')
plt.ylabel('Polaridad promedio')
plt.title('Polaridad promedio por día de la semana')
plt.xticks(range(7), ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
plt.show()