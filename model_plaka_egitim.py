# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 16:46:35 2021

@author: mecit.sezgin
"""

import numpy as np
import os

from tflite_model_maker.config import ExportFormat
from tflite_model_maker import model_spec
from tflite_model_maker import object_detector

import tensorflow as tf
assert tf.__version__.startswith('2')

tf.get_logger().setLevel('ERROR')
from absl import logging
logging.set_verbosity(logging.ERROR)



#%%
spec = model_spec.get('efficientdet_lite0')

#%%
print("train_data yükleniyor")
train_data= object_detector.DataLoader.from_pascal_voc("plaka_train", "plaka_train",["plaka"])

#%%
print("validation_data yükleniyor")
validation_data= object_detector.DataLoader.from_pascal_voc("plaka_test","plaka_test",["plaka"])


#%%
model = object_detector.create(train_data, model_spec=spec,epochs=100, batch_size=8, train_whole_model=True, validation_data=validation_data)

#%%
eva = model.evaluate(validation_data)
print(eva)

#%%
model.export(export_dir='model_plaka')


#%%
#model.evaluate_tflite('model.tflite', validation_data)















