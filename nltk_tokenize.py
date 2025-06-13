import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required tokenizer data (run only once)
nltk.download('punkt')

# Sample text
text = "Hello! My name is Thakku. I am learning Natural Language Processing using NLTK."

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentence Tokenization:")
print(sentences)

# Word Tokenization
words = word_tokenize(text)
print("\nWord Tokenization:")
print(words)
