# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 12:12:00 2016

@author: jason
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.cluster.bicluster import SpectralCoclustering
import numpy as np
    
data = pd.read_csv('inputWeather.csv')
cityList = dict(zip([i for i in range(len(data.CityMonth))],data.CityMonth))    
corr_data = data.iloc[:,1:7]

corr_weather = pd.DataFrame.corr(corr_data.transpose())

## Group according to 3 groups (winter, summer, and transition seasons (fall and spring))
#model = SpectralCoclustering(n_clusters=3, random_state=0)
#model.fit(corr_weather)
#corr_data["Group"] = pd.Series(model.row_labels_, index=corr_data.index)
#corr_data = corr_data.ix[np.argsort(model.row_labels_)]
#cityOrder = corr_data.ix[np.argsort(model.row_labels_)].index.tolist()
#corr_data=corr_data.reset_index(drop=True)

#corr_weather = pd.DataFrame.corr(corr_data.transpose())

fig, ax = plt.subplots(figsize=(40,40))
corrMap = ax.pcolor(corr_weather)

ax_labels = [cityList[key] for key in cityList.keys()]
ax_labels = ax_labels[:-1]
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.set_xticklabels(ax_labels, rotation=45, minor=False)
ax.set_yticklabels(ax_labels, minor=False)
ax.axis("tight")
cbar = plt.colorbar(corrMap)
plt.savefig("corr_weather.pdf")