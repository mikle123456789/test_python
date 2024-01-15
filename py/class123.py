import pandas as pd 
import os
import matplotlib.pyplot as plt
import numpy as np 

class drawing_plots():
    def draw_plot(path, path_to_plots = None):
        if path_to_plots is None:
            path_to_plots = os.path.join('/'.join(path.split('/')[:-2]), 'plots')
        dataframe = pd.read_json(path)
        path1 = path_to_plots
        if not os.path.exists(path1):
            os.mkdir(path1)
        for i in dataframe:
            for j in dataframe:
                #print(i, j)
                if i != 'name' and j != 'name':
                    plt.plot(dataframe[i], dataframe[j]) 
                    plt.xlabel(i)
                    plt.ylabel(j)    
                    plt.savefig(os.path.join(path1, f'{i}_{j}.jpg'))
                    plt.clf()
        return path1
