#%% Imports
import math
import cmath
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
#%% Set Style
sns.set_style('whitegrid')
#%% Constants
tau = 2 * math.pi

#%% Figure1
def plot1():
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, tau/8)
    r2 = (0, 1)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='royalblue')
    ax.plot(theta2, r2, color='red')    
    xticks = ax.xaxis.get_ticklocs()
    xticklabels = [r'$\frac{' + f'{num}' + '}{8}$' + r'$\tau$' for num in range(8)]
    ax.xaxis.set_ticks(xticks)
    ax.set_xticklabels(xticklabels) 
    ax.set_rticks([0, 0.5, 1])
    ax.set_rlabel_position(45)
    return fig

#%% Figure2
def plot2():
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, tau/8)
    r2 = (0, 1)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='royalblue')
    ax.plot(theta2, r2, color='red')
    ax.set_rticks([0, 0.5, 1])
    ax.set_rlabel_position(45)
    return fig
# %% Figure 3
def factorial(factor):
    result = 1
    for num in range(2, factor+1):
        result *= num
    return result

def euler_series(factor):
    total = 1.0
    for num in range(1, factor + 1):
        total += 1.0 / factorial(num)
    return total

def plot3():
    x = np.arange(100)
    y = map(euler_series, x)
    y = np.array(list(y))
    fig, ax = plt.subplots()
    ax.plot(x, y, color='royalblue')
    ax.set_xlabel('factorial')
    ax.set_ylabel('euler_series(factorial)')
    return fig
# %% Figure 4
def plot4():
    x1 = list(range(0, 6))
    y1 = list(map(math.factorial, x1))

    x2 = (np.arange(1, 6.1, 0.1)).tolist()
    y2 = list(map(math.gamma, x2)) 
    x2 = np.arange(1, 6.1, 0.1) - 1

    fig, ax = plt.subplots()
    ax.scatter(x1, y1, color='tomato', label='n!')
    ax.plot(x2, y2, color='royalblue', label=r'$\Gamma$(n+1)')
    ax.set_label('n')
    ax.legend()
    return fig
# %% Figure 5
def plot5():
    x1 = list(range(0, 11))
    y1 = list(map(math.factorial, x1))

    x2 = (np.arange(1, 11.1, 0.1)).tolist()
    y2 = list(map(math.gamma, x2)) 
    x2 = np.arange(1, 11.1, 0.1) - 1

    fig, ax = plt.subplots()
    ax.scatter(x1, y1, color='tomato', label='n!')
    ax.plot(x2, y2, color='royalblue', label=r'$\Gamma$(n+1)')
    ax.set_label('n')
    ax.legend()
    return fig
# %% Figure 6
def plot6():
    x1 = list(range(0, 11))
    y1 = list(map(math.factorial, x1))

    x2 = (np.arange(1, 11.1, 0.1)).tolist()
    y2 = list(map(math.gamma, x2)) 
    x2 = np.arange(1, 11.1, 0.1) - 1

    fig, ax = plt.subplots()
    ax.scatter(x1, y1, color='tomato', label='n!')
    ax.plot(x2, y2, color='royalblue', label=r'$\Gamma$(n+1)')
    ax.set_label('n')
    ax.legend()
    ax.set_yscale('log')
    return fig

# %% Figure 7
def plot7():
    fig, ax = plt.subplots(subplot_kw={'aspect':'equal'})
    ax.set_xlim(left=0, right=6)
    ax.set_ylim(bottom=0, top=6)
    x1 = (4, 4)
    y1 = (1, 5)
    x2 = (1, 4)
    y2 = (1, 1)
    x3 = (1, 4)
    y3 = (1, 5)
    ax.plot(x1, y1, color='cyan', lw=2, ls=':')
    ax.plot(x2, y2, color='magenta', lw=2, ls=':')
    ax.plot(x3, y3, color='tomato', lw=2, ls=':')
    return fig
# %% Figure 8
def plot8():
    fig, ax = plt.subplots(subplot_kw={'aspect':'equal'})
    ax.set_xlim(left=0, right=6)
    ax.set_ylim(bottom=0, top=6)
    x1 = (1, 4)
    y1 = (1, 5)
    x2 = (1, 4)
    y2 = (1, 5)
    ax.plot(x1, y1, color='tomato', lw=2, ls=':')
    ax.scatter(x2, y2, color='royalblue', s=50)
    return fig
# %% Figure 9
def plot9():
    fig, ax = plt.subplots(subplot_kw={'aspect':'equal'})
    ax.set_xlim(left=0, right=6)
    ax.set_ylim(bottom=0, top=6)
    x1 = (4, 4)
    y1 = (1, 5)
    x2 = (1, 4)
    y2 = (1, 1)
    x3 = (1, 4)
    y3 = (1, 5)
    x4 = (1, 4)
    y4 = (1, 5)
    ax.plot(x1, y1, color='cyan', lw=2, ls=':')
    ax.plot(x2, y2, color='magenta', lw=2, ls=':')
    ax.plot(x3, y3, color='tomato', lw=2, ls=':')
    ax.scatter(x4, y4, color='royalblue', s=50)
    return fig
#%% Figure 10
def plot10():
    fig, ax = plt.subplots(subplot_kw={'projection':'3d', 'aspect':'equal'})
    x1 = (3, 1)
    y1 = (4, 1)
    z1 = (7, 1)
    x2 = (1, 3)
    y2 = (1, 1)
    z2 = (1, 1)
    x3 = (1, 1)
    y3 = (1, 4)
    z3 = (1, 1)
    x4 = (1, 1)
    y4 = (1, 1)
    z4 = (1, 7)
    x5 = (1, 3)
    y5 = (1, 4)
    z5 = (1, 7)
    ax.scatter3D(x1, y1, z1, s=50, color='royalblue')
    ax.plot3D(x2, y2, z2, color='magenta', lw=2, ls=':')
    ax.plot3D(x3, y3, z3, color='cyan', lw=2, ls=':')
    ax.plot3D(x4, y4, z4, color='seagreen', lw=2, ls=':')
    ax.plot3D(x5, y5, z5, color='tomato', lw=2, ls='-')
    ax.set_xlim(left=0, right=7)
    ax.set_ylim(bottom=0, top=7)
    ax.set_zlim(bottom=0, top=7)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    return fig
