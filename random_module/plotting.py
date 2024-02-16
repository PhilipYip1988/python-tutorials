import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
import random
import math
#%% Constants
tau = math.tau
#%% Plot1
def plot1():
    nums = [random.uniform(a=0, b=10) 
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    return fig
#%% Plot2
def plot2():
    nums = [random.triangular(low=0, high=10) 
            for 
            num 
            in 
            range (100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    return fig
#%% Plot3
def plot3():
    nums = [random.gauss(mu=0, sigma=1) 
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    ax.set_xlim(left=-10, right=10)
    return fig
#%% Plot4
def plot4():
    nums1 = [random.gauss(mu=0, sigma=1) 
             for 
             num 
             in 
             range(100000)]
    nums2 = [random.gauss(mu=0, sigma=2) 
            for 
            num 
            in 
            range(100000)]
    nums3 = [random.gauss(mu=0, sigma=3) 
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums1, bins=100, color='seagreen', alpha=0.5, label='sigma=1')
    ax.hist(nums2, bins=100, color='royalblue', alpha=0.3, label='sigma=2')
    ax.hist(nums3, bins=100, color='tomato', alpha=0.1, label='sigma=3')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    ax.set_xlim(left=-10, right=10)
    return fig
#%% Plot5
def plot5():
    nums = [random.lognormvariate(mu=0, sigma=1) 
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    ax.set_xlim(left=0, right=10)
    return fig
#%% Plot6
def plot6():
    nums = [random.expovariate(lambd=1/5)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    ax.set_xlim(left=0, right=30)
    return fig
#%% Plot7
def plot7():
    nums = [random.expovariate(lambd=-1/5)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    ax.set_xlim(left=-30, right=0)
    return fig
#%% Plot8
def plot8():
    nums = [random.gammavariate(alpha=1, beta=5)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    ax.set_xlim(left=0, right=30)
    return fig
#%% Plot9
def plot9():
    nums = [random.gammavariate(alpha=2, beta=5)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    ax.set_xlim(left=0, right=55)
    return fig
#%% Plot10
def plot10():
    nums = [random.gammavariate(alpha=3, beta=5)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    ax.set_xlim(left=0, right=55)
    return fig
#%% Plot11
def plot11():
    nums = [random.gammavariate(alpha=100000, beta=5)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    return fig
#%% Plot12
def plot12():
    nums = [random.betavariate(alpha=1, beta=1)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    #ax.set_xlim(left=0, right=55)
    return fig
#%% Plot13
def plot13():
    nums = [random.betavariate(alpha=1, beta=5)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    #ax.set_xlim(left=0, right=55)
    return fig
#%% Plot14
def plot14():
    nums = [random.betavariate(alpha=5, beta=5)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    #ax.set_xlim(left=0, right=55)
    return fig
#%% Plot15
def plot15():
    nums = [random.paretovariate(alpha=1.161)
            for 
            num 
            in 
            range(100)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    ax.set_xlim(left=0, right=100)
    return fig
#%% Plot16
def plot16():
    nums = [random.weibullvariate(alpha=1, beta=0.5)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    #ax.set_xlim(left=0, right=100)
    return fig
#%% Plot17
def plot17():
    nums = [random.weibullvariate(alpha=1, beta=1)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    #ax.set_xlim(left=0, right=100)
    return fig
#%% Plot18
def plot18():
    nums = [random.weibullvariate(alpha=1, beta=2)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    #ax.set_xlim(left=0, right=100)
    return fig
#%% Plot19
def plot19():
    nums = [random.weibullvariate(alpha=1, beta=3)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    #ax.set_xlim(left=0, right=100)
    return fig
#%% Plot20
def plot20():
    nums1 = [random.weibullvariate(alpha=1, beta=3)
             for 
             num 
             in 
             range(100000)]
    nums2 = [random.weibullvariate(alpha=2, beta=3)
            for 
            num 
            in 
            range(100000)]
    nums3 = [random.weibullvariate(alpha=3, beta=3)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums1, bins=100, color='seagreen', alpha=0.3, label='sigma=1')
    ax.hist(nums2, bins=100, color='royalblue', alpha=0.3, label='sigma=2')
    ax.hist(nums3, bins=100, color='tomato', alpha=0.3, label='sigma=3')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    ax.set_xlim(left=0, right=7)
    return fig
#%% Plot21
def plot21():
    nums = [random.vonmisesvariate(mu=math.tau/4, kappa=0)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    #ax.set_xlim(left=0, right=100)
    return fig
#%% Plot22
def plot22():
    nums = [random.vonmisesvariate(mu=math.tau/4, kappa=0)
            for 
            num 
            in 
            range(100000)]
    fig, ax = plt.subplots()
    ax.hist(nums, bins=100, color='seagreen')
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    xticks = np.arange(0, tau+tau/16, tau/16)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(17)]
    ax.xaxis.set_ticks(xticks)
    ax.set_xticklabels(xticklabels) 
    return fig
#%% Plot23
def plot23():
    nums = [random.vonmisesvariate(mu=math.tau/4, kappa=0)
            for 
            num 
            in 
            range(100000)]
    counts, angles = np.histogram(nums, bins=100)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.scatter(angles[1:], counts, color='seagreen')
    xticks = np.arange(0, 360, 22.5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(16)]
    ax.set_thetagrids(xticks)
    ax.set_xticklabels(xticklabels) 
    return fig
#%% Plot24
def plot24():
    nums = [random.vonmisesvariate(mu=math.tau/4, kappa=1)
            for 
            num 
            in 
            range(100000)]
    counts, angles = np.histogram(nums, bins=100)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.scatter(angles[1:], counts, color='seagreen')
    xticks = np.arange(0, 360, 22.5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(16)]
    ax.set_thetagrids(xticks)
    ax.set_xticklabels(xticklabels) 
    return fig
#%% Plot25
def plot25():
    nums = [random.vonmisesvariate(mu=math.tau/4, kappa=2)
            for 
            num 
            in 
            range(100000)]
    counts, angles = np.histogram(nums, bins=100)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.scatter(angles[1:], counts, color='seagreen')
    xticks = np.arange(0, 360, 22.5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(16)]
    ax.set_thetagrids(xticks)
    ax.set_xticklabels(xticklabels) 
    return fig