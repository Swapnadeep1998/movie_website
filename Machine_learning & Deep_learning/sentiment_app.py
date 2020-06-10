from tensorflow.keras.preprocessing.text import tokenizer_from_json
import re
from tensorflow.keras.models import  load_model
import json
from tensorflow.keras.preprocessing.sequence import pad_sequences


with open('tokenizer_version_2.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)

senti_model = load_model("sentiment_version_2.h5")
max_len = 150
trunc_type = 'post'
padding = 'post'

def clean_text(text):  
    
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"books", "movies", text)
    text = re.sub(r"book", "movie", text)
    text = re.sub(r"read", "watch", text)
    text = re.sub(r"pages", "plots", text)
    text = re.sub(r"author", "story writer", text)
    text = re.sub(r"written", "directed", text)
    text = re.sub(r"ordered", "booked ticket", text)    
    text = re.sub(r"reading", "watching", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)        
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text) 
    text = re.sub(r"\'ll", " will", text)  
    text = re.sub(r"\'ve", " have", text)  
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"don't", "do not", text)
    text = re.sub(r"did't", "did not", text)
    text = re.sub(r"can't", "can not", text)
    text = re.sub(r"it's", "it is", text)
    text = re.sub(r"couldn't", "could not", text)
    text = re.sub(r"have't", "have not", text)
    text = re.sub(r"[,.\"\'!@#$%^&*(){}?/;`~:<>+=-]", "", text)
    return text

def CleanTokenize(l):
    cleaned_sentences = []   
    for line in l:
        line = clean_text(str(line))               
        cleaned_sentences.append(line)
    return cleaned_sentences


def sentiment(review):
	cleaned_review = CleanTokenize(review)
	test_sequences = tokenizer.texts_to_sequences(cleaned_review)
	test_padded = pad_sequences(test_sequences,maxlen=max_len, padding=padding)
	prob = senti_model.predict(test_padded)
	return prob
