# -*- coding: UTF-8 -*-

import random

f_raw_data=open("raw_data.txt","w",encoding="utf-8")
f_location=open("hainan_position.txt",encoding="utf-8")
f_activity=open("event.txt",encoding="utf-8")
f_people=open("people.txt",encoding="utf-8")

position=[]
for line in f_location.readlines():
    if("酒店" not in line and "宾馆" not in line):
        line=line.strip()
        position.append(line)
        

trip_activity=[]
for line in f_activity.readlines():
    line=line.strip()
    trip_activity.append(line)

#trip_budget=["省钱","舒适","经济","奢侈"]

s_result=""
s_result+="text,intent,activity\n"
template_1="我想%(activity)s，海南有什么景点推荐吗？|serch_byactivity|%(activity)s\n"
template_2="我想%(activity)s，请给我推荐一些景点。|serch_byactivity|%(activity)s\n"
template_3="海南%(activity)s去什么地方好？|search_byactivity|%(activity)s\n"
template_4="请推荐一些海南可以%(activity)s的景点。|search_byactivity|%(activity)s\n"
template_5="我喜欢%(activity)s，海南去哪些地方比较好？|search_byactivity|%(activity)s\n"
template_6="%(activity)s海南可以去哪些地方？|search_byactivity|%(activity)s\n"
for i in range(25):
    s_result+=template_1%{"activity":random.choice(trip_activity)}
    s_result+=template_2%{"activity":random.choice(trip_activity)}
    s_result+=template_3%{"activity":random.choice(trip_activity)}
    s_result+=template_4%{"activity":random.choice(trip_activity)}
    s_result+=template_5%{"activity":random.choice(trip_activity)}
    s_result+=template_6%{"activity":random.choice(trip_activity)}



# =============================================================================
# s_result+="text,intent,budget\n"
# template_7="我想要一次%(budget)s海南行，能给我提供一条路线吗？|search_bytype|%(budget)s\n"
# template_24="这次去海南我希望%(budget)s一点，能给我提供一条路线吗？|search_bytype|%(budget)s\n"
# for i in range(50):
#     s_result+=template_7%{"budget":random.choice(trip_budget)}
#     s_result+=template_24%{"budget":random.choice(trip_budget)}
# =============================================================================

    
trip_type=['亲子','和父母','和朋友','夫妻','一个人','情侣']
s_result+="text,intent,trip_type\n"
template_9="请给我推荐一条%(trip_type)s海南行的路线。|search_bytype|%(trip_type)s\n"
template_10="请问海南有适合%(trip_type)s出行的路线吗？|search_bytype|%(trip_type)s\n"
template_11="%(trip_type)s旅游海南合适什么样的旅行路线？|search_bytype|%(trip_type)s\n"
for i in range(25):
    s_result+=template_9%{"trip_type":random.choice(trip_type)}
    s_result+=template_10%{"trip_type":random.choice(trip_type)}
    s_result+=template_11%{"trip_type":random.choice(trip_type)}
trip_type_1=['和父母','和朋友',"和女朋友","和男朋友","和老公","和老婆"]
template_12="想要%(trip_type)s去海南旅行，有什么路线推荐？|search_bytype|%(trip_type)s\n"
template_13="要%(trip_type)s一起去海南玩，请问有什么好的路线推荐吗？|search_bytype|%(trip_type)s\n"
for i in range(25):
    s_result+=template_12%{"trip_type":random.choice(trip_type_1)}
    s_result+=template_13%{"trip_type":random.choice(trip_type_1)}


s_result+="text,intent,budget\n"
budget=["2000","3000","4000","5000","6000","7000","8000"]
template_8="这次去海南旅游的预算是人均%(budget)s，能给我推荐一条路线吗？|search_bybudget|%(budget)s\n"
template_23="这次去海南旅游的价格打算控制在%(budget)s以下，该怎么玩？|search_bybudget|%(budget)s\n"
for i in range(50):
    s_result+=template_8%{"budget":random.choice(budget)}
    s_result+=template_23%{"budget":random.choice(budget)}
    


