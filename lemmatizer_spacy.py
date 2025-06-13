import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Your input sentence
sentence = "The children were playing games and having fun."

# Process the sentence
doc = nlp(sentence)

# Print original and lemmatized words
print("Original Tokens:", [token.text for token in doc])
print("Lemmatized Tokens:", [token.lemma_ for token in doc])
