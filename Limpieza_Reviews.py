import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words('english'))

# Definir una función para limpiar y procesar el texto
def clean_text(text):
    # Convertir a minúsculas
    text = text.lower()
    # Eliminar signos de puntuación y caracteres especiales
    text = re.sub(r'[^\w\s]', '', text)
    # Eliminar números y símbolos
    text = re.sub(r'\d+', '', text)
    # Tokenizar el texto en palabras
    words = nltk.word_tokenize(text)
    # Eliminar stop words
    words = [w for w in words if not w in stop_words]
    # Realizar la lematización de las palabras
    words = [lemmatizer.lemmatize(w) for w in words]
    # Unir las palabras en un nuevo texto
    new_text = ' '.join(words)
    return new_text
	
	
reviews_df['clean_text'] = reviews_df['text'].apply(clean_text)