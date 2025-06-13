# Import libraries
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk import pos_tag

# Download resources (only once per setup)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')

# Helper function to convert POS tag to wordnet POS
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # default

# Input sentence
sentence = "The children were playing games and having fun."

# Tokenize and POS tag
tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)

# Create lemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatize tokens using POS
lemmatized = [lemmatizer.lemmatize(token, get_wordnet_pos(pos)) for token, pos in pos_tags]

# Print results
print("Original Tokens:", tokens)
print("Lemmatized Tokens:", lemmatized)
