import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download tokenizer model (only needed once)
nltk.download('punkt')

text = "Thakku is learning Natural Language Processing with spaCy."
words = word_tokenize(text)

stemmer = PorterStemmer()

print("Stemming using NLTK:")
for word in words:
    print(f"{word} --> {stemmer.stem(word)}")
