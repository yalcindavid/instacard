import pandas as pd
import numpy as np
from numpy import array
from data import one_hot_post_padding
# from data import build_clients_sequences
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from data import read_products
from data import user_table
data = pd.read_csv("/Users/yd953/PycharmProjects/instacard/merge_sample.csv")

#rechercher les orders par clients

def user_table():
    user = pd.read_csv("/Users/yd953/PycharmProjects/instacard/merge_sample.csv")
    user_col = pd.unique(user['user_id']).tolist()
    user_col = user_col[:5]
    rows = []

    for i in user_col:
        data = user[user['user_id']== i]
        order_col = pd.unique(data['order_id']).tolist()

        liste = []
        for j in order_col:
            liste.append(data[data['order_id']==j]['department_id'])

        rows.append([i,liste])
    df = pd.DataFrame(rows,columns = ['user_id','department_id'],)
    df = df['department_id']
    print(df)
    return df

L = user_table()

#catégorie
C = 5
#2panier
T = 4
#observation
# for i in df_user['department_id']:
#     print(i)
X = np.array(L)
maxlen = 5
X = np.zeros((5,T,maxlen))
for i in range(len(L)):
    xi = pad_sequences(sequences=L[i],maxlen=C,dtype='int32',padding='pre',truncating='pre',value=0.0)
    t = min(T,xi.shape[0])
    xi = xi[:t]
    d = T-t
    X[i][d:] = xi
print(X)

#one hot encode
X_onehot = one_hot_post_padding(X,21)

#definir X et Y

Y = X_onehot[:][-1][:] #la derniere order
X = X_onehot[:][:-1][:] #2eme dimension order tous sauf le moin un

X = np.array(X)
Y = np.array(Y)



print("X=",X)
print("Y=",Y)
print("X shape=",X.shape)
print("Y shape=",Y.shape)
print(type(X))
print(type(Y))


