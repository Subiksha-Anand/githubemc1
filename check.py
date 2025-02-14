import pickle

with open("tokenizer.pkl", "rb") as handle:
    tokenizer = pickle.load(handle)

print(type(tokenizer))  # Should print <class 'keras.preprocessing.text.Tokenizer'>

# Test with sample text
test_text = "This is a great movie"
test_sequence = tokenizer.texts_to_sequences([test_text])

print(test_sequence)  # Should NOT be an empty list