#%% Figure 11
def plot11():
    fig, ax = plt.subplots(subplot_kw={'aspect':'equal'})
    r = 1
    theta = np.arange(-tau, tau, 0.1)
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    ax.plot(x, y, color='royalblue')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(left=-1.5, right=1.5)
    ax.set_ylim(bottom=-1.5, top=1.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    return fig
#%% Figure12
def plot12():
    angle = 2*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='royalblue')
    ax.plot(theta2, r2, color='tomato') 
    ax.scatter(theta3, r3, s=50, color='tomato')
    ax.plot(theta4, r4, color='magenta', lw=2, ls=':')
    ax.plot(theta5, r5, color='cyan', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax.set_thetagrids(xticks)
    ax.set_xticklabels(xticklabels) 
    ax.set_rticks([0, 0.5, 1])
    ax.set_rlabel_position(45)
    ax.set_thetamin(0)
    ax.set_thetamax(90)
    theta6 = 0
    r6 = 0
    ax.annotate('adjacent',
                xy=(0.1, math.cos(angle)/2-0.02),  # theta, radius
                xytext=(0.1, math.cos(angle)/2-0.02),
                color='magenta')
    ax.annotate('opposite',
                xy=(angle-0.5, math.cos(angle)-0.02),  # theta, radius
                xytext=(angle-0.5, math.cos(angle)-0.02),
                color='cyan', rotation=90)
    ax.annotate('hypotenuse',
            xy=(angle-0.1, math.cos(angle)/2-0.01),  # theta, radius
            xytext=(angle-0.1, math.cos(angle)/2-0.01),
            color='red', rotation=45)
    ax.annotate(r'$\theta$',
                xy=(0.3, 0.1),  # theta, radius
                xytext=(0.3, 0.1),
                color='black')
#%% Figure13
def plot13():
    angle = 0*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='royalblue')
    ax.plot(theta4, r4, color='magenta', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax.set_thetagrids(xticks)
    ax.set_xticklabels(xticklabels) 
    ax.set_rticks([0, 0.5, 1])
    ax.set_rlabel_position(45)
    ax.set_thetamin(0)
    ax.set_thetamax(90)
    theta6 = 0
    r6 = 0
    return fig
#%% Figure14
def plot14():
    angle = 1*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='royalblue')
    ax.plot(theta2, r2, color='tomato') 
    ax.scatter(theta3, r3, s=50, color='tomato')
    ax.plot(theta4, r4, color='magenta', lw=2, ls=':')
    ax.plot(theta5, r5, color='cyan', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax.set_thetagrids(xticks)
    ax.set_xticklabels(xticklabels) 
    ax.set_rticks([0, 0.5, 1])
    ax.set_rlabel_position(45)
    ax.set_thetamin(0)
    ax.set_thetamax(90)
    theta6 = 0
    r6 = 0
    ax.annotate('adjacent',
                xy=(0.1, math.cos(angle)/2-0.02),  # theta, radius
                xytext=(0.1, math.cos(angle)/2-0.02),
                color='magenta')
    ax.annotate('opposite',
                xy=(angle-0.26, math.cos(angle)-0.06),  # theta, radius
                xytext=(angle-0.26, math.cos(angle)-0.06),
                color='cyan', rotation=90)
    ax.annotate('hypotenuse',
            xy=(angle-0.1, math.cos(angle)/2-0.01),  # theta, radius
            xytext=(angle-0.1, math.cos(angle)/2-0.01),
            color='red', rotation=22.5)
    ax.annotate(r'$\theta$',
                xy=(0.1, 0.1),  # theta, radius
                xytext=(0.1, 0.1),
                color='black')
    return fig
#%% Figure15
def plot15():
    angle = 3*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='royalblue')
    ax.plot(theta2, r2, color='tomato') 
    ax.scatter(theta3, r3, s=50, color='tomato')
    ax.plot(theta4, r4, color='magenta', lw=2, ls=':')
    ax.plot(theta5, r5, color='cyan', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax.set_thetagrids(xticks)
    ax.set_xticklabels(xticklabels) 
    ax.set_rticks([0, 0.5, 1])
    ax.set_rlabel_position(45)
    ax.set_thetamin(0)
    ax.set_thetamax(90)
    theta6 = 0
    r6 = 0
    ax.annotate('adjacent',
                xy=(0.1, math.cos(angle)/2-0.02),  # theta, radius
                xytext=(0.1, math.cos(angle)/2-0.02),
                color='magenta')
    ax.annotate('opposite',
                xy=(angle-0.3, math.sin(angle)-0.4),  # theta, radius
                xytext=(angle-0.3, math.sin(angle)-0.4),
                color='cyan', rotation=90)
    ax.annotate('hypotenuse',
            xy=(angle-0.05, math.cos(angle)/2+0.2),  # theta, radius
            xytext=(angle-0.05, math.cos(angle)/2+0.2),
            color='red', rotation=67.5)
    ax.annotate(r'$\theta$',
                xy=(0.5, 0.04),  # theta, radius
                xytext=(0.5, 0.04),
                color='black')
    return fig
#%% Figure16
def plot16():
    fig, ax = plt.subplots(1, 2, subplot_kw={'projection': 'polar'})
    angle = 1*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    ax[1].plot(theta, r, color='royalblue')
    ax[1].plot(theta2, r2, color='tomato') 
    ax[1].scatter(theta3, r3, s=50, color='tomato')
    ax[1].plot(theta4, r4, color='magenta', lw=2, ls=':')
    ax[1].plot(theta5, r5, color='cyan', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax[1].set_thetagrids(xticks)
    ax[1].set_xticklabels(xticklabels) 
    ax[1].set_rticks([0, 0.5, 1])
    ax[1].set_rlabel_position(45)
    ax[1].set_thetamin(0)
    ax[1].set_thetamax(90)
    theta6 = 0
    r6 = 0
    ax[1].annotate('adjacent',
            xy=(0.1, math.cos(angle)/2-0.02),  # theta, radius
            xytext=(0.1, math.cos(angle)/2-0.02),
            color='magenta')
    ax[1].annotate('opposite',
            xy=(angle-0.26, math.cos(angle)-0.06),  # theta, radius
            xytext=(angle-0.26, math.cos(angle)-0.06),
            color='cyan', rotation=90)
    ax[1].annotate('hypotenuse',
            xy=(angle-0.1, math.cos(angle)/2-0.01),  # theta, radius
            xytext=(angle-0.1, math.cos(angle)/2-0.01),
            color='red', rotation=22.5)
    ax[1].annotate(r'$\theta$',
            xy=(0.1, 0.1),  # theta, radius
            xytext=(0.1, 0.1),
            color='black')
    angle = 3*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    ax[0].plot(theta, r, color='royalblue')
    ax[0].plot(theta2, r2, color='tomato') 
    ax[0].scatter(theta3, r3, s=50, color='tomato')
    ax[0].plot(theta4, r4, color='magenta', lw=2, ls=':')
    ax[0].plot(theta5, r5, color='cyan', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax[0].set_thetagrids(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[0].set_rticks([0, 0.5, 1])
    ax[0].set_rlabel_position(45)
    ax[0].set_thetamin(0)
    ax[0].set_thetamax(90)
    theta6 = 0
    r6 = 0
    ax[0].annotate('adjacent',
            xy=(0.1, math.cos(angle)/2-0.02),  # theta, radius
            xytext=(0.1, math.cos(angle)/2-0.02),
            color='magenta')
    ax[0].annotate('opposite',
            xy=(angle-0.3, math.sin(angle)-0.4),  # theta, radius
            xytext=(angle-0.3, math.sin(angle)-0.4),
            color='cyan', rotation=90)
    ax[0].annotate('hypotenuse',
            xy=(angle-0.05, math.cos(angle)/2+0.2),  # theta, radius
            xytext=(angle-0.05, math.cos(angle)/2+0.2),
            color='red', rotation=67.5)
    ax[0].annotate(r'$\theta$',
            xy=(0.5, 0.04),  # theta, radius
            xytext=(0.5, 0.04),
            color='black')
    angle = 3*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    ax[0].plot(theta, r, color='royalblue')
    ax[0].plot(theta2, r2, color='tomato') 
    ax[0].scatter(theta3, r3, s=50, color='tomato')
    ax[0].plot(theta4, r4, color='magenta', lw=2, ls=':')
    ax[0].plot(theta5, r5, color='cyan', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax[0].set_thetagrids(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[0].set_rticks([0, 0.5, 1])
    ax[0].set_rlabel_position(45)
    ax[0].set_thetamin(0)
    ax[0].set_thetamax(90)
    theta6 = 0
    r6 = 0
    ax[0].annotate('adjacent',
                xy=(0.1, math.cos(angle)/2-0.02),  # theta, radius
                xytext=(0.1, math.cos(angle)/2-0.02),
                color='magenta')
    ax[0].annotate('opposite',
                xy=(angle-0.3, math.sin(angle)-0.4),  # theta, radius
                xytext=(angle-0.3, math.sin(angle)-0.4),
                color='cyan', rotation=90)
    ax[0].annotate('hypotenuse',
            xy=(angle-0.05, math.cos(angle)/2+0.2),  # theta, radius
            xytext=(angle-0.05, math.cos(angle)/2+0.2),
            color='red', rotation=67.5)
    ax[0].annotate(r'$\theta$',
                xy=(0.5, 0.04),  # theta, radius
                xytext=(0.5, 0.04),
                color='black')
    return fig
#%% Figure17
def plot17():
    angle = 4*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='royalblue')
    ax.plot(theta5, r5, color='cyan', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax.set_thetagrids(xticks)
    ax.set_xticklabels(xticklabels) 
    ax.set_rticks([0, 0.5, 1])
    ax.set_rlabel_position(45)
    ax.set_thetamin(0)
    ax.set_thetamax(90)
    theta6 = 0
    r6 = 0
    return fig
#%% Figure18
def plot18():
    fig, ax = plt.subplots(1, 2, subplot_kw={'projection': 'polar'})
    angle = 4*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    ax[0].plot(theta, r, color='royalblue')
    ax[0].plot(theta5, r5, color='cyan', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax[0].set_thetagrids(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[0].set_rticks([0, 0.5, 1])
    ax[0].set_rlabel_position(45)
    ax[0].set_thetamin(0)
    ax[0].set_thetamax(90)
    theta6 = 0
    r6 = 0
    angle = 0*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    ax[1].plot(theta, r, color='royalblue')
    ax[1].plot(theta4, r4, color='magenta', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax[1].set_thetagrids(xticks)
    ax[1].set_xticklabels(xticklabels) 
    ax[1].set_rticks([0, 0.5, 1])
    ax[1].set_rlabel_position(45)
    ax[1].set_thetamin(0)
    ax[1].set_thetamax(90)
    theta6 = 0
    r6 = 0
    return fig
#%% Figure19
def plot19():
    fig, ax = plt.subplots(1, 2)
    theta = np.linspace(0, 4*tau/16, 5)
    y = np.sin(theta)
    x = np.cos(theta)
    ax[0].scatter(theta, y, s=50, c='cyan')
    ax[0].set_xlabel(r'$\theta$')
    ax[0].set_ylabel('y')
    ax[1].scatter(theta, x, s=50, c='magenta')
    ax[1].set_xlabel(r'$\theta$')
    ax[1].set_ylabel('x')
    xticks = np.linspace(0, 4*tau/16, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax[0].xaxis.set_ticks(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[1].xaxis.set_ticks(xticks)
    ax[1].set_xticklabels(xticklabels) 
    return fig

#%% Figure 20
def plot20():
    fig, ax = plt.subplots(subplot_kw={'aspect':'equal'})
    r = 1
    theta = np.arange(-tau, tau, 0.1)
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    ax.plot(x, y, color='royalblue')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(left=-1.5, right=1.5)
    ax.set_ylim(bottom=-1.5, top=1.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    theta = 2 * tau/16
    y = r * np.sin(theta)
    x = r * np.cos(theta)
    ax.scatter(x, y, s=50, color='tomato')
    theta = 6 * tau/16
    y = r * np.sin(theta)
    x = r * np.cos(theta)
    ax.scatter(x, y, s=50, color='tomato')
    theta = 10 * tau/16
    y = r * np.sin(theta)
    x = r * np.cos(theta)
    ax.scatter(x, y, s=50, color='tomato') 
    theta = 14 * tau/16
    y = r * np.sin(theta)
    x = r * np.cos(theta)
    ax.scatter(x, y, s=50, color='tomato')
    return fig

#%% Figure 21
def plot21():
    fig, ax = plt.subplots(1, 2, subplot_kw={'projection': 'polar'})
    angle = 1*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    ax[0].plot(theta, r, color='royalblue')
    ax[0].plot(theta2, r2, color='tomato') 
    ax[0].scatter(theta3, r3, s=50, color='tomato')
    ax[0].plot(theta4, r4, color='magenta', lw=2, ls=':')
    ax[0].plot(theta5, r5, color='cyan', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax[0].set_thetagrids(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[0].set_rticks([0, 0.5, 1])
    ax[0].set_rlabel_position(45)
    ax[0].set_thetamin(0)
    ax[0].set_thetamax(90)
    theta6 = 0
    r6 = 0
    ax[0].annotate('adjacent',
            xy=(0.1, math.cos(angle)/2-0.02),  # theta, radius
            xytext=(0.1, math.cos(angle)/2-0.02),
            color='magenta')
    ax[0].annotate('opposite',
            xy=(angle-0.26, math.cos(angle)-0.06),  # theta, radius
            xytext=(angle-0.26, math.cos(angle)-0.06),
            color='cyan', rotation=90)
    ax[0].annotate('hypotenuse',
            xy=(angle-0.1, math.cos(angle)/2-0.01),  # theta, radius
            xytext=(angle-0.1, math.cos(angle)/2-0.01),
            color='red', rotation=22.5)
    ax[0].annotate(r'$\theta$',
            xy=(0.1, 0.1),  # theta, radius
            xytext=(0.1, 0.1),
            color='black')

    angle = 5*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    ax[1].plot(theta, r, color='royalblue')
    ax[1].plot(theta2, r2, color='tomato') 
    ax[1].scatter(theta3, r3, s=50, color='tomato')
    xticks = np.linspace(90, 180, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(4, 9)]
    ax[1].set_thetagrids(xticks)
    ax[1].set_xticklabels(xticklabels) 
    ax[1].set_rticks([0, 0.5, 1])
    ax[1].set_rlabel_position(45)
    ax[1].set_thetamin(90)
    ax[1].set_thetamax(180)
    theta6 = 0
    r6 = 0
    fig.tight_layout()
    return fig
#%% Figure22
def plot22():
    fig, ax = plt.subplots(1, 2)
    theta = np.linspace(0, 16*tau/16, 17)
    y = np.sin(theta)
    x = np.cos(theta)
    ax[0].scatter(theta, y, s=50, c='cyan')
    ax[0].set_xlabel(r'$\theta$')
    ax[0].set_ylabel('y')
    ax[1].scatter(theta, x, s=50, c='magenta')
    ax[1].set_xlabel(r'$\theta$')
    ax[1].set_ylabel('x')
    xticks = np.linspace(0, 16*tau/16, 9)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(0, 17, 2)]
    ax[0].xaxis.set_ticks(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[1].xaxis.set_ticks(xticks)
    ax[1].set_xticklabels(xticklabels) 
    fig.tight_layout()
    return fig
#%% Figure23
def plot23():
    fig, ax = plt.subplots(1, 1)
    theta = np.linspace(0, 16*tau/16, 17)
    ratio = np.tan(theta)
    ax.scatter(theta, ratio, s=50, c='orange')
    ax.set_xlabel(r'$\theta$')
    ax.set_ylabel(r'$\frac{y}{x}$')
    xticks = np.linspace(0, 16*tau/16, 9)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(0, 17, 2)]
    ax.xaxis.set_ticks(xticks)
    ax.set_xticklabels(xticklabels)
    ax.set_ylim(bottom=-5, top=5) 
    fig.tight_layout()
    return fig
#%% Figure24
def plot24():
    fig, ax = plt.subplots(2, 1)
    theta = np.linspace(0, 16*tau/16, 17)
    y = np.sin(theta)
    x = np.cos(theta)
    ax[0].scatter(theta, y, s=50, c='cyan', label='y')
    ax[0].scatter(theta, x, s=50, c='magenta', label='x')
    ax[0].set_xlabel(r'$\theta$')
    xticks = np.linspace(0, 16*tau/16, 9)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(0, 17, 2)]
    ax[0].xaxis.set_ticks(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[0].legend()
    ratio = np.tan(theta)
    ax[1].scatter(theta, ratio, s=50, c='orange')
    ax[1].set_xlabel(r'$\theta$')
    ax[1].set_ylabel(r'$\frac{y}{x}$')
    xticks = np.linspace(0, 16*tau/16, 9)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(0, 17, 2)]
    ax[1].xaxis.set_ticks(xticks)
    ax[1].set_xticklabels(xticklabels)
    ax[1].set_ylim(bottom=-5, top=5) 
    fig.tight_layout()
    return fig
#%% Figure25
def plot25():
    fig, ax = plt.subplots(2, 1)
    theta = np.linspace(-8*tau/16, 8*tau/16, 17)
    y = np.sin(theta)
    x = np.cos(theta)
    ax[0].scatter(theta, y, s=50, c='cyan', label='y')
    ax[0].scatter(theta, x, s=50, c='magenta', label='x')
    ax[0].set_xlabel(r'$\theta$')
    xticks = np.linspace(-8*tau/16, 8*tau/16, 9)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(-8, 9, 2)]
    ax[0].xaxis.set_ticks(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[0].legend()
    ratio = np.tan(theta)
    ax[1].scatter(theta, ratio, s=50, c='orange')
    ax[1].set_xlabel(r'$\theta$')
    ax[1].set_ylabel(r'$\frac{y}{x}$')
    xticks = np.linspace(-8*tau/16, 8*tau/16, 9)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(-8, 9, 2)]
    ax[1].xaxis.set_ticks(xticks)
    ax[1].set_xticklabels(xticklabels)
    ax[1].set_ylim(bottom=-5, top=5) 
    fig.tight_layout()
    return fig
#%% Figure26
def plot26():
    fig, ax = plt.subplots(2, 1)
    theta = np.linspace(-8*tau/16, 8*tau/16, 17)
    y = np.sin(theta) ** 2
    x = np.cos(theta) ** 2
    ax[0].scatter(theta, y, s=50, c='cyan', label=r'$y^{2}$')
    ax[0].scatter(theta, x, s=50, c='magenta', label=r'$x^{2}$')
    ax[0].set_xlabel(r'$\theta$')
    xticks = np.linspace(-8*tau/16, 8*tau/16, 9)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(-8, 9, 2)]
    ax[0].xaxis.set_ticks(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[0].legend()
    ratio = np.tan(theta) ** 2
    ax[1].scatter(theta, ratio, s=50, c='orange')
    ax[1].set_xlabel(r'$\theta$')
    ax[1].set_ylabel(r'$\frac{y^{2}}{x^{2}}$')
    xticks = np.linspace(-8*tau/16, 8*tau/16, 9)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(-8, 9, 2)]
    ax[1].xaxis.set_ticks(xticks)
    ax[1].set_xticklabels(xticklabels)
    ax[1].set_ylim(bottom=0, top=5) 
    fig.tight_layout()
    return fig
#%% Figure27
def plot27():
    fig, ax = plt.subplots(2, 1)
    theta = np.linspace(-4*tau/16, 4*tau/16, 9)
    y = np.sin(theta)
    x = np.cos(theta)
    ax[0].plot(theta, y, color='cyan', label='y')
    ax[0].plot(theta, x, color='magenta', label='x')
    ax[0].set_xlabel(r'$\theta$')
    xticks = np.linspace(-4*tau/16, 4*tau/16, 9)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(-4, 5, 1)]
    ax[0].xaxis.set_ticks(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[0].legend()
    ratio = np.tan(theta)
    ax[1].plot(theta, ratio, color='orange')
    ax[1].set_xlabel(r'$\theta$')
    ax[1].set_ylabel(r'$\frac{y}{x}$')
    xticks = np.linspace(-4*tau/16, 4*tau/16, 9)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(-4, 5, 1)]
    ax[1].xaxis.set_ticks(xticks)
    ax[1].set_xticklabels(xticklabels)
    ax[1].set_ylim(bottom=-5, top=5) 
    fig.tight_layout()
    return fig
#%% Figure28
def plot28():
    fig, ax = plt.subplots(2, 1)
    theta = np.linspace(0*tau/16, 8*tau/16, 9)
    y = np.sin(theta)
    x = np.cos(theta)
    ax[0].plot(theta, y, color='cyan', label='y')
    ax[0].plot(theta, x, color='magenta', label='x')
    ax[0].set_xlabel(r'$\theta$')
    xticks = np.linspace(0*tau/16, 8*tau/16, 9)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(0, 9, 1)]
    ax[0].xaxis.set_ticks(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[0].legend()
    ratio = np.tan(theta)
    ax[1].plot(theta, ratio, color='orange')
    ax[1].set_xlabel(r'$\theta$')
    ax[1].set_ylabel(r'$\frac{y}{x}$')
    xticks = np.linspace(0*tau/16, 8*tau/16, 9)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(0, 9, 1)]
    ax[1].xaxis.set_ticks(xticks)
    ax[1].set_xticklabels(xticklabels)
    ax[1].set_ylim(bottom=-5, top=5) 
    #fig.tight_layout()
    return fig
## Figure29
def standard_normal(x):
    return (math.exp(-(x**2)/2))/math.sqrt(tau)

def plot29():
    x = list(np.linspace(-4, 4, 100))
    y = list(map(standard_normal, x))
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, color='royalblue')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.plot((0, 0), (0, 0.4), color='tomato', ls=':')
    ax.plot((-4.1, 0), (0.4, 0.4), color='tomato', ls=':')
    ax.annotate(xy=(0.1, 0), text=r'$\mu$', xytext=(0.1, 0))
    ax.annotate(xy=(-4, 0.38), text=r'$\frac{1}{\sqrt{\tau}}$', xytext=(-4, 0.38))
    return fig
## Figure30
def plot30():
    x = list(np.linspace(-4, 4, 100))
    y = list(map(standard_normal, x))
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, color='royalblue')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.plot((0, 0), (0, 0.4), color='tomato', ls=':')
    ax.plot((-4.1, 0), (0.4, 0.4), color='tomato', ls=':')
    ax.plot((-1/2**0.5, -1/2**0.5), (0, 0.31), color='seagreen', ls=':')
    ax.plot((1/2**0.5, 1/2**0.5), (0, 0.31), color='seagreen', ls=':')
    ax.plot((-2/2**0.5, -2/2**0.5), (0, 0.15), color='seagreen', ls=':')
    ax.plot((2/2**0.5, 2/2**0.5), (0, 0.15), color='seagreen', ls=':')
    ax.plot((-3/2**0.5, -3/2**0.5), (0, 0.04), color='seagreen', ls=':')
    ax.plot((3/2**0.5, 3/2**0.5), (0, 0.04), color='seagreen', ls=':')
    ax.annotate(xy=(0.1, 0), text=r'$\mu$', xytext=(0.1, 0))
    ax.annotate(xy=(-4, 0.38), text=r'$\frac{1}{\sqrt{\tau}}$', xytext=(-4, 0.38))
    return fig
## Figure31
def plot31():
    x = list(np.linspace(-4, 4, 100))
    y = list(map(standard_normal, x))
    z = list(map(math.erf, x))
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(x, y, color='royalblue')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')
    ax[0].plot((0, 0), (0, 0.4), color='tomato', ls=':')
    ax[0].plot((-4.1, 0), (0.4, 0.4), color='tomato', ls=':')
    ax[0].plot((-1/2**0.5, -1/2**0.5), (0, 0.31), color='seagreen', ls=':')
    ax[0].plot((1/2**0.5, 1/2**0.5), (0, 0.31), color='seagreen', ls=':')
    ax[0].plot((-2/2**0.5, -2/2**0.5), (0, 0.15), color='seagreen', ls=':')
    ax[0].plot((2/2**0.5, 2/2**0.5), (0, 0.15), color='seagreen', ls=':')
    ax[0].plot((-3/2**0.5, -3/2**0.5), (0, 0.04), color='seagreen', ls=':')
    ax[0].plot((3/2**0.5, 3/2**0.5), (0, 0.04), color='seagreen', ls=':')
    ax[0].annotate(xy=(0.1, 0), text=r'$\mu$', xytext=(0.1, 0))
    ax[0].annotate(xy=(-4, 0.35), text=r'$\frac{1}{\sqrt{\tau}}$', xytext=(-4, 0.35))
    ax[1].plot(x, z, color='royalblue')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')
    ax[1].plot((-4, 4), (0, 0.), color='tomato', ls=':')
    ax[1].plot((-1/2**0.5, -1/2**0.5), (0, math.erf(-1/2**0.5)), color='seagreen', ls=':')
    ax[1].plot((1/2**0.5, 1/2**0.5), (0, math.erf(1/2**0.5)), color='seagreen', ls=':')
    ax[1].plot((-2/2**0.5, -2/2**0.5), (0, math.erf(-2/2**0.5)), color='seagreen', ls=':')
    ax[1].plot((2/2**0.5, 2/2**0.5), (0, math.erf(21/2**0.5)), color='seagreen', ls=':')
    ax[1].plot((-3/2**0.5, -3/2**0.5), (0, math.erf(-3/2**0.5)), color='seagreen', ls=':')
    ax[1].plot((3/2**0.5, 3/2**0.5), (0, math.erf(3/2**0.5)), color='seagreen', ls=':')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel(r'erf$(x)$')
    fig.tight_layout()
    return fig
## Figure32
def plot32():
    x = list(np.linspace(-4, 4, 100))
    y = list(map(standard_normal, x))
    z = list(map(math.erfc, x))
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(x, y, color='royalblue')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')
    ax[0].plot((0, 0), (0, 0.4), color='tomato', ls=':')
    ax[0].plot((-4.1, 0), (0.4, 0.4), color='tomato', ls=':')
    ax[0].plot((-1/2**0.5, -1/2**0.5), (0, 0.31), color='seagreen', ls=':')
    ax[0].plot((1/2**0.5, 1/2**0.5), (0, 0.31), color='seagreen', ls=':')
    ax[0].plot((-2/2**0.5, -2/2**0.5), (0, 0.15), color='seagreen', ls=':')
    ax[0].plot((2/2**0.5, 2/2**0.5), (0, 0.15), color='seagreen', ls=':')
    ax[0].plot((-3/2**0.5, -3/2**0.5), (0, 0.04), color='seagreen', ls=':')
    ax[0].plot((3/2**0.5, 3/2**0.5), (0, 0.04), color='seagreen', ls=':')
    ax[0].annotate(xy=(0.1, 0), text=r'$\mu$', xytext=(0.1, 0))
    ax[0].annotate(xy=(-4, 0.35), text=r'$\frac{1}{\sqrt{\tau}}$', xytext=(-4, 0.35))
    ax[1].plot(x, z, color='royalblue')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')
    ax[1].plot((-4, 4), (0, 0.), color='tomato', ls=':')
    ax[1].plot((-1/2**0.5, -1/2**0.5), (0, math.erfc(-1/2**0.5)), color='seagreen', ls=':')
    ax[1].plot((1/2**0.5, 1/2**0.5), (0, math.erfc(1/2**0.5)), color='seagreen', ls=':')
    ax[1].plot((-2/2**0.5, -2/2**0.5), (0, math.erfc(-2/2**0.5)), color='seagreen', ls=':')
    ax[1].plot((2/2**0.5, 2/2**0.5), (0, math.erfc(21/2**0.5)), color='seagreen', ls=':')
    ax[1].plot((-3/2**0.5, -3/2**0.5), (0, math.erfc(-3/2**0.5)), color='seagreen', ls=':')
    ax[1].plot((3/2**0.5, 3/2**0.5), (0, math.erfc(3/2**0.5)), color='seagreen', ls=':')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel(r'erfc$(x)$')
    fig.tight_layout()
    return fig
#%% Figure33
def plot33():
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    ax.plot((-200, 200), (-200, 200), color='darkgray', ls=':')
    ax.plot((-200, 200), (200, -200), color='darkgray', ls=':')
    theta1 = np.linspace(-16*tau/16, 16*tau/16, 17)
    x1 = np.cosh(theta1)
    y1 = np.sinh(theta1)
    ax.scatter(x1, y1, s=25, color='darkgray')
    theta4 = np.linspace(-tau, tau, 100)
    x4 = np.cosh(theta4)
    y4 = np.sinh(theta4)
    ax.plot(x4, y4, color='royalblue')
    ax.spines['bottom'].set_position('center')
    return fig
#%% Figure34
def plot34():
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    ax.plot((-4, 4), (-4, 4), color='darkgray', ls=':')
    ax.plot((-4, 4), (4, -4), color='darkgray', ls=':')
    ax.set_xlim((-1, 3))
    ax.set_ylim((-3, 3))
    theta1 = np.linspace(-4*tau/16, 4*tau/16, 9)
    x1 = np.cosh(theta1)
    y1 = np.sinh(theta1)
    ax.scatter(x1, y1, s=25, color='darkgray')
    x2 = math.cosh(4*tau/16)
    y2 = math.sinh(4*tau/16)
    ax.scatter(x2, y2, s=50, color='tomato')
    x3 = (0, math.cosh(4*tau/16))
    y3 = (0, math.sinh(4*tau/16))
    ax.plot(x3, y3, color='tomato')
    theta4 = np.linspace(-tau/4, tau/4, 100)
    x4 = np.cosh(theta4)
    y4 = np.sinh(theta4)
    ax.plot(x4, y4, color='royalblue')
    ax.spines['bottom'].set_position('center')
    x5 = (math.cosh(4*tau/16), math.cosh(4*tau/16))
    y5 = (0, math.sinh(4*tau/16))
    ax.plot(x5, y5, color='cyan', ls=':')
    x6 = (0, math.cosh(4*tau/16))
    y6 = (0, 0)
    ax.plot(x6, y6, color='magenta', ls=':')
    ax.annotate(text=r'$\theta$',xy=(0, 0), xytext=(0.3, 0.05))
    return fig
#%% Figure35
def plot35():
    fig, ax = plt.subplots(2, 1)
    theta = np.linspace(-16*tau/16, 16*tau/16, 100)
    x = np.cosh(theta)
    y = np.sinh(theta)
    ax[0].plot(theta, y, color='cyan')
    ax[1].plot(theta, x, color='magenta')
    xticks = np.linspace(-16*tau/16, 16*tau/16, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(-16, 24, 8)]
    ax[0].set_xlabel(r'$\theta$')
    ax[1].set_xlabel(r'$\theta$')
    ax[0].set_ylabel(r'$y$')
    ax[1].set_ylabel(r'$x$')
    ax[0].xaxis.set_ticks(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[1].xaxis.set_ticks(xticks)
    ax[1].set_xticklabels(xticklabels)
    return fig
#%% Figure36
def plot36():
    fig, ax = plt.subplots(2, 1)
    theta = np.linspace(-4*tau/16, 4*tau/16, 100)
    x = np.cosh(theta)
    y = np.sinh(theta)
    ax[0].plot(theta, y, color='cyan')
    ax[1].plot(theta, x, color='magenta')
    xticks = np.linspace(-4*tau/16, 4*tau/16, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(-4, 6, 2)]
    ax[0].set_xlabel(r'$\theta$')
    ax[1].set_xlabel(r'$\theta$')
    ax[0].set_ylabel(r'$y$')
    ax[1].set_ylabel(r'$x$')
    ax[0].xaxis.set_ticks(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[1].xaxis.set_ticks(xticks)
    ax[1].set_xticklabels(xticklabels) 
    return fig
#%% Figure37
def plot37():
    fig, ax = plt.subplots()
    theta = np.linspace(-4*tau/16, 4*tau/16, 100)
    x = np.cosh(theta)
    y = np.sinh(theta)
    ax.plot(theta, y**2, color='cyan', label=r'$y^{2}$')
    ax.plot(theta, x**2, color='magenta', label=r'$x^{2}$')
    xticks = np.linspace(-4*tau/16, 4*tau/16, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(-4, 6, 2)]
    ax.set_xlabel(r'$\theta$')
    ax.xaxis.set_ticks(xticks)
    ax.set_xticklabels(xticklabels)  
    return fig
#%% Figure38
def plot38():
    fig, ax = plt.subplots(2, 1)
    theta = np.linspace(0, 4*tau/16, 100)
    x1 = 0.5 * np.exp(theta)
    x2 = 0.5 * np.exp(-theta)
    ax[0].plot(theta, x1, color='sandybrown', label=r'$\frac{1}{2}$'+'exp'+r'$(\theta)$')
    ax[1].plot(theta, x2, color='palegreen', label=r'$\frac{1}{2}$'+'exp'+r'$(-\theta)$')
    xticks = np.linspace(0, 4*tau/16, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(0, 5, 1)]
    ax[0].set_xlabel(r'$\theta$')
    ax[1].set_xlabel(r'$\theta$')
    ax[0].xaxis.set_ticks(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[1].xaxis.set_ticks(xticks)
    ax[1].set_xticklabels(xticklabels) 
    ax[0].legend()
    ax[1].legend()
    return fig
#%% Figure39
def plot39():
    fig, ax = plt.subplots(2, 1)
    theta = np.linspace(0, 4*tau/16, 100)
    x = np.cosh(theta)
    y = np.sinh(theta)
    ax[0].plot(theta, y, color='cyan', label=r'$y$'+' (sandybrown-palegreen)')
    ax[1].plot(theta, x, color='magenta', label=r'$x$'+' (sandybrown+palegreen)')
    xticks = np.linspace(0, 4*tau/16, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(0, 5, 1)]
    ax[0].set_xlabel(r'$\theta$')
    ax[1].set_xlabel(r'$\theta$')
    ax[0].set_ylabel(r'$y$')
    ax[1].set_ylabel(r'$x$')
    ax[0].xaxis.set_ticks(xticks)
    ax[0].set_xticklabels(xticklabels) 
    ax[1].xaxis.set_ticks(xticks)
    ax[1].set_xticklabels(xticklabels) 
    ax[0].legend()
    ax[1].legend()
    return fig
#%% Figure40
def plot40():
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    ax.scatter(3, 2, s=50, color='tomato')
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlim(left=-5, right=5)
    ax.set_ylim(bottom=-5, top=5)
    xticks = np.linspace(-5, 5, 11)
    yticks = np.linspace(-5, 5, 11)
    ax.xaxis.set_ticks(xticks)
    ax.yaxis.set_ticks(yticks)
    x1 = (0, 3)
    y1 = (0, 0)
    ax.plot(x1, y1, color='magenta', ls=':')
    x2 = (3, 3)
    y2 = (0, 2)
    ax.plot(x2, y2, color='cyan', ls=':')
    ax.set_xlabel('real')
    ax.set_ylabel('imag')
    return fig
#%% Figure41
def plot41():
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    ax.scatter(3, 2, s=50, color='lightgray')
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlim(left=-5, right=5)
    ax.set_ylim(bottom=-5, top=5)
    xticks = np.linspace(-5, 5, 11)
    yticks = np.linspace(-5, 5, 11)
    ax.xaxis.set_ticks(xticks)
    ax.yaxis.set_ticks(yticks)
    x1 = (0, 3)
    y1 = (0, 0)
    ax.plot(x1, y1, color='magenta', ls=':')
    x2 = (3, 3)
    y2 = (0, 2)
    ax.plot(x2, y2, color='cyan', ls=':')
    ax.set_xlabel('real')
    ax.set_ylabel('imag')
    x3 = (3, 1)
    y3 = (2, 2)
    ax.plot(x3, y3, color='magenta', ls=':')
    x4 = (1, 1)
    y4 = (2, 3)
    ax.plot(x4, y4, color='cyan', ls=':')
    ax.scatter(1, 3, s=50, color='tomato')
    return fig
#%% Figure42
def plot42():
    angle = 2*tau/16
    theta = np.linspace(0, tau, 100)
    r = np.ones(100)
    theta2 = (0, angle)
    r2 = (0, 1)
    theta3 = (angle,)
    r3 = (1,)
    theta4 = (0, 0)
    r4 = (0, math.cos(angle))
    theta5 = (0, angle)
    r5 = (math.cos(angle), 1)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='royalblue')
    ax.plot(theta2, r2, color='tomato') 
    ax.scatter(theta3, r3, s=50, color='tomato')
    ax.plot(theta4, r4, color='magenta', lw=2, ls=':')
    ax.plot(theta5, r5, color='cyan', lw=2, ls=':')
    xticks = np.linspace(0, 90, 5)
    xticklabels = [r'$\frac{' + f'{num}' + '}{16}$' + r'$\tau$' for num in range(5)]
    ax.set_thetagrids(xticks)
    ax.set_xticklabels(xticklabels) 
    ax.set_rticks([0, 0.5, 1])
    ax.set_rlabel_position(45)
    ax.set_thetamin(0)
    ax.set_thetamax(90)
    theta6 = 0
    r6 = 0
    ax.annotate('real component',
                xy=(0.1, math.cos(angle)/2-0.02),  # theta, radius
                xytext=(0.1, math.cos(angle)/2-0.02),
                color='magenta')
    ax.annotate('imaginary component',
                xy=(angle-0.5, math.cos(angle)-0.02),  # theta, radius
                xytext=(angle-0.5, math.cos(angle)-0.02),
                color='cyan', rotation=90)
    ax.annotate('radius',
            xy=(angle-0.1, math.cos(angle)/2-0.01),  # theta, radius
            xytext=(angle-0.1, math.cos(angle)/2-0.01),
            color='red', rotation=45)
    ax.annotate(r'$\varphi$',
                xy=(0.3, 0.1),  # theta, radius
                xytext=(0.3, 0.1),
                color='black')
#%% Figure43
def plot43():
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    ax.scatter(3, 2, s=50, color='tomato')
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlim(left=-5, right=5)
    ax.set_ylim(bottom=-5, top=5)
    xticks = np.linspace(-5, 5, 11)
    yticks = np.linspace(-5, 5, 11)
    ax.xaxis.set_ticks(xticks)
    ax.yaxis.set_ticks(yticks)
    x1 = (0, 3)
    y1 = (0, 0)
    ax.plot(x1, y1, color='magenta', ls=':')
    x2 = (3, 3)
    y2 = (0, 2)
    ax.plot(x2, y2, color='cyan', ls=':')
    ax.set_xlabel('real')
    ax.set_ylabel('imag')
    x3 = (0, 3)
    y3 = (0, 2)
    ax.plot(x3, y3, color='tomato', ls=':')
    theta = np.linspace(0, tau, 100)
    r4 = cmath.polar(3+2j)[0] * np.ones(100)
    x4 = r4 * np.cos(theta)
    y4 = r4 * np.sin(theta)
    ax.plot(x4, y4, color='royalblue')
    theta = np.linspace(0, tau, 17)
    x5 = cmath.polar(3+2j)[0] * np.cos(theta)
    y5 = cmath.polar(3+2j)[0] * np.sin(theta)
    ax.scatter(x5, y5, color='gray', s=50)
    ax.annotate(text=r'$\varphi$', xy=(0.5, 0.2), xytext=(0.5, 0.2))
    ax.annotate(text=r'$r$', xy=(1.5, 1.2), xytext=(1.5, 1.2), color='tomato')
    return fig