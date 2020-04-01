# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings
import jieba
jieba.load_userdict("jieba_userdict.txt")

from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.events import SlotSet
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import (MaxHistoryTrackerFeaturizer,
                                   BinarySingleStateFeaturizer)

from random import choice

logger = logging.getLogger(__name__)


def run_restaurantbot_online(input_channel=ConsoleInputChannel(),
                      interpreter=RasaNLUInterpreter("models/default/model_20190702-213207"),
                      domain_file="hainan_domain.yml",
                      training_data_file="data/story.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), KerasPolicy()],
                  interpreter=interpreter)

    training_data = agent.load_data(training_data_file)
    agent.train_online(training_data,
                       input_channel=input_channel,
                       max_history=2,
                       batch_size=16,
                       epochs=200,
                       max_training_samples=300)

    return agent


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    run_restaurantbot_online()