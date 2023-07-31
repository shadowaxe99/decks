```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class NLPProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def process_text(self, text):
        # Tokenize the text
        word_tokens = word_tokenize(text)

        # Remove stop words
        filtered_text = [w for w in word_tokens if not w in self.stop_words]

        # Lemmatize the words
        lemmatized_text = [self.lemmatizer.lemmatize(w) for w in filtered_text]

        return lemmatized_text

def processNLP(investorPreferences):
    nlp_processor = NLPProcessor()
    processed_preferences = {}

    for key, value in investorPreferences.items():
        processed_preferences[key] = nlp_processor.process_text(value)

    return processed_preferences
```