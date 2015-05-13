import sys
sys.path.append('/solution')
import matplotlib as mlp
mlp.rcParams['font.family'] = u'NanumGothic'
mlp.rcParams['font.size'] = 10
mlp.rcParams['figure.dpi'] = 160
mlp.rcParams['savefig.dpi'] = 144

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
from wzdat.util import hdf_path, hdf_exists

import os
