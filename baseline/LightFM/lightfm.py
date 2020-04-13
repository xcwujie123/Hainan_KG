#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:59:59 2020

@author: didi
"""

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score,f1_score

from lightfm import LightFM
from lightfm.data import Dataset
from lightfm.cross_validation import random_train_test_split
from lightfm.evaluation import precision_at_k
from lightfm.evaluation import auc_score
import time
import pickle
from scipy.sparse import csr_matrix

#model = LightFM(no_components=40,k=20,n=20,loss="bpr",learning_rate=0.05,max_sampled=30)
model = LightFM(no_components=40,k=20,n=20,loss="warp")

f_train=open("interaction.txt","r",encoding="utf-8")
lines=list(f_train.readlines())
rows,columns=0,0
for line in lines:
    line=line.strip()
    temp_rows,temp_columns,rate=line.split("\t")
    rows=max(rows,int(temp_rows))
    columns=max(columns,int(temp_columns))
    
arr_train=np.zeros([rows+1,columns+1])
for line in lines:
    line=line.strip()
    temp_rows,temp_columns,rate=line.split("\t")
    if rate=="1":
        #print(temp_rows,temp_columns)
        arr_train[int(temp_rows),int(temp_columns)]=1

df_data=pd.DataFrame(arr_train,index=list(range(rows+1)),columns=list(range(columns+1)))
data1 = csr_matrix(df_data)
data1.toarray()
train,test=random_train_test_split(data1,test_percentage=0.4, random_state=np.random.RandomState(1))


arr_itemfeature=np.load("entity_embedding.npy")[:columns+1,:]
#arr_itemfeature*=10
df_itemfeature=pd.DataFrame(arr_itemfeature,index=list(range(columns+1)),columns=list(range(20)))
data_feature=csr_matrix(df_itemfeature)
data_feature.toarray()

#model.fit(train,item_features=data_feature,epochs=50,verbose=True)
model.fit(train,epochs=10)
#print(auc_score(model,test,item_features=data_feature).mean())
print(auc_score(model,test).mean())
y_true=[]
y_predict=[]
max_rate=0
min_rate=0
f_test=open("test_1.txt","r",encoding="utf-8")
for line in f_test.readlines():
    line=line.strip()
    user,item,rate=line.split("\t")
    y_true.append(int(rate))
    rating=model.predict(np.int(user),[int(item)],item_features=data_feature)[0]
    rating=model.predict(np.int(user),[int(item)])[0]
    #print(rating)
    if rating>max_rate:
        max_rate=rating
    if rating<min_rate:
        min_rate=rating
    if rating>0.5:
        y_predict.append(1)
    else:
        y_predict.append(0)
    
print(accuracy_score(y_true,y_predict))
print(f1_score(y_true,y_predict))

k_list=[1,2,5,10,20,50,100]
with open("topk_test.pkl","rb") as f:
    dict_test=pickle.load(f)
with open("topk_history.pkl","rb") as f:
    dict_history=pickle.load(f)
    
precision_list = {k: [] for k in k_list}
recall_list = {k: [] for k in k_list}
for user,value in dict_test.items():
    dict_result={}
    for item in value:
        rate=model.predict(np.int(user),[int(item)])[0]
        dict_result[item]=rate
    item_score_pair_sorted = sorted(dict_result.items(), key=lambda x: x[1], reverse=True)
    item_sorted = [str(i[0]) for i in item_score_pair_sorted]
    for k in k_list:
        hit_num = len(set(item_sorted[:k]) & set(dict_history[user]))
# =============================================================================
#         print(hit_num)
#         print(k)
# =============================================================================
        precision_list[k].append(hit_num / k)
        recall_list[k].append(hit_num / len(dict_history[user]))

precision = [np.mean(precision_list[k]) for k in k_list]
recall = [np.mean(recall_list[k]) for k in k_list]
print(precision)
print(recall)