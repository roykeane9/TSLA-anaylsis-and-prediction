#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


file = 'D:/file/TSLA_3years.csv'
df = pd.read_csv(file, index_col = 'Date', parse_dates = True)

df


# In[2]:


predict_val = 'Close' 
predict_day = int(input("Input predict days:"))
proportion = int(predict_day)/len(df)
print("Predict days proportion: %f" %proportion)

df['Pre_val'] = df[predict_val].shift(1)
df.fillna(df[predict_val].iloc[0], inplace = True)

df


# In[3]:


import pandas as pd


df = df[['Open', 'High', 'Low', 'Close', 'Volume', 'Pre_val']]
df['Amplitude'] = abs(df['High'] - df['Low']) / df['Pre_val'] * 100.0
df['CO_PCT'] = (df['Close'] - df['Open']) / df['Open'] * 100.0
df = df[['Close', 'Amplitude', 'CO_PCT', 'Volume']]
df.fillna(-999, inplace = True)
df['Label'] = df[predict_val].shift(-predict_day)
Df = df[:]

df


# In[4]:


import numpy as np
from sklearn import preprocessing

x = np.array(df.drop(['Label'],axis=1))
x = preprocessing.scale(x)

last_x = x[-predict_day:]
x = x[:-predict_day]
y= np.array(df[:-predict_day]['Label'])

df.dropna(inplace = True)

print("x:\n", x, "\nlast_x:\n", last_x, "\ny:\n", y)


# In[5]:


from sklearn import model_selection,svm
from sklearn.linear_model import LinearRegression


train_x, test_x, train_y, test_y = model_selection.train_test_split(x, y, test_size = 0.3)
model = LinearRegression(n_jobs=-1)
model.fit(train_x, train_y)
accuracy = model.score(test_x, test_y)
print("Accuracy: ",accuracy)
predict_set = model.predict(last_x)

predict_set


# In[6]:


import datetime


df['Predict'] = np.nan
last_date = Df.iloc[-1].name
last_unix = last_date.timestamp()
next_unix = last_unix + 86400 

for i in predict_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]
    
df


# In[7]:


first_predict_val = Df.iloc[-1][predict_val]
df.loc[last_date] = np.nan
df = df.sort_index()
df.loc[last_date]['Predict'] = first_predict_val

df


# In[8]:


import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
Df[predict_val].plot()
df['Predict'].plot()
plt.legend(loc = 4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(linestyle='--')
plt.savefig('D:/file/TSLA_Price.png')
plt.show()


# In[9]:


import matplotlib.pyplot as plt
import numpy as np

pre = df['Predict']
pre.dropna(inplace = True)

x, y = np.array(pre.index), pre.values

plt.figure(figsize=(20, 10))
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Predict value')
plt.plot(x, y, marker='o', color='darkorange', linewidth='2')
plt.grid(linestyle='--')

for i in range(len(x)):
    plt.text(x[i], y[i]+0.5, y[i].round(2),  fontsize=16, verticalalignment='center', horizontalalignment='right')
    
plt.savefig('D:/file/TSLA_Predict.png')
plt.show()


# In[10]:


import matplotlib.pyplot as plt

DF = Df[-30:]
x, y = np.array(pre.index), pre.values

plt.figure(figsize=(20, 10))
DF[predict_val].plot()
df['Predict'].plot()
plt.legend(loc = 4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(linestyle='--')
for a, b in zip(DF.index, DF['Close']):
    plt.text(a, b-1, round(b, 2), fontsize=15, verticalalignment='center', horizontalalignment='right')
for i in range(1,len(x)):
    plt.text(x[i], y[i]+0.5, y[i].round(2),  fontsize=16, verticalalignment='center', horizontalalignment='right')
    

plt.savefig('D:/file/30d_TSLA_Price.png')
plt.show()

