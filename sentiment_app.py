import tensorflow as tf
from tensorflow.keras.models import load_model
import json
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences

max_length = 100
trunc_type = 'post'

model = load_model("sentiment.h5")


with open('tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)

sentence = input(str("Give your reviews: "))


def classify(sentence):
	test_sequence = tokenizer.texts_to_sequences([sentence])
	test_padded = pad_sequences(test_sequence , maxlen = max_length, padding= 'post', truncating= trunc_type)
	result = model.predict(test_padded)
	if result[0][0]>=0.5:
		return 1
	else:
		return 0

print(classify(sentence))
