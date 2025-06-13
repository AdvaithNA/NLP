import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Input sentence
sentence = "The children were playing games and having so much fun in the garden."

# Process the sentence
doc = nlp(sentence)

# Remove stopwords
filtered_tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]

# Output
print("Original Tokens:", [token.text for token in doc])
print("Filtered Tokens (no stopwords):", filtered_tokens)
