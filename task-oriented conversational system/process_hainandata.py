# -*- coding: UTF-8 -*-
import json
import numpy as np
import pandas as pd
activity={}
f_activity=open("database/activity.txt","r",encoding="utf-8")
for line in f_activity.readlines():
    line=line.strip()
    activity_s=line[:-2]
    activity_s=activity_s.split(":")[1]
    activity_list=activity_s.split("||")
    for item in activity_list:
        if item not in activity:
            activity[item]=0
        activity[item]+=1
result=[]
for key,value in activity.items():
    temp=key.split(",")
    temp.append(str(value))
    result.append(temp)
#print(result)
arr_result=np.array(result)
#print(arr_result.shape)
df_result=pd.DataFrame(arr_result,columns=["position","activity","time","count"])

f_route=open("route_hainan.txt","r",encoding="utf-8")
f_people=open("database/people.txt","r",encoding="utf-8")
f_write=open("route_data.json","w",encoding="utf-8")
route_list=[]
people_list=[]
result=[]
for line in f_route.readlines():
    line=line.strip()
    temp=line.split(":")[1]
    temp_list=temp.split(",")
    route_list.append(temp_list)
    
for line in f_people.readlines():
    line=line.strip()
    temp=line.split(":")[1]
    temp_list=temp.split("|")
    people_list.append(temp_list)
    
# print(len(people_list))
# print(len(route_list))

for i in range(len(route_list)):
    #print(i)
    temp={}
    temp["travel_days"]=people_list[i][0]
    temp["travel_title"]=people_list[i][1]
    temp["travel_type"]=people_list[i][2]
    temp["travel_month"]=people_list[i][3]
    temp["budget"]=people_list[i][4]
    temp["route"]=route_list[i]
    result.append(temp)

f_write.write(json.dumps(result, ensure_ascii=False, indent=2))