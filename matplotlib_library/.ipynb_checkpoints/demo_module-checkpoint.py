import numpy as np
import matplotlib.pyplot as plt 

def figurecanvas():
    fig = plt.figure(num=1, figsize=(5, 3), dpi=96, facecolor='cyan', edgecolor='black', linewidth=5);
    ax = fig.add_subplot();
    ax.set_visible(b=False);
    return None
    
def axes():
    fig, ax = plt.subplots(num=2, figsize=(5, 3), dpi=96, facecolor='cyan', edgecolor='black', linewidth=5);
    ax.set_facecolor('yellow');
    return None

def axes_label():
    fig, ax = plt.subplots(num=3, figsize=(5, 3), dpi=96, facecolor='cyan', edgecolor='black', linewidth=5);
    ax.set_facecolor('yellow');
    ax.set_xlabel('x', color='red');
    ax.set_ylabel('y', color='red');
    ax.set_title('y = f(x)', color='red');
    return None

def plot():
    fig, ax = plt.subplots(num=4, figsize=(5, 3), dpi=96, facecolor='cyan', edgecolor='black', linewidth=5);
    ax.set_facecolor('yellow')
    ax.set_xlabel('x', color='red');
    ax.set_ylabel('y', color='red');
    ax.set_title('y = f(x)', color='red');
    ax.scatter(x=np.array([1, 2, 3, 4, 5]), 
               y=np.array([2, 4, 6, 8, 10]), color='blueviolet', s=100);
