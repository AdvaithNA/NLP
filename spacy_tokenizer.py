import spacy

# Load the small English model (make sure it's downloaded first)
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Thakku is learning Natural Language Processing with spaCy."

# Process the text
doc = nlp(text)

# Tokenization + POS + Lemma
print("Token  |  POS Tag  |  Lemma")
print("------------------------------")
for token in doc:
    print(f"{token.text:10} {token.pos_:10} {token.lemma_}")
