# -*- coding: utf-8 -*-
"""DAP1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OvnnpCPJtWcZZtC25xPoi2VSSRpeoaDC
"""

!pip install numpy
import numpy as np



import numpy as np

#element wise operations
a1=np.array([1,2,3,4,5])
a2=np.array([2,3,4,5,6])
result=a1+a2
print(result)

#broadcasting
a1=np.array([1,2,3,4,5])
result1=a1+3
print(result1)



#linear algebra with numpy

a1=np.array([[2,3],[3,2]])
a2=np.array([[5,4],[4,5]])
print(a1)
print(a2)
res=np.dot(a1,a2) #dot product
print(res)
d=np.linalg.eig(res )
print(d)

a1=np.array([[2,3,5],[2,3,6]])
print(a1)
b=np.sum(a1)
print(b)
a2=np.array([[5,6,7],[7,8,9]])
b2=np.sum(a1+a2)
print(b2)
a2=np.array([[5,6,7],[7,8,9]])
c=np.sum(a2, axis=0)#row wise addition

d=np.sum(a2, axis=1)#column wise addition
print(c)
print(d)

#statistical operations

a=np.array([1,2,3,4,5])
print(a)
c=np.mean(a)#mean operation
print(c)
d=np.median(a)#median operation
print(d)
e=np.var(a)#variant operation
print(e)
f=np.std(a)#standard deviation operation
print(f)

#creating the dataset loading the dataset and saving the dataset
import numpy as np
data=np.loadtxt("/content/num.txt", dtype=int)#loading text into program
print(data)
data=np.savetxt("/content/nu.txt", data)#saving the txt file
print(data)

import matplotlib.pyplot as plt
a=np.array([1,2,3,4,5,6,7,8,9,10])
b=np.array([2,3,4,1,5,6,7,9,2,3,9,10])
plt.plot(a)
plt.plot(b)

import pandas as pd

a=['Jwalitha','Ramya','Durga','Jahnavi','Lahari','Raju','Ravi','Ramu']
r=pd.Series(a,index=[99,33,35,12,67,89,32,44])
print(r)

df=pd.read_csv("/content/archive (2).zip")
print(df)

df=pd.read_csv("/content/mmm.txt",)
print(df)

df=pd.read_excel("/content/HR_Employee_Data.xlsx")
print(df)

df=pd.read_excel("/content/HR_Employee_Data.xlsx",sheet_name=0)
print(df)

print(df.loc[1])

df=pd.read_excel("/content/test.xlsx")
print(df)

mv=df['Age/Sex'].mean()
df=df.fillna(mv)
print(df)

df=pd.read_excel("/content/test.xlsx")
print(df)

mv=df['Age/Sex'].mean()
df=df.fillna(mv)
print(df)
df.shape

rr=pd.read_excel("/content/duplicate.xlsx")
print(rr)
rr.shape

testing=rr.tail(10)
for i in range(38,28,-1):
  rr.drop([i],axis=0, inplace=True)

testingfake=rr.tail(10)
for i in range(38,28,-1):
   rr.drop([i],axis=0, inplace=True)

rr.head(5)

rr=rr.drop_duplicates()
print(rr)

rr=pd.read_excel("/content/duplicate.xlsx")
print(rr)
rr=rr.drop_duplicates()
print(rr)

rr.head(4)

from google.colab import drive
drive.mount('/content/drive')

rr.shape

df.shape
last=df.tail(10)
print(last)
for i in range(27,38,-1):
   last.drop([i],axis=0, inplace=True)
dataa=pd.concat([last],axis=0)
dataa.to_csv("done.csv")

print(df.groupby(['Age/Sex'])['Death/Migration'].count())

print(df.groupby(['Name of the Volunteer'])['Head of the family '].count())

