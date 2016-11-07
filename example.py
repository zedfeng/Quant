import pandas as pd
import scipy as sp
data=sp.randn(5,2)
dates=pd.date_range('28/12/2015',periods=5)
df=pd.DataFrame(data,columns=('price','weight'),index=dates)
print(df.mean())