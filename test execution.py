import pandas as pd
data={'names':['harish','chethan','bharath','nagesh'],
      'branch name':['CS','EC','ME','CS'],
       'regno':['183cs21011','183ec21003','183me21002','183cs21026'],
       'marks':[95,70,75,80],
        'college name':['GPTC','SJES','GJC','GPTC']}
df=pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt
plt.bar(df['names'],df['marks'],color='purple')
plt.xlabel('names')
plt.ylabel('marks')
plt.title("bar graph")
plt.show()




