import argparse
import logging
# =============================================================================
# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
# from __future__ import unicode_literals
# =============================================================================

#from policy import RestaurantPolicy
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.mapping_policy import MappingPolicy
agent = Agent("hainan_domain.yml",policies=[MemoizationPolicy(max_history=3),MappingPolicy(),RestaurantPolicy(batch_size=100,epochs=400,validation_split=0.2)])
training_data = agent.load_data("data/stories.md")
agent.train(training_data)
agent.persist("models/dialogue")


# =============================================================================
# agent = Agent()
# data = agent.load_data("data/stories.md")
# agent.train(data)
# =============================================================================
