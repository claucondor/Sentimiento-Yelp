import requests
import json
import pandas as pd

api_key = 'zW8tYyrQiIik_N8HFs3ARaPFiiDxWeOQ9tkZBj6T_W-WgEt1SXtkLgKo1n-54Veve9TJTxckf13F4EH-2SW2drisG0DkGNZgGKpNJ2TkVOFuSjMWaxI2qmQ2l-hFZHYx'

headers = {
    "Authorization": "Bearer " + api_key
}

cities = ["New York", "Los Angeles", "Chicago", "Houston"]

dfs = []
for city in cities:
    for offset in range(0, 20, 20):
        url = "https://api.yelp.com/v3/businesses/search"
        params = {
            "term": "restaurant",
            "location": city,
            "limit": 20,
            "offset": offset,
            "categories": "restaurants,bars,food",
            "locale": "en_US"
        }
        response = requests.get(url, headers=headers, params=params)
        data = json.loads(response.text)
        df = pd.json_normalize(data["businesses"])
        dfs.append(df)
df = pd.concat(dfs)

cols_to_drop = ['coordinates.latitude','coordinates.longitude','display_phone','phone','distance','image_url','is_closed','location.address1','location.address2','location.address3','location.zip_code','location.country','location.state','location.display_address','url']
df.drop(columns=cols_to_drop, inplace=True)

# Muestra la cantidad de filas y columnas del dataframe
print(df.shape)

# Muestra los nombres de las columnas
print(df.columns)

# Muestra información sobre cada columna, incluyendo el tipo de dato y la cantidad de valores no nulos
print(df.info())

# Muestra estadísticas descriptivas para las columnas numéricas
print(df.describe())

# Muestra la cantidad de valores nulos en cada columna
print(df.isnull().sum())

# Elimina las filas que tienen al menos un valor nulo
df.dropna(inplace=True)


reviews = []
for business_id in df['id']:
    url = f"https://api.yelp.com/v3/businesses/{business_id}/reviews"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    if 'reviews' in data:
        reviews_data = data['reviews']
        for review in reviews_data[:50]:
            review_dict = {
                'id': business_id,
                'text': review['text'],
                'rating': review['rating'],
                'time_created': review['time_created'],
            }
            reviews.append(review_dict)

reviews_df = pd.DataFrame(reviews)
reviews_df.drop(columns=cols_to_drop, inplace=True)



