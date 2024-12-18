import pandas as pd
 
# s1=pd.Series([1,2,3,45,5],index=["a","b","c","e","d"])
# print(s1)
# s1=pd.DataFrame([1,2,3,45,5],index=["a","b","c","e","d"])
# print(s1)
s1= planet_gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
s2=pd.DataFrame(s1,index=["1","2","3","4","5","6","7"])
s2["name"]=[1,2,3,4,5,6,7]
s1=pd.Series([1,2,3,45,5,8,9,10],index=s2.columns)
s2.loc[8] = s1
s3 = s2.drop("3",axis=0)
print(s3.iloc[1:3])
print(s3.iloc[6])