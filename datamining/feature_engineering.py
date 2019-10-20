import pandas as pd
import numpy as np

from sklearn.preprocessing import *

def target_encoding(train, test, features):
    '''
    先只支持dataframe格式的文件
    :param train:
    :param test:
    :param features:
    :return:
    '''
    assert type(train).__name__ == 'DataFrame'
    pass

def one_hot_encoding(train, test, features):
    pass

if __name__ == '__main__':
    d = pd.DataFrame()
    print(type(d).__name__)