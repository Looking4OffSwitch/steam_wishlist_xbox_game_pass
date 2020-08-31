import string
import re
import Levenshtein
from stop_words import get_stop_words
import nltk
from nltk.corpus import stopwords

def clean_string(text: str):
    text = text.lower()
    text = ''.join(word for word in text if word not in string.punctuation)

    # remove all non-asci chars (e.g. '®', '™', etc.)
    text = re.sub(r'[^\x00-\x7f]', r'', text)

    stop_words = get_stop_words('english')

    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])

    return text


def degree_difference(str1: string, str2: string):
    # https://towardsdatascience.com/calculating-string-similarity-in-python-276e18a7d33a
    dist = Levenshtein.distance(str1, str2)
    return dist


if __name__ == 'utils':
     nltk.download('stopwords', quiet=True)
