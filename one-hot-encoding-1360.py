#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:41:10 2021

@author: nicole
"""

import pandas as pd
import numpy as np
import copy

hashes_fd = pd.read_csv('hashes-flower-dog-1360.csv')

hashes_fd_onehot = hashes_fd.copy()

hashes_fd_onehot = pd.get_dummies(hashes_fd_onehot, columns=['hash'], prefix=['hash'])

print(hashes_fd_onehot.head())

hashes_fd_onehot.to_csv('df_onehot_encoding_1360.csv', index=False)