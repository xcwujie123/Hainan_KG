#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 20:54:03 2020

@author: didi
"""

import numpy as np
import tensorflow as tf
# =============================================================================
# tf.reset_default_graph()
# entity_embedding = tf.get_variable(name='entity',shape=[1, 2],initializer=tf.random_uniform_initializer(minval=-1,maxval=1))
# with tf.Session() as sess:
#     tf.global_variables_initializer().run()
#     a=entity_embedding.eval(session=sess)
#     np.save("a.npy",a)
# =============================================================================

a=np.load("entity_embedding.npy")
print(a)