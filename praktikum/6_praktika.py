import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
import spacy
from gensim.utils import simple_preprocess

article = 'Natural language processing (NLP) is a field of artificial intelligence\
that gives computers the ability to understand text and spoken words in much the same way human beings can.'

print('NLTK:', nltk.word_tokenize(article))
nlp = spacy.load("en_core_web_sm")
article_spacy = nlp(article)
print("paCy:", [t.text for t in article_spacy])
print("Gensim", simple_preprocess(article))
