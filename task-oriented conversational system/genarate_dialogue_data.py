# -*- coding: UTF-8 -*-
import markdown as md
import random
f_story=open("story.md","w",encoding="utf-8")
s_write=""
intent_list=["search_byactivity","search_bytype","search_route","search_bybudget","search_bytitle"]
action_list=["action_searchbyactivity","action_searchbytype","action_searchroute","action_searchbybudget","action_searchbytitle"]
# =============================================================================
# intent_list=["search_byactivity","search_bytype"]
# action_list=["action_searchbyactivity","action_searchbytype"]
# =============================================================================
index_list=list(range(len(intent_list)))
for i in range(20):
    s_write+="## Generated Story "+str(i+1)+"\n"
    s_write+="* greet\n"+"\t- utter_greet\n"
    for i in range(5):
        index=random.choice(index_list)
        s_write+="* "+intent_list[index]+"\n"
        s_write+="\t- "+action_list[index]+"\n"
    s_write+="* saygoodbye\n"+"\t- utter_goodbye\n"
    s_write+="\n\n"
print(s_write)
f_story.write(s_write)
f_story.close()