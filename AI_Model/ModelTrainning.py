#Imorting Libraries
import tensorflow as tf
import tensorflow_hub as hub
import pandas as pd
import seaborn as sns
import numpy as np
%matplotlib inline
from sklearn.model_selection import train_test_split

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# helps in model building
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout, Embedding, LSTM
from tensorflow.keras.callbacks import EarlyStopping

# split data into train and test set
from sklearn.model_selection import train_test_split


# Load the data
df = pd.read_csv('combined.csv')
df.head()

df['target'] = df['spam'].map( {1:0, 0:1 })
df.head()

# Split the data into train and test
df_train = df.sample(frac=.8, random_state=11)
df_test = df.drop(df_train.index)
print(df_train.shape, df_test.shape)

y_train = df_train['target'].values
y_test = df_test['target'].values
y_test.shape

X_train = df_train['text'].values
X_test = df_test['text'].values

#Tokenization of the data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)
word_dict = tokenizer.index_word

X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)


X_train_pad = pad_sequences(X_train_seq, maxlen=20, padding='post')
X_test_pad = pad_sequences(X_test_seq, maxlen=20, padding='post')
X_train_pad[:5]
X_train_pad.shape



from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dropout, Dense

#Model Building
model = Sequential([
    Embedding(input_dim=33955+1, output_dim=20, name='embedding1'),
    LSTM(400, name='LSTM'),
    Dropout(0.4, name='Dropout1'),
    Dense(32, activation='relu', name='Dense1'),
    Dense(16, activation='relu', name='Dense2'),
    Dense(1, activation='sigmoid', name='output_layer')
])

early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=10)

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train_pad, y_train, 
          epochs= 10, batch_size= 64, 
          validation_data= (X_test_pad, y_test), 
          verbose= 1, callbacks= [early_stop])

model.save("new-trained-model.h5")
model.save("../04-inference/new-trained-model.h5")



#Manual Testing
text = str(input("Enter the value: "))
tokenizer = Tokenizer()

def spam_ham(text):
    sms_test = [text]
    sms_seq = tokenizer.texts_to_sequences(sms_test)
    sms_pad = pad_sequences(sms_seq, maxlen= 20, padding='post')
    tokenizer.index_word
    sms_pad
    a = model.predict(sms_pad)
    if a >= 0.5:
        print('spam')
    else:
        print('not spam')

spam_ham(text)

model_prod = tf.keras.models.load_model('./new-trained-model.h5', custom_objects={'KerasLayer':hub.KerasLayer})
model_prod.summary()
