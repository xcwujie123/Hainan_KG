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
# =============================================================================
# from rasa_core.agent import Agent
# from rasa_core.channels.console import ConsoleInputChannel
# =============================================================================
from rasa_core.events import SlotSet
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import (MaxHistoryTrackerFeaturizer,
                                   BinarySingleStateFeaturizer)

from random import choice

logger = logging.getLogger(__name__)


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer
    import jieba

    jieba.load_userdict("jieba_userdict.txt")
    training_data = load_data("data/train_file_new.json")
    trainer = Trainer(config.load("hainan_nlu_model_config.json"))
    trainer.train(training_data)
    model_directory = trainer.persist("models/")

    return model_directory


if __name__ == "__main__":
    logging.basicConfig(level="INFO")

    train_nlu()