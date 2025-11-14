import pickle
import pandas as pd
import os

#バイナリファイルの読み書き
def read_bin(filename):
    with open(filename,'rb') as bf:
        bin_data = pd.read_pickle(bf)
    return bin_data

def save_bin(filename,data):
    with open(filename,'wb') as bf:
        pickle.dump(data,bf)


