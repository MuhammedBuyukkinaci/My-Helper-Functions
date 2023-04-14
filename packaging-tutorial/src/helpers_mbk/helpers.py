import os
import random

import numpy as np
import pandas as pd


def seed_everything(seed=51):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)


def glance_data(path):
    df = pd.read_csv(path)
    print("========")
    print(f"Shape of data = {df.shape}")
    print("========")
    print("Column types are:")
    print(df.dtypes)
    print("========")
    print("Take a glance at data")
    print(pd.concat([df.head(), df.tail()], axis=0))
    print("========")
