import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)
import pandas as pd
a=pd.Series({'a':0.,'b':1.})
print(a)
#b=pd.Series()
#print(b)
print(a.dtypes)
print(a['b'])
b=pd.DataFrame([[1,2,3],[4,5,6]],columns=['name','id','age'],index=[1,2])
print(b)
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
'''c=pd.DataFrame(data)
print(c)
d=pd.DataFrame({1:'name',2:'id'},index=[1])
print(d)'''
b['emp']=[7,8]
print(b)
df = pd.DataFrame({'a':1.,'b':['TEST','Sample','case'],'c':'sdf'})
print(df)
print("++++++++++++++++")
print(df.dtypes)
print("++++++++++++++++")
print(df.head())
print("++++++++++++++++")
print(df.tail())
print("++++++++++++++++")
print(df.columns)
print("++++++++++++++++")
print(df.index)
print("++++++++++++++++")
print(df.describe())
print(df.iloc[1:])
del df['a']
df.pop('c')
print(df)
df1=pd.DataFrame([1,2,3],columns=['numbers'])
df2=pd.merge(df,df1,how='inner',left_index=True,right_index=True)
print(df2)
