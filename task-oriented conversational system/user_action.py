# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import argparse
import logging
import jieba
jieba.load_userdict("jieba_userdict.txt")

from rasa_core.actions import Action
from rasa_core.events import SlotSet
import json
import numpy as np
import pandas as pd

df_activity=pd.read_csv("data/activity_search.csv")

with open("data/route_data.json",encoding="utf-8") as f:
    route_db=json.load(f)
    
class ActionSearchbyactivity(Action):
    def name(self):
        return "action_searchbyactivity"
    def run(self,dispatcher,tracker,domain):
        if tracker.get_slot("activity") is None:
            dispatcher.utter_message("请输入您想要在海南进行的活动")
        else:
            df_celected=df_activity.loc[df_activity["activity"]=="潜水"]
            df_celected=df_celected.sort_values(by="count",ascending=False)
            arr_celected=df_celected.values
            if(df_celected.shape[0]==0):
                dispatcher.utter_message("未能查询到该适合进行活动的地点")
            elif(df_celected.shape[0]==1):
                dispatcher.utter_message("您可以在%(position)s%(activity)s"%{"position":arr_celected[0][0],"activity":tracker.get_slot("activity")})
            else:
                position_list=[]
                position_list.append(arr_celected[0][0])
                position_list.append(arr_celected[1][0])
                s_position=",".join(position_list)
                dispatcher.utter_message("您可以去%(position)s%(activity)s"%{"position":s_position,"activity":tracker.get_slot("activity")})
            return []


class ActionSearchbytype(Action):
    def name(self):
        return "action_searchbytype"
    def run(self,dispatcher,tracker,domain):
        if tracker.get_slot("trip_type") is None:
            dispatcher.utter_message("您希望和谁一起旅行呢？")
            return []
        dispatcher.utter_message("请稍等，正在为您安排路线")
        for i in range(len(route_db)):
            if tracker.get_slot("trip_type") in route_db[i]["travel_type"]:
                route_list=route_db[i]["route"]
                s_route="--".join(route_list)
                s_result="根据您的需求我们为您安排了下面的路线：\n%s"%s_route
                dispatcher.utter_message(s_result)
                break
            if(i==len(route_db)-1):
                dispatcher.utter_message("未能找到您需要的路线，请重新查询")
        return []

class ActionSearchbytitle(Action):
    def name(self):
        return "action_searchbytitle"
    def run(self,dispatcher,tracker,domain):
        if tracker.get_slot("trip_title") is None:
            #print(tracker.get_slot("trip_title"))
            dispatcher.utter_message("您希望这次旅行有什么特色或者是主题呢？")
            return []
        dispatcher.utter_message("请稍等，正在为您安排路线")
        for i in range(len(route_db)):
            if tracker.get_slot("trip_title") in route_db[i]["travel_title"]:
                route_list=route_db[i]["route"]
                s_route="--".join(route_list)
                s_result="根据您的需求我们为您安排了下面的路线：\n%s"%s_route
                dispatcher.utter_message(s_result)
                break
            if(i==len(route_db)-1):
                dispatcher.utter_message("未能找到您需要的路线，请重新查询")
        return []

class ActionSearchbybudget(Action):
    def name(self):
        return "action_searchbybudget"
    def run(self,dispatcher,tracker,domain):
        if tracker.get_slot("budget") is None:
            dispatcher.utter_message("您这次旅行的预算是人均多少钱呢？")
            print(tracker.get_slot("budget"))
            return []
        dispatcher.utter_message("请稍等，正在为您安排路线")
        for i in range(len(route_db)):
            if tracker.get_slot("budget") == route_db[i]["budget"]:
                route_list=route_db[i]["route"]
                s_route="--".join(route_list)
                s_result="根据您的需求我们为您安排了下面的路线：\n%s"%s_route
                dispatcher.utter_message(s_result)
                break
            if(i==len(route_db)-1):
                dispatcher.utter_message("未能找到您需要的路线，请重新查询")
        return []

class ActionSearchRoute(Action):
    def name(self):
        return "action_searchroute"
    def run(self,dispater,tracker,domain):
# =============================================================================
#         if tracker.get_slot("spot_name")==None and tracker.get_slot("spot_name_1")==None and tracker.get_slot("spot_name_2")==None:
#             dispater.utter_message("请输入您想要去的地点")
#         dispater.utter_message("请稍等，正在为您安排路线")
# =============================================================================
# =============================================================================
#         slot=[]
#         if tracker.get_slot("spot_name")!=None:
#             slot.append(tracker.get_slot("spot_name"))
#         if tracker.get_slot("spot_name_1")!=None:
#             slot.append(tracker.get_slot("spot_name_1"))
#         if tracker.get_slot("spot_name_2")!=None:
#             slot.append(tracker.get_slot("spot_name_2"))
#         if len(slot)==0:
#             dispater.utter_message("请输入您想要去的地点")
#             return []
# =============================================================================
        slot={}
        slot["s1"]=tracker.get_slot("spot_name")
        slot["s2"]=tracker.get_slot("spot_name_1")
        slot["s3"]=tracker.get_slot("spot_name_2")
        if slot["s1"]==None and slot["s2"]==None and slot["s3"]==None:
            dispater.utter_message("请输入您想要去的地点")
            return []
        dispater.utter_message("请稍等，正在为您安排路线")
        for i in range(len(route_db)):
            if slot["s1"]!=None:
                if(slot["s1"] not in route_db[i]["route"]):
                    break
            if slot["s2"]!=None:
                if(slot["s2"] not in route_db[i]["route"]):
                    break
            if slot["s3"]!=None:
                if(slot["s3"] not in route_db[i]["route"]):
                    break
            route=route_db[i]["route"]
            route_s="--".join(route)
            dispater.utter_message("为您推荐以下路线：\n"+route_s)
            return []
        dispater.utter_message("未能找到您需要的路线")
        return []
                    
                    
                    