import numpy as np
import matplotlib.pyplot as plt
runs=np.array([100,50,91,78,89,25,34,19,9,10])
w=np.array([1,0,2,0,3,7,8,8,7,5])
plt.plot(runs,w,color='orange')
plt.title('Ind VS AUS_score')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
tiger=np.linspace(-2*np.pi,2*np.pi,100)
print(tiger)
plt.plot(tiger,np.sin(tiger),color='RED')
plt.title("sin(x)")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
tiger=np.linspace(-1*np.pi,2*np.pi,100)
print(tiger)
plt.plot(tiger,np.sin(tiger),color='black')
plt.title("sin(x)")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
tiger=np.linspace(-np.pi,np.pi,100)
print(tiger)
plt.plot(tiger,np.sin(tiger),color='yellow')
plt.title("sin(x)")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
tiger=np.linspace(-2*np.pi,2*np.pi,50)
print(tiger)
plt.scatter (tiger,np.sin(tiger),color='RED')
plt.title("sin(x)")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
overs=np.arange(5,50,5)
overs_a=np.arange(5,30,5)
runs_i=np.array([25,51,84,131,160,189,220,250,267])
runs_a=np.array([15,41,94,110,151])
wickets=np.array([12,32,96])
plt.subplot(2,1,1)
plt.plot(overs,runs_i,color='blue',label='India')

plt.subplot(2,1,2)

plt.plot(overs_a,runs_a,color='red',label='Aus')

plt.legend(loc='best')

plt.show()

import matplotlib.pyplot as plt
a=[230,560,780,127,128]
b=[200,160,270,127,400]
years=[1,2,3,4]
profit_a=[(a[i]-a[i-1]) for i in range(1,len(a))]
profit_b=[(b[i]-b[i-1]) for i in range(1,len(b))]
plt.subplot(2,1,2)
plt.plot(years,profit_a,color='hotpink',linewidth='5',label='CompanyA',marker='+',ms='40',mec='m')
plt.subplot(2,1,1)
plt.plot(years,profit_b,color='orange',linewidth='5',label='CompanyB',marker='*',linestyle='dotted')

a=np.array([25,60,5,10])
labe=['AIML','Python','Pandas','Numpy']
explo=[0.2,0,0,0]
plt.pie(a,labels=labe,explode=explo,startangle=180,set)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

a = np.array([25, 60, 5, 10])
labels = ['AIML', 'Python', 'Pandas', 'Numpy']
explode = [0.2, 0, 0, 0]
colors = ['black', 'red', 'green', 'orange']

plt.pie(a, labels=labels, explode=explode, startangle=180,colors=colors)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

a = np.array([25, 60, 5, 10])
labels = ['AIML', 'Python', 'Pandas', 'Numpy']
explode = [0.2, 0, 0, 0]
colors = ['black', 'red', 'green', 'orange']
plt.title('Python',fontsize=30)

plt.pie(a, labels=labels, explode=explode, startangle=180,colors=colors,)
plt.text(-1.5,0,'Pandas',fontsize=14,color='orange')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("/content/temperature analysis.xlsx")
print(df)
avgtemp=df['TEMPERATURE'].mean()
df=df.fillna(avgtemp)
a1=np.array(df['TEMPERATURE'])
maxtemp=df['TEMPERATURE'].max()
mintemp=df['TEMPERATURE'].min()
days=[a1[i] for i in range(1, len(a1)) if a1[i]>avgtemp]
date=np.array(df['DAY'])
plt.plot(date,a1,color='blue',linewidth='2',label='Temperature',marker='*',ms='10',mec='b')
plt.legend(loc='best')
print('Mean =',avgtemp)
print('Maximum =',maxtemp)
print('Minimum =',mintemp)
print('Threshold',avgtemp,'is',len(days),'DAY')
plt.show()

pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
sns.scatterplot(x="total_bill",y="tip",data=tips)
plt.title("Scatter Plot of total Bills Vs Tip")
plt.xlabel("Total Bill($)")
plt.ylabel("Tip($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
sns.scatterplot(x="total_bill",y="tip",data=tips)
plt.title("Scatter Plot of total Bills Vs Tip")
plt.xlabel("Total Bill($)")
plt.ylabel("Tip($)")
plt.show()
tips.head(20)

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
sns.violinplot(x="day",y="total_bill",data=tips)
plt.title("Distribution of  Total Bill by day")
plt.xlabel("Day of the week")
plt.ylabel("Total Bills")
plt.show()
tips.head(20)

import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset("iris")
correlation_matrix=iris.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title('Correlation Heatmap of Iris Dataset')
plt.show()
print(iris)

import seaborn as sns
import matplotlib.pyplot as plt
flights = sns.load_dataset("flights")
correlation_matrix = flights.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title('Flights data set')
plt.show()

print(flights)

