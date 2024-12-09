import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print('Jason Glotzbach Melt, Pivot, Aggregations, Interation Assignment')
print("\n")

arrhyth_data = pd.read_csv('arrhythmia.data',sep=',',header=None)
arrhyth_data.insert(0, "Subject ID", ["ID_" + str(i) for i in range(1, len(arrhyth_data) + 1)])
arrhyth_data.rename(columns={0: 'Age', 1: 'Sex', 2: 'Height', 3: 'Weight', 4: 'QRS Duration', 5: 'PR Interval', 6: 'QT Interval', 7: 'T Interval', 8: 'P Interval'}, inplace=True)
cols = list(arrhyth_data.columns.values)
arrhyth_data.drop(cols[9:281], axis=1, inplace=True)
print(arrhyth_data.head(3))
print("\n")

#Melt 
print('using Melt:')
arrhyth_data_melted = pd.melt(arrhyth_data, id_vars='Sex', value_vars='Weight')
print(arrhyth_data_melted)
print("\n")

#Pivot 
print('using Pivot:')
arrhyth_data_pivot = arrhyth_data.pivot(index="Subject ID", columns='Sex', values='QT Interval')
print(arrhyth_data_pivot)
print("\n")

#Aggregation 
print('using Aggregation:')
ag_arrhyth_data = arrhyth_data.aggregate({'Height':['min','max','mean'], 'Weight':['min','max','mean'], 'QRS Duration':['min','max','mean']})
print(ag_arrhyth_data)
print("\n")

#Iteration
print('using Iteration:')
for index, row in arrhyth_data.iterrows():
    print(index, row['Age'], row['Sex'])
print("\n")

#Groupby
print('using GroupBy:')
grouped_data = arrhyth_data.groupby('Sex')['Weight'].mean()
print(grouped_data)