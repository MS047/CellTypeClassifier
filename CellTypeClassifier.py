# -*- coding utf-8 -*-

# This script allows to use a scikit-learn.org classifier (supervised or unsupervised),
# in order to sort kilosort/phy generated units according to their cell type
# using their features, extracted thanks to the DataManager class written in FeaturesExtraction.py.

# Maxime Beau, 2017-05-10

import FeaturesExtraction as fe

import numpy as np

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

import os, sys



