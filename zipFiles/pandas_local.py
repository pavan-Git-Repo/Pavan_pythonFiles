import pandas as pd
import matplotlib.pyplot as plt
frame = {'Day':[1,2,3,4,5,6],"visitors":[1000,200,3000,4000,5000,2000], ' Bounce_rate':[20,20,23,15,10,34]}
df = pd.DataFrame(frame)
df.set_index('Day',inplace = True)
df.plot()
plt.show()
print(df)