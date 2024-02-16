import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set_style('whitegrid')
import statistics as st

def plot1():
    df = {'data5': np.array([1, 2, 3, 4]),
          'data6': np.array([1, 2, 3, 2])}
    sns.scatterplot(data=df, x='data5', y='data6')
    
def plot2():
    df = {'data5': np.array([1, 2, 3, 4]),
          'data6': np.array([1, 2, 3, 2])}
    sns.scatterplot(data=df, x='data5', y='data6')
    lin_fit = st.linear_regression(df['data5'], df['data6'])
    yp = []
    for x in df['data5']:
        yp.append(lin_fit.slope * x + lin_fit.intercept)
    df['yp'] = yp
    sns.lineplot(df, x='data5', y='yp', color='red')