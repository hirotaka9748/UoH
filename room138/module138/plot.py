import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot(file1,file2):

    data01_axis1 = np.loadtxt(file1, comments='!', unpack=True)
    data01_value1 = np.loadtxt(file2, comments='!', unpack=True)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.plot(data01_axis1, data01_value1, "o-", color="k")
    ax.set_xlim()
    ax.set_ylim()
    ax.set_xlabel("θ")
    ax.set_ylabel("difference")
    plt.show()
    
def pandasPlot(calc_path):
    data = pd.read_csv(calc_path,encoding = 'UTF8', header=None)
    fig=plt.plot(data[0],data[1])
    plt.grid()
    
def pandasPlots(calc_path):
    data = pd.read_csv(calc_path,encoding = 'UTF8', header=None)
    fig=plt.plot(data[0],data[1])
    fig=plt.plot(data[0],data[2])
    plt.grid()