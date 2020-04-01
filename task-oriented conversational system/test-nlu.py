# -*- coding: UTF-8 -*-
import json
import jieba
jieba.load_userdict("jieba_userdict.txt")

#from klein import Klein
from rasa_nlu import config


class ItemStore(object):
    #app = Klein()

    def __init__(self, model_dir):
        from rasa_nlu.model import Metadata, Interpreter
        self.interpreter = Interpreter.load(model_dir)
        self._items = {}

    def test(self, data):

        result = {}

        pred = self.interpreter.parse(data)
        result['text'] = data
        result["intent"] = pred.get("intent").get("name")
        #result["intent"] = pred.get("intent")

        entities = pred.get("entities")
        entities_res = {}
        for entitie in entities:
            name = entitie.get("entity")
            value = entitie.get("value")
            '''
            if name == "info":
                if "phone" in value:
                    value = "phone"
                elif "address" in value:
                    value = "address"
                elif "food" in value:
                    value = "food"
            elif name == "area":
            '''
            entities_res.setdefault(name, value)
        result["entities"] = entities_res

        print(result)
        return result


if __name__ == '__main__':
    #model_dir = "models/default/model_20180928-033359"
    model_dir = "models/default/model_20190708-171410"
    #model_dir = "models/default/model_20181227-015909"
    store = ItemStore(model_dir)
    while True:
        output = store.test(input("请输入："))
