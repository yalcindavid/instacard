from keras.models import Sequential, Model
from keras.layers import LSTM, Dense, Dropout, Masking, Embedding, Input
from main import X, Y
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix

X = np.array(X)
Y = np.array(Y)



print("X=",X)
print("Y=",Y)
print("X shape=",X.shape)
print("Y shape=",Y.shape)
print(type(X))
print(type(Y))


# look_back = 1
# # create and fit the LSTM network

model = Sequential()
model.add(LSTM(22,input_shape=(4,22)))
model.add(Dense(64,activation='sigmoid'))
model.add(Dense(22,activation='softmax'))
model.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])
model.fit(X, Y, epochs=200, batch_size=1, verbose=2)



