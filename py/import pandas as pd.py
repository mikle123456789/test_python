import pandas as pd 
import os
import matplotlib
import numpy as np 

class drawing_plots():
    def draw_plot(path):
        dataframe = pd.read_json(path)
        for i in dataframe:
            print(i)

path = os.path.join('data', 'deviation.json')
drawing_plots.draw_plot(path)