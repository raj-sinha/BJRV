# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 00:43:50 2017

@author: Vibhav
"""

# read distance_matrix text file

import numpy as np
import _pickle as cPickle

distance_mat = cPickle.load(open("distance_matrix.pkl", "rb" ))