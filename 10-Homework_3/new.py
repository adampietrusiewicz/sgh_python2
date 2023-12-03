import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

insurance = pd.read_csv('insurance.csv')
insurance.head()
insurance.info()
insurance.describe()
insurance.columns