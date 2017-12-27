import os
import random
import numpy as np
import cv2
import math
## data_root_dir + each line of data_list should be the path of an image
data_root_dir = 'data/'
data_list = 'txt/webface_list.txt' 

BATCH_SIZE = 100
M_VALUE = 4

basic_learning_rate = 0.1
weight_decay = 0.0005
step_value = [16000, 20000, 24000]
max_iter = 28000
factor = 0.1

lambda_base = 1000
lambda_gamma = 0.12
lambda_power = 1
lambda_min = 5
begin_iteration = 0


## change the following variable before you run "python get_lfw_features.py"
test_data_dir = '/home/idealsee/github/sphereface_tensorflow_a-softmax/lfw_evaluation/lfw-112X96'
test_list = '../lfw_evaluation/lfw_list.txt'
test_ckpt_model = './ckpt/28000model.ckpt'