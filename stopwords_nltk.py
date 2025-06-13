import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk import pos_tag

# Download required resources (only once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')

# Function to convert POS tags to WordNet format
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
        return wordnet.NOUN  # default to noun

# Create lemmatizer
lemmatizer = WordNetLemmatizer()

# Input sentence
sentence = "The children were playing games and having fun."

# Tokenize and POS tagging
tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)

# Lemmatize using POS
lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags]

# Output results
print("Original Tokens:", tokens)
print("Lemmatized Tokens:", lemmatized_words)
