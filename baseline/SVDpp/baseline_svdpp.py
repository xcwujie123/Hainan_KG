#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:44:53 2020

@author: didi
"""

import numpy as np
import random
from sklearn.metrics import accuracy_score,f1_score
import pickle
 
class SVD:
    def __init__(self,mat,K=20):
        self.mat=np.array(mat)
        self.K=K
        self.bi={}
        self.bu={}
        self.qi={}
        self.pu={}
        self.avg=np.mean(self.mat[:,2])
        for i in range(self.mat.shape[0]):
            uid=self.mat[i,0]
            iid=self.mat[i,1]
            self.bi.setdefault(iid,0)
            self.bu.setdefault(uid,0)
            self.qi.setdefault(iid,np.random.random((self.K,1))/10*np.sqrt(self.K))
            self.pu.setdefault(uid,np.random.random((self.K,1))/10*np.sqrt(self.K))
    def predict(self,uid,iid):  #预测评分的函数
        #setdefault的作用是当该用户或者物品未出现过时，新建它的bi,bu,qi,pu，并设置初始值为0
        self.bi.setdefault(iid,0)
        self.bu.setdefault(uid,0)
        self.qi.setdefault(iid,np.zeros((self.K,1)))
        self.pu.setdefault(uid,np.zeros((self.K,1)))
        rating=self.avg+self.bi[iid]+self.bu[uid]+np.sum(self.qi[iid]*self.pu[uid]) #预测评分公式
        #由于评分范围在1到5，所以当分数大于5或小于1时，返回5,1.
        if rating>1:
            rating=1
        if rating<0:
            rating=0
        return rating
    def train(self,steps=1,gamma=0.04,Lambda=0.15):    #训练函数，step为迭代次数。
        print('train data size',self.mat.shape)
        for step in range(steps):
            print('step',step+1,'is running')
            KK=np.random.permutation(self.mat.shape[0]) #随机梯度下降算法，kk为对矩阵进行随机洗牌
            rmse=0.0
            for i in range(self.mat.shape[0]):
                j=KK[i]
                uid=self.mat[j,0]
                iid=self.mat[j,1]
                rating=self.mat[j,2]
                eui=rating-self.predict(uid, iid)
                rmse+=eui**2
                self.bu[uid]+=gamma*(eui-Lambda*self.bu[uid])  
                self.bi[iid]+=gamma*(eui-Lambda*self.bi[iid])
                tmp=self.qi[iid]
                self.qi[iid]+=gamma*(eui*self.pu[uid]-Lambda*self.qi[iid])
                self.pu[uid]+=gamma*(eui*tmp-Lambda*self.pu[uid])
            gamma=0.93*gamma
            print('rmse is',np.sqrt(rmse/self.mat.shape[0]))
            
    def evaluate(self,uid,iid):
        self.bi.setdefault(iid,0)
        self.bu.setdefault(uid,0)
        self.qi.setdefault(iid,np.zeros((self.K,1)))
        self.pu.setdefault(uid,np.zeros((self.K,1)))
        rating=self.avg+self.bi[iid]+self.bu[uid]+np.sum(self.qi[iid]*self.pu[uid]) #预测评分公式
# =============================================================================
#         if rating>2.5:
#             rating=1
#         if rating<=2.5:
#             rating=0
# =============================================================================
        return rating
    def test(self,test_data):  #gamma以0.93的学习率递减
        
        test_data=np.array(test_data)
        print('test data size',test_data.shape)
        rmse=0.0
        for i in range(test_data.shape[0]):
            uid=test_data[i,0]
            iid=test_data[i,1]
            rating=test_data[i,2]
            eui=rating-self.predict(uid, iid)
            rmse+=eui**2
        print('rmse of test data is',np.sqrt(rmse/test_data.shape[0]))


f_train=open("train_1.txt","r",encoding="utf-8")
f_test=open("test_1.txt","r",encoding="utf-8")
train_data=[]
for line in f_train.readlines():
    line=line.strip()
    user,item,rate=line.split("\t")
    if rate=="1":
        train_data.append([int(user),int(item),1])
    else:
        train_data.append([int(user),int(item),0])
test_data=[]
y_true=[]
y_predict=[]
user_item=[]
for line in f_test.readlines():
    line=line.strip()
    #;print(line)
    user,item,rate=line.split("\t")
    user_item.append([int(user),int(item)])
    y_true.append(int(rate))
    if rate=="1":
        test_data.append([int(user),int(item),1])
    else:
        test_data.append([int(user),int(item),0])
a=SVD(train_data,2)
a.train()
for user,item in user_item:
    rating=a.evaluate(user,item)
    #print(rating)
    if rating>0.5:
        y_predict.append(1)
    else:
        y_predict.append(0)
# =============================================================================
# print(y_true)
# print(y_predict)
# =============================================================================
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
        rate=a.evaluate(int(user),int(item))
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