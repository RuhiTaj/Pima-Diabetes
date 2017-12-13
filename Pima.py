# import all packages
import pandas as pd
from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Loading dataset and to retrieve first 5 rows
dataset = pd.read_csv('pima-indians-diabetes.csv')
dataset.head()