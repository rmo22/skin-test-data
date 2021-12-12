# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

df=pd.read_csv(r'pccHeat map W0.csv')


df = df.rename(columns={'Deformation, mm': 'Deformation'})

y=plt.figure(1)
ax3=y.add_subplot(1,1,1)
# type(y)
corrMatrix = df.corr()

corrMatrix.round(decimals=2)

plt.xticks(rotation=45)



#this changes the font 

sn.set(font_scale=1)
sn.set_style("whitegrid")
#changing the colour
# heat_map = sb.heatmap(data, cmap="YlGnBu")

# mask = np.triu(np.ones_like(corrMatrix,dtype=bool))
mask = np.triu(np.ones_like(corrMatrix,dtype=bool))
annot_kws={'fontsize':10}
cmap=sn.diverging_palette(220,10,as_cmap=True) #giving a gradient on the heatmap
ax3=sn.heatmap(corrMatrix,cmap=cmap, annot=True, mask=mask,vmin=-1, vmax=1, annot_kws=annot_kws, cbar_kws={'shrink':0.6})
palette = sn.diverging_palette(20, 220, n=256)

font = {'Times New Roman' : 'normal',
        'weight' : 'normal',
        'size'   : 14}	
plt.show()




# palette = sn.diverging_palette(200, 100, n=256) # seeing if changing numbers changes colour combination


