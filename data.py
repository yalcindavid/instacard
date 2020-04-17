import pandas as pd
import numpy as np


def read_orders(n_clients, path ="/Users/yd953/PycharmProjects/instacard/orders.csv"):
    orders_df = pd.read_csv(path)
    orders_df = orders_df[["order_id","user_id"]]
    return orders_df[orders_df['user_id'].isin(range(N+1))]


def read_orders_products(path = "/Users/yd953/PycharmProjects/instacard/order_products__prior.csv"):
    orders_products_df = pd.read_csv(path)
    return orders_products_df[['order_id','product_id']]

def read_products(path="/Users/yd953/PycharmProjects/instacard/products.csv"):
    product_df = pd.read_csv(path)
    return product_df[['product_id','department_id']]


N=5
def read_write_sample(N=5):

    product_df = read_products()
    #lire un exemple d'order ['order_id','user_id']
    orders_df = read_orders(N)

    #lire order product avec ['order_id','product_id']
    orders_prod_df = read_orders_products()

    #1er merge ['user_id','order_id','product_id']
    orders_prod_df = pd.merge(orders_df,orders_prod_df,how="inner",on='order_id')

    #2eme merge ['user_id','order_id','product_id','department_id']
    orders_prod_df = pd.merge(orders_prod_df,product_df,on='product_id')

    #garger les colonnes ['user_id','order_id','department_id']
    orders_prod_df = orders_prod_df[['user_id','order_id','department_id']]

    #save echantillons
    orders_prod_df.to_csv("/Users/yd953/PycharmProjects/instacard/merge_sample.csv")

read_write_sample()


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
    df = pd.DataFrame(rows,columns = ['user_id','department_id'])
    print(df)
    return df

def one_hot_post_padding(matrix, max_categories_found,):
    '''
    Make a one hot matrix X after a padding
    Input:
        matrix after the padding
        max_categories_found = max of categorie found in every baskets
    Output:
        a one hot matrix as an array
    '''

    X_onehot = [] #our new onehot list of list of list in output

    for user in matrix:
        '''for each user'''
        L = [] #onehot of each user

        for order in user:
            '''for each basket in each user'''
            L1 = np.zeros(max_categories_found + 1) #onehot of each basket/order by user
            #print(order)

            for categorie in order:
                '''for each categorie in each order'''
                #print(categorie)
                c = int(categorie) #transform categorie from float to integer

                if c == 0:
                    L1[c] = 0
                else:
                    L1[c] = 1

            L.append(list(L1)) #append each order to each user in the list

        X_onehot.append(L) #append each user in one elist

    return list(X_onehot)
df_user = user_table()
df_user.to_csv("/Users/yd953/PycharmProjects/instacard/merge_sample_l.csv")

