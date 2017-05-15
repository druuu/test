from sklearn import datasets
from matplotlib import rcParams

import numpy as np
import pandas as pd
import seaborn as sns

#Set graph fonts
rcParams['font.family'] = 'DejaVu Sans'

#load boston dataset
boston_dataset = datasets.load_boston()
boston_data = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)

boston_sample = boston_data.head(10)
boston_sample
