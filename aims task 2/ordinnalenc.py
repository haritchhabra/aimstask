import pandas as pd
data = {'SOCIETY': ['AIMS','YUVAAN','NSS'],
        'CATEGORY': ['TECH','CULTURAL','SOCIAL SERVICE']}
df=pd.DataFrame(data)

newsoc={'TECH': 1,'CULTURAL':2,'SOCIAL SERVICE':3}

df['category_encoding']=df['CATEGORY'].map(newsoc)

print(df)