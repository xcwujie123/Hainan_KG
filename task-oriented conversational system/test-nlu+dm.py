from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import warnings
import os
import logging.handlers
import logging
import jieba
jieba.load_userdict("jieba_userdict.txt")


agent = Agent.load("models/dialogue",
                   interpreter=RasaNLUInterpreter("models/default/model_20190708-171410"))

LOG_FILE = 'hianan_dialogue.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, encoding='utf-8')
fmt = '%(asctime)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger = logging.getLogger('dialogue')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def search(userid_text):
    userid = "Kiri"
    question = userid_text
    result = agent.handle_message(question,None,None,userid)
    #print("result:",result)
    #agent.handle_message("海南有什么好玩的", None, None, "1")
    response = ''
    if result != []:
        for i in range(len(result)):
            if result[i]['text'] != 'Undefined utter template <utter_restart>.':
                response += result[i]['text'] + '\n'
        response = response.strip()
    else:
        response = '程序错误，没有回答'

    logger.info("ID: " + userid + "\n" +"Question: "+ question + "\n" + "Answer: " + response)

    return response


if __name__ == "__main__":
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)
    while(True):
        print("Response:",search(input("User：")))