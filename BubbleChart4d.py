# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
from sklearn.linear_model import LinearRegression
df=pd.read_csv('SkinClassBubble.csv')

#both sets of code on this page work but the second lot actually displays the colour bar title and the right font sizes
# fig, ax = plt.subplots()
# my_scatter_plot = ax.scatter(
# df["Moisture"], #x value
# df["Roughness"], #y value
# df["Friction"], #z value, i.i. size of the marker
# df["Deformation"] #what I want to be the 4th dimension illustrated by colour gradient
# )

# plt.scatter(df["Moisture"], 
#             df["Roughness"], 
#             s=df["Friction"]*1000, alpha=0.5, 
#             c=df["Deformation"], 
          
#             )


# # plt.colorbar(),

# #Chris's blah blah blah
f=18
cmap=plt.get_cmap('viridis_r')
# c.set_label(r'$\zeta\ [s^{-1}]$', fontsize=f) 

ax=df.plot(kind="scatter", x= "Moisture", y="Roughness", alpha=0.5,s=df['Friction']*1000,figsize=(10,7),c="Deformation, mm",cmap=cmap, vmin=0.28, vmax=0.34)


#         y = "Roughness", alpha=0.5, 
#         s=df["Friction"]*1000, figsize=(10,7), 
#         c="Deformation", cmap=cmap, colorbar=True,
#         )









#setting the axes limits using axes.set which in this case is ax.set
ax.set_xlim([20,60])
ax.set_ylim([2.2,4])
# plt.clim([0.2, 0.4])
#need to change colour bar cmap limits to 0.2-0.4 for the deformation


# # plt.show()

# plt.rcParams["font.family"] = "Times New Roman"
plt.xlabel("Moisture (c.u.)")
# # plt.xticks(fontsize=f)
# # plt.yticks(fontsize=f)
plt.ylabel(u"Roughness Ra (\u03bcm)")


#legend
for area in [0.1, 0.5, 0.8, 1.2]:
        
                label=str(df['Friction'])
        
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='CoF corresponds to bubble area')
# #now going to try to label each data point with the participant number


 
# df=pd.DataFrame(columns=['Moisture','Roughness','Participant'])
# df=df.set_index('Participant')
# # ax=df.set_index('x')['y'].plot(style='o')
# ax=plt.scatter("Moisture","Roughness")

#this part of code is for labelling the point e.g. participant number or treatment
def label_point(Moisture,Roughness,Participant, ax):
    d=pd.concat({'Moisture':Moisture,'Roughness':Roughness,'Participant':Participant},axis=1)
    for i, point in d.iterrows():
        ax.text(point['Moisture'],point['Roughness'],str(point['Participant']), fontsize=10)
label_point(df.Moisture,df.Roughness,df.Participant,ax)


# print()       
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 14}	
plt.rc('font', **Roman) #a double hashtag is referred to as a kwargs and allows input of variables into a single function