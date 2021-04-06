#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:06:08 2021

@author: nicole
"""

import pandas as pd
import numpy as np
import copy
import category_encoders as ce

hashes_fd = pd.read_csv('hashes-flower-dog-1360.csv')

hashes_fd_ce = hashes_fd.copy()

encoder = ce.BinaryEncoder(cols=['hash'])
df_binary = encoder.fit_transform(hashes_fd_ce)

df_binary.head()
print(df_binary.head())

df_binary.to_csv('df_binary_encoding_1360.csv', index=False)