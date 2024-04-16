import tensorflow as tf
import tensorflow_hub as pornhub
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# helps in model building
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout, Embedding, LSTM
from tensorflow.keras.callbacks import EarlyStopping

# split data into train and test set
from sklearn.model_selection import train_test_split
tokenizer = Tokenizer()

model_prod = tf.keras.models.load_model('./new-trained-model.h5', custom_objects={'KerasLayer':pornhub.KerasLayer})

text = str(input("Enter the value: "))

sms_test = [text]
def spam_ham(text):
    sms_seq = tokenizer.texts_to_sequences(sms_test)
    sms_pad = pad_sequences(sms_seq, maxlen= 20, padding='post')
    tokenizer.index_word
    sms_pad
    a = model_prod.predict(sms_pad)
    a = a[0][0]
    print(a*100)
    if a >= 0.5:
        print('spam')
    else:
        print('not spam')

spam_ham(sms_test)