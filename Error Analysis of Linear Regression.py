#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


true = [173.22, 181.41, 188.27, 189.98, 194.76]
pre_5d_data = [[147.23, 147.54, 162.01, 179.53, 166.73],
           [146.82, 147.12, 162.01, 178.6, 166.67],
           [147.26, 148, 163.78, 180.05, 167.21],
           [146.72, 146.82, 161.52, 177.49, 167.85],
           [147.04, 147.2, 161.87, 177.81, 167.46],
           [147.26, 147.2, 161.2, 178.3, 167.88],
           [146.92, 147.12, 162.55, 176.92, 168.08],
           [146.97, 147.07, 161.09, 178.95, 167.11],
           [147.27, 147.5, 162.31, 178.28, 167.14],
           [147.52, 147.97, 162.29, 180.28, 165.48]]

df_5 = pd.DataFrame(pre_5d_data)
err_5 = pd.DataFrame(pre_5d_data, columns=['1 Day', '2 Day', '3 Day', '4 Day', '5 Day'])

for x in range(10):
    for y in range(len(true)):
        err_5.iloc[x, y] = (abs(df_5.iloc[x, y] - true[y]) /  df_5.iloc[x, y])*100

plt.figure(figsize=(10, 5))        
plt.title("Predicted closing price and actual error percentage (%)")
boxplot = err_5.boxplot(column=['1 Day', '2 Day', '3 Day', '4 Day', '5 Day'])


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


true = [173.22, 181.41, 188.27, 189.98]
pre_4d_data = [[146.16, 160.5, 178.51, 166.72],
              [147.13, 161.89, 179.16, 165.6],
              [146.56, 161.83, 177.64, 166.36],
              [146.59, 160.47, 181.21, 166.06],
              [147.16, 161.51, 180.71, 166.13],
              [147.01, 161.85, 178.25, 165.74],
              [147.06, 161.31, 180.38, 166.21],
              [146.21, 160.23, 178.88, 167.36],
              [146.34, 160.6, 179.56, 166.02],
              [147.05, 161.79, 178.62, 166.06]]

df_4 = pd.DataFrame(pre_4d_data)
err_4 = pd.DataFrame(pre_4d_data, columns=['1 Day', '2 Day', '3 Day', '4 Day'])

for x in range(10):
    for y in range(len(true)):
        err_4.iloc[x, y] = (abs(df_4.iloc[x, y] - true[y]) /  df_4.iloc[x, y])*100

plt.figure(figsize=(10, 5))        
plt.title("Predicted closing price and actual error percentage (%)")
boxplot = err_4.boxplot(column=['1 Day', '2 Day', '3 Day', '4 Day'])


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt


true = [173.22, 181.41, 188.27]
pre_3d_data = [[161.25, 177.66, 166.65],
              [160, 181.13, 167.15],
              [161.12, 178.34, 166.58],
              [159.22, 178.69, 167.12],
              [160.44, 178.63, 167.29],
              [160.63, 179.33, 167.1],
              [162.55, 178.55, 167.27],
              [159.99, 178.65, 168.1],
              [161.04, 178.86, 167.6],
              [160.47, 179.67, 165.46]]

df_3 = pd.DataFrame(pre_3d_data)
err_3 = pd.DataFrame(pre_3d_data, columns=['1 Day', '2 Day', '3 Day'])

for x in range(10):
    for y in range(len(true)):
        err_3.iloc[x, y] = (abs(df_3.iloc[x, y] - true[y]) /  df_3.iloc[x, y])*100

plt.figure(figsize=(10, 5)) 
plt.title("Predicted closing price and actual error percentage (%)")
boxplot = err_3.boxplot(column=['1 Day', '2 Day', '3 Day'])


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt


true = [173.22, 181.41]
pre_2d_data = [[178.9, 166.7],
              [177.91, 166.71],
              [179.6, 166.98],
              [177.3, 166.76],
              [178.92, 166.8],
              [178.43, 166.55],
              [178.6, 166.55],
              [178.16, 166.91],
              [179.16, 166.84],
              [177.53, 167.11]]

df_2 = pd.DataFrame(pre_2d_data)
err_2 = pd.DataFrame(pre_2d_data, columns=['1 Day', '2 Day'])

for x in range(10):
    for y in range(len(true)):
        err_2.iloc[x, y] = (abs(df_2.iloc[x, y] - true[y]) /  df_2.iloc[x, y])*100

plt.figure(figsize=(10, 5)) 
plt.title("Predicted closing price and actual error percentage (%)")
boxplot = err_2.boxplot(column=['1 Day', '2 Day'])


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt


true = [173.22]
pre_1d_data = [[167.51], [166.96], [167.08], [167.12], [167.02],
               [166.99], [167.03], [166.76], [167.12], [166.87]]

df_1 = pd.DataFrame(pre_1d_data)
err_1 = pd.DataFrame(pre_1d_data, columns=['1 Day'])

for x in range(10):
    for y in range(len(true)):
        err_1.iloc[x, y] = (abs(df_1.iloc[x, y] - true[y]) /  df_1.iloc[x, y])*100

plt.figure(figsize=(10, 5)) 
plt.title("Predicted closing price and actual error percentage (%)")
boxplot = err_1.boxplot(column=['1 Day'])


# In[ ]:




