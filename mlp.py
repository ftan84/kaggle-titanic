import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
# from keras.callbacks import ModelCheckpoint
from sklearn.model_selection import cross_val_score, GridSearchCV, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def mlp_baseline():
    '''Baseline model

    This is the baseline model which consists of a network with one hidden
    layer consisting of the same number of neurons as input neruons.
    '''
    model = Sequential()
    model.add(Dense())
