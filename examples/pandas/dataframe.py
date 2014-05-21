import numpy as np
import pandas as pd
from bokeh import mpl

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
df.plot(legend=False)

mpl.to_bokeh(pd_obj=df, name="dataframe")