trip_title=['自由行','摄影','人文','小资','省钱','穷游','畅游海岛','购物','周末游','半自由行','徒步','跟团','奢侈','美食','骑行','海滨','邮轮','当地特色','蜜月','自驾']
s_result+="text,intent,trip_title\n"
trip_title_1=["自由行","半自由行","穷游","跟团","自驾","骑行"]
template_14="我们想要以%(trip_title)s的方式游览海南，能给我推荐一条路线吗？|search_bytitle|%(trip_title)s\n"
template_16="想要在海南%(trip_title)s，旅游路线是什么样的？|search_bytitle|%(trip_title)s\n"
for i in range(25):
    s_result+=template_14%{"trip_title":random.choice(trip_title_1)}
    s_result+=template_16%{"trip_title":random.choice(trip_title_1)}    
trip_title_2=["奢侈","省钱"]
template_15="想要拥有一次%(trip_title)s海南旅游体验，路线有什么推荐吗？|search_bytitle|%(trip_title)s\n"
for i in range(25):
    s_result+=template_15%{"trip_title":random.choice(trip_title_2)}
trip_title_3=["蜜月","购物","畅游海岛","摄影"]
template_24="想要在海南%(trip_title)s，旅游路线是什么样的？|search_bytitle|%(trip_title)s\n"
template_26="这次海南行的主题是%(trip_title)s，可以给我推荐一条路线吗？|search_bytitle|%(trip_title)s\n"
for i in range(25):
    s_result+=template_24%{"trip_title":random.choice(trip_title_3)}
    s_result+=template_26%{"trip_title":random.choice(trip_title_3)}
trip_title_4=["畅游海岛","海滨","邮轮","当地特色","美食"]
template_25="想要在海南好好体验一下%(trip_title)s，有什么路线推荐吗？|search_bytitle|%(trip_title)s\n"
template_27="这次旅行的目的是感受一下海南的%(trip_title)s，选什么路线好呢？|search_bytitle|%(trip_title)s\n"
for i in range(25):
    s_result+=template_25%{"trip_title":random.choice(trip_title_4)}
    s_result+=template_27%{"trip_title":random.choice(trip_title_4)}



s_result+="text,intent,spot_name,spot_name_1\n"
template_17="我比较想去%(spot_1)s和%(spot_2)s，可以帮我安排一条路线吗？|search_route|%(spot_1)s,%(spot_2)s\n"
template_18="我想去%(spot_1)s和%(spot_2)s，可以怎么玩？|search_route|%(spot_1)s,%(spot_2)s\n"
template_19="这次旅行计划去%(spot_1)s和%(spot_2)s，应该怎么玩？|search_route|%(spot_1)s,%(spot_2)s\n"
for i in range(25):
    s_result+=template_17%{"spot_1":random.choice(position),"spot_2":random.choice(position)}
    s_result+=template_18%{"spot_1":random.choice(position),"spot_2":random.choice(position)}
    s_result+=template_19%{"spot_1":random.choice(position),"spot_2":random.choice(position)}


s_result+="text,intent,spot_name,spot_name_1,spot_name_2\n"
template_20="我比较想去%(spot_1)s、%(spot_2)s和%(spot_3)s，可以帮我安排一条路线吗？|search_route|%(spot_1)s,%(spot_2)s,%(spot_3)s\n"
template_21="我想去%(spot_1)s，%(spot_2)s和%(spot_3)s，可以怎么玩？|search_route|%(spot_1)s,%(spot_2)s,%(spot_3)s\n"
template_22="这次旅行计划去%(spot_1)s、%(spot_2)s和%(spot_3)s，应该怎么玩？|search_route|%(spot_1)s,%(spot_2)s,%(spot_3)s\n"
for i in range(25):
    s_result+=template_20%{"spot_1":random.choice(position),"spot_2":random.choice(position),"spot_3":random.choice(position)}
    s_result+=template_21%{"spot_1":random.choice(position),"spot_2":random.choice(position),"spot_3":random.choice(position)}
    s_result+=template_22%{"spot_1":random.choice(position),"spot_2":random.choice(position),"spot_3":random.choice(position)}


s_result+="text,intent\n你好|greet\n您好|greet\n您好吗|greet\n嗨|greet\n喂|greet\n再见|goodbye\n拜拜|goodbye\n很高兴和你说话|goodbye\n谢谢你|goodbye\n谢谢您|goodbye\n"
print(s_result)
f_raw_data.write(s_result)
f_activity.close()
f_location.close()
f_people.close()
f_raw_data.close